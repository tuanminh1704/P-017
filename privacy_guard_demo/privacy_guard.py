"""
============================================================
  PRIVACY-UTILITY RELEASE GUARD
  Framework đánh giá trade-off Privacy vs Utility
  khi che khuôn mặt trong ảnh đường phố
============================================================

PIPELINE:
  [1] Phát hiện khuôn mặt (PII) bằng MediaPipe Face Detection
  [2] Áp dụng 7 cấu hình che mờ (blur / pixelate / blackout)
  [3] Đo Privacy: miss rate + re-detection attack
  [4] Đo Utility: YOLO person detection retention
  [5] Slice Analysis: đánh giá theo kích thước mặt
  [6] Pareto Frontier + Release Gate quyết định

CÁCH CHẠY:
  1. pip install -r requirements.txt
  2. Bỏ ảnh vào thư mục 'input_images/'
  3. python privacy_guard.py
  4. Xem kết quả trong 'results/'
"""

import cv2
import os
import glob
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # Render offline, không cần GUI
import matplotlib.pyplot as plt
import mediapipe as mp
from ultralytics import YOLO
from datetime import datetime

# ================================================================
#  CẤU HÌNH CHUNG
# ================================================================

INPUT_DIR = "input_images"
RESULTS_DIR = "results"
OUTPUT_IMG_DIR = os.path.join(RESULTS_DIR, "images")

# --- Ngưỡng Release Gate ---
# Privacy: miss rate tối đa cho phép (sót >5% mặt → BLOCK)
PRIVACY_THRESHOLD = 0.05
# Utility: mức sụt giảm tối đa cho phép (mất >10% người → quá tệ)
UTILITY_DROP_THRESHOLD = 0.10

# --- 7 cấu hình che mờ (Config Grid) ---
# Mỗi config là một "núm vặn" khác nhau trên chiếc bập bênh Privacy-Utility
CONFIGS = [
    {"id": "blur_light",   "method": "blur",     "kernel": 21, "label": "Blur nhẹ (k=21)"},
    {"id": "blur_medium",  "method": "blur",     "kernel": 51, "label": "Blur vừa (k=51)"},
    {"id": "blur_heavy",   "method": "blur",     "kernel": 99, "label": "Blur mạnh (k=99)"},
    {"id": "pixel_light",  "method": "pixelate", "factor": 6,  "label": "Pixel nhẹ (f=6)"},
    {"id": "pixel_medium", "method": "pixelate", "factor": 12, "label": "Pixel vừa (f=12)"},
    {"id": "pixel_heavy",  "method": "pixelate", "factor": 20, "label": "Pixel nặng (f=20)"},
    {"id": "blackout",     "method": "blackout", "factor": 0,  "label": "Tô đen (Blackout)"},
]


# ================================================================
#  KHỞI TẠO MÔ HÌNH
# ================================================================

def init_models():
    """Tải sẵn các mô hình AI cần dùng."""
    print("=" * 60)
    print("  PRIVACY-UTILITY RELEASE GUARD")
    print("  Đang khởi tạo hệ thống...")
    print("=" * 60)

    # Face Detection: MediaPipe (chính xác hơn Haar Cascade rất nhiều)
    print("[1/2] Tải MediaPipe Face Detection...")
    mp_face = mp.solutions.face_detection
    face_det = mp_face.FaceDetection(
        model_selection=1,         # 1 = full-range (phát hiện mặt xa tới ~5m)
        min_detection_confidence=0.5,
    )

    # Person Detection: YOLOv8-nano (tự tải trọng số nếu chưa có)
    print("[2/2] Tải YOLOv8 Person Detector...")
    yolo = YOLO("yolov8n.pt")

    print("[OK]  Sẵn sàng!\n")
    return face_det, yolo


# ================================================================
#  PHÁT HIỆN KHUÔN MẶT
# ================================================================

def detect_faces(img, face_detector):
    """
    Trả về danh sách khuôn mặt: [(x, y, w, h, confidence), ...]
    Dùng MediaPipe — chính xác hơn Haar Cascade rất nhiều,
    đặc biệt với mặt nghiêng, ánh sáng yếu.
    """
    h_img, w_img = img.shape[:2]
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detector.process(rgb)

    faces = []
    if results.detections:
        for det in results.detections:
            bb = det.location_data.relative_bounding_box
            x = max(0, int(bb.xmin * w_img))
            y = max(0, int(bb.ymin * h_img))
            w = min(int(bb.width * w_img), w_img - x)
            h = min(int(bb.height * h_img), h_img - y)
            conf = det.score[0]
            if w > 5 and h > 5:
                faces.append((x, y, w, h, conf))
    return faces


# ================================================================
#  CÁC PHƯƠNG PHÁP CHE MỜ (PRIVACY MECHANISMS)
# ================================================================

def _padded_roi(img, x, y, w, h, pad_ratio=0.15):
    """Mở rộng vùng che thêm 15% mỗi chiều để không bị sót mép mặt."""
    px = int(w * pad_ratio)
    py = int(h * pad_ratio)
    x1 = max(0, x - px)
    y1 = max(0, y - py)
    x2 = min(img.shape[1], x + w + px)
    y2 = min(img.shape[0], y + h + py)
    return x1, y1, x2, y2


def apply_blur(img, x, y, w, h, kernel):
    """Gaussian Blur — làm nhòe mượt vùng mặt."""
    x1, y1, x2, y2 = _padded_roi(img, x, y, w, h)
    roi = img[y1:y2, x1:x2]
    img[y1:y2, x1:x2] = cv2.GaussianBlur(roi, (kernel, kernel), 0)
    return img


def apply_pixelate(img, x, y, w, h, factor):
    """Pixelate — biến vùng mặt thành các ô vuông khảm."""
    x1, y1, x2, y2 = _padded_roi(img, x, y, w, h)
    roi = img[y1:y2, x1:x2]
    rh, rw = roi.shape[:2]
    sw = max(1, rw // factor)
    sh = max(1, rh // factor)
    small = cv2.resize(roi, (sw, sh), interpolation=cv2.INTER_LINEAR)
    img[y1:y2, x1:x2] = cv2.resize(small, (rw, rh), interpolation=cv2.INTER_NEAREST)
    return img


def apply_blackout(img, x, y, w, h):
    """Blackout — tô đen kín vùng mặt."""
    x1, y1, x2, y2 = _padded_roi(img, x, y, w, h)
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 0), -1)
    return img


def anonymize(img, faces, config):
    """Áp dụng một config che mờ lên tất cả khuôn mặt trong ảnh."""
    out = img.copy()
    method = config["method"]
    for (x, y, w, h, _) in faces:
        if method == "blur":
            out = apply_blur(out, x, y, w, h, config["kernel"])
        elif method == "pixelate":
            out = apply_pixelate(out, x, y, w, h, config["factor"])
        elif method == "blackout":
            out = apply_blackout(out, x, y, w, h)
    return out


# ================================================================
#  ĐO PRIVACY (Bước 4a)
# ================================================================

def eval_privacy(original_faces, blurred_img, face_detector):
    """
    Đo Privacy bằng RE-DETECTION ATTACK:
      - Chạy lại face detector lên ảnh ĐÃ che mờ.
      - Nếu detector vẫn thấy mặt ở vùng đã che → Privacy thất bại.
      - Miss Rate = số mặt rò rỉ / tổng số mặt gốc.
    """
    if len(original_faces) == 0:
        return {"miss_rate": 0.0, "faces_leaked": 0, "total_faces": 0}

    redetected = detect_faces(blurred_img, face_detector)

    # Đếm mặt "rò rỉ": mặt phát hiện lại trùng vị trí với mặt gốc
    leaked = 0
    for (rx, ry, rw, rh, _) in redetected:
        for (ox, oy, ow, oh, _) in original_faces:
            # Tính vùng giao nhau (intersection)
            ix1 = max(rx, ox)
            iy1 = max(ry, oy)
            ix2 = min(rx + rw, ox + ow)
            iy2 = min(ry + rh, oy + oh)
            if ix2 > ix1 and iy2 > iy1:
                leaked += 1
                break  # Mỗi mặt re-detect chỉ tính 1 lần

    miss_rate = leaked / len(original_faces)
    return {
        "miss_rate": round(miss_rate, 4),
        "faces_leaked": leaked,
        "total_faces": len(original_faces),
    }


# ================================================================
#  ĐO UTILITY (Bước 4b)
# ================================================================

def eval_utility(original_img, blurred_img, yolo):
    """
    Đo Utility = khả năng AI downstream vẫn hoạt động tốt.
    So sánh số người YOLOv8 đếm được trên ảnh gốc vs ảnh đã che.
    """
    orig_res = yolo(original_img, classes=[0], verbose=False)
    blur_res = yolo(blurred_img, classes=[0], verbose=False)

    orig_n = len(orig_res[0].boxes)
    blur_n = len(blur_res[0].boxes)

    orig_confs = orig_res[0].boxes.conf.cpu().numpy() if orig_n > 0 else np.array([])
    blur_confs = blur_res[0].boxes.conf.cpu().numpy() if blur_n > 0 else np.array([])

    retention = (blur_n / orig_n) if orig_n > 0 else 1.0
    return {
        "original_count": orig_n,
        "blurred_count": blur_n,
        "retention": round(retention, 4),
        "utility_drop": round(1.0 - retention, 4),
        "orig_avg_conf": round(float(orig_confs.mean()), 4) if len(orig_confs) else 0.0,
        "blur_avg_conf": round(float(blur_confs.mean()), 4) if len(blur_confs) else 0.0,
    }


# ================================================================
#  SLICE ANALYSIS (Bước 5 — phân tích theo trường hợp khó)
# ================================================================

SLICE_BINS = [
    ("small  (<40px)",  0,  40),
    ("medium (40-100px)", 40, 100),
    ("large  (>100px)", 100, 9999),
]


def face_slice(face):
    """Phân loại khuôn mặt theo chiều cao pixel."""
    h = face[3]
    for name, lo, hi in SLICE_BINS:
        if lo <= h < hi:
            return name
    return "unknown"


def build_slice_stats(original_faces, blurred_img, face_detector):
    """Tính miss-rate riêng cho từng slice."""
    stats = {name: {"total": 0, "leaked": 0} for name, _, _ in SLICE_BINS}

    # Đếm tổng mặt theo slice
    for f in original_faces:
        s = face_slice(f)
        if s in stats:
            stats[s]["total"] += 1

    # Đếm mặt rò rỉ theo slice
    redetected = detect_faces(blurred_img, face_detector)
    for (rx, ry, rw, rh, _) in redetected:
        for of in original_faces:
            ox, oy, ow, oh = of[:4]
            ix1, iy1 = max(rx, ox), max(ry, oy)
            ix2, iy2 = min(rx + rw, ox + ow), min(ry + rh, oy + oh)
            if ix2 > ix1 and iy2 > iy1:
                s = face_slice(of)
                if s in stats:
                    stats[s]["leaked"] += 1
                break

    # Tính miss-rate
    for s in stats:
        t = stats[s]["total"]
        stats[s]["miss_rate"] = round(stats[s]["leaked"] / t, 4) if t > 0 else 0.0
    return stats


# ================================================================
#  PARETO FRONTIER (Bước 6)
# ================================================================

def pareto_indices(points):
    """
    Tìm tập Pareto-optimal.
    Mỗi point = (miss_rate, utility_drop) — cả hai đều muốn nhỏ.
    """
    n = len(points)
    is_pareto = [True] * n
    for i in range(n):
        if not is_pareto[i]:
            continue
        for j in range(n):
            if i == j:
                continue
            # j dominate i nếu j tốt hơn hoặc bằng ở cả 2 chiều, và tốt hơn ít nhất 1 chiều
            if (points[j][0] <= points[i][0] and points[j][1] <= points[i][1]
                    and (points[j][0] < points[i][0] or points[j][1] < points[i][1])):
                is_pareto[i] = False
                break
    return [i for i in range(n) if is_pareto[i]]


def plot_pareto(results, path):
    """Vẽ biểu đồ Pareto Frontier với vùng an toàn / nguy hiểm."""
    mrs = [r["privacy"]["miss_rate"] for r in results]
    uds = [r["utility"]["utility_drop"] for r in results]
    labels = [r["config"]["label"] for r in results]

    pidx = pareto_indices(list(zip(mrs, uds)))

    fig, ax = plt.subplots(figsize=(11, 7))

    # Tô vùng an toàn (xanh nhạt)
    ax.axvspan(0, PRIVACY_THRESHOLD, color="#d4edda", alpha=0.35, label="Vùng Privacy an toàn")
    ax.axhspan(0, UTILITY_DROP_THRESHOLD, color="#cce5ff", alpha=0.35, label="Vùng Utility chấp nhận")

    # Vạch ngưỡng
    ax.axvline(PRIVACY_THRESHOLD, color="red", ls="--", lw=1.2,
               label=f"Privacy threshold ({PRIVACY_THRESHOLD*100:.0f}%)")
    ax.axhline(UTILITY_DROP_THRESHOLD, color="orange", ls="--", lw=1.2,
               label=f"Utility-drop max ({UTILITY_DROP_THRESHOLD*100:.0f}%)")

    # Đường Pareto
    pareto_pts = sorted([(mrs[i], uds[i]) for i in pidx])
    if pareto_pts:
        px, py = zip(*pareto_pts)
        ax.plot(px, py, "b-o", ms=4, alpha=0.5, label="Pareto frontier")

    # Các điểm config
    for i in range(len(results)):
        ok_p = mrs[i] <= PRIVACY_THRESHOLD
        ok_u = uds[i] <= UTILITY_DROP_THRESHOLD
        color = "green" if (ok_p and ok_u) else ("orange" if ok_p else "red")
        marker = "★" if (ok_p and ok_u) else "●"
        ax.scatter(mrs[i], uds[i], c=color, s=180, zorder=5, edgecolors="black", linewidths=0.8)
        ax.annotate(labels[i], (mrs[i], uds[i]),
                    textcoords="offset points", xytext=(10, 6), fontsize=8)

    ax.set_xlabel("Privacy Miss-Rate  (↓ thấp = an toàn hơn)", fontsize=12)
    ax.set_ylabel("Utility Drop  (↓ thấp = hữu dụng hơn)", fontsize=12)
    ax.set_title("PARETO FRONTIER — Privacy vs Utility Trade-off", fontsize=14, weight="bold")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, alpha=0.25)
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Chart] Pareto  → {path}")


def plot_slices(results, path):
    """Vẽ biểu đồ cột miss-rate theo Slice cho từng config."""
    slice_names = [s for s, _, _ in SLICE_BINS]
    n_cfg = len(results)

    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(slice_names))
    w = 0.8 / n_cfg

    for i, r in enumerate(results):
        mrs = []
        for s in slice_names:
            mrs.append(r["slices"].get(s, {}).get("miss_rate", 0) * 100)
        ax.bar(x + i * w, mrs, w, label=r["config"]["label"])

    ax.axhline(PRIVACY_THRESHOLD * 100, color="red", ls=":", lw=1.2,
               label=f"Threshold ({PRIVACY_THRESHOLD*100:.0f}%)")
    ax.set_xticks(x + w * n_cfg / 2)
    ax.set_xticklabels(slice_names)
    ax.set_xlabel("Face Slice (kích thước khuôn mặt)")
    ax.set_ylabel("Miss-Rate (%)")
    ax.set_title("SLICE ANALYSIS — Miss-Rate theo loại khuôn mặt", fontsize=13, weight="bold")
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.25, axis="y")
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Chart] Slices  → {path}")


def plot_utility_bar(results, path):
    """Vẽ biểu đồ cột so sánh Utility Retention của các config."""
    labels = [r["config"]["label"] for r in results]
    retentions = [r["utility"]["retention"] * 100 for r in results]
    colors = []
    for r in results:
        if "RELEASE" in r["gate"]:
            colors.append("#28a745")
        elif r["utility"]["utility_drop"] > UTILITY_DROP_THRESHOLD:
            colors.append("#fd7e14")
        else:
            colors.append("#dc3545")

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.barh(labels, retentions, color=colors, edgecolor="black", linewidth=0.5)
    ax.axvline((1 - UTILITY_DROP_THRESHOLD) * 100, color="orange", ls="--",
               label=f"Ngưỡng tối thiểu ({(1-UTILITY_DROP_THRESHOLD)*100:.0f}%)")
    ax.set_xlabel("Utility Retention (%)")
    ax.set_title("SO SÁNH UTILITY — Số người YOLO đếm được so với ảnh gốc", fontsize=13, weight="bold")
    ax.legend()
    ax.grid(True, alpha=0.25, axis="x")
    # Ghi giá trị lên cột
    for bar, val in zip(bars, retentions):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
                f"{val:.1f}%", va="center", fontsize=9)
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Chart] Utility → {path}")


# ================================================================
#  PIPELINE CHÍNH
# ================================================================

def run_pipeline():
    face_detector, yolo = init_models()

    # Tạo thư mục
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # Quét ảnh đầu vào
    image_paths = []
    for ext in ("*.jpg", "*.jpeg", "*.png", "*.bmp", "*.webp"):
        image_paths.extend(glob.glob(os.path.join(INPUT_DIR, ext)))

    if not image_paths:
        print(f"\n[!] Thư mục '{INPUT_DIR}/' trống.")
        print(f"    Hãy bỏ ảnh đường phố vào đó rồi chạy lại.\n")
        return

    print(f"[INFO] Tìm thấy {len(image_paths)} ảnh.\n")

    # --- Chạy từng Config ---
    all_results = []

    for cfg in CONFIGS:
        cid = cfg["id"]
        print(f"{'─'*60}")
        print(f"  ▶ CONFIG: {cfg['label']}")
        print(f"{'─'*60}")

        out_dir = os.path.join(OUTPUT_IMG_DIR, cid)
        os.makedirs(out_dir, exist_ok=True)

        agg_faces = 0
        agg_leaked = 0
        agg_orig_n = 0
        agg_blur_n = 0
        agg_slices = {s: {"total": 0, "leaked": 0} for s, _, _ in SLICE_BINS}

        for img_path in image_paths:
            name = os.path.basename(img_path)
            orig = cv2.imread(img_path)
            if orig is None:
                continue

            # [1] Phát hiện mặt
            faces = detect_faces(orig, face_detector)

            # [2] Che mờ
            blurred = anonymize(orig, faces, cfg)
            cv2.imwrite(os.path.join(out_dir, name), blurred)

            # [3] Đo Privacy
            priv = eval_privacy(faces, blurred, face_detector)
            agg_faces += priv["total_faces"]
            agg_leaked += priv["faces_leaked"]

            # [4] Đo Utility
            util = eval_utility(orig, blurred, yolo)
            agg_orig_n += util["original_count"]
            agg_blur_n += util["blurred_count"]

            # [5] Slice
            sl = build_slice_stats(faces, blurred, face_detector)
            for s in agg_slices:
                agg_slices[s]["total"] += sl.get(s, {}).get("total", 0)
                agg_slices[s]["leaked"] += sl.get(s, {}).get("leaked", 0)

            print(f"    {name:30s}  mặt={len(faces):2d}  lộ={priv['faces_leaked']:2d}  "
                  f"người(gốc/mờ)={util['original_count']}/{util['blurred_count']}")

        # Tổng kết config
        miss_rate = (agg_leaked / agg_faces) if agg_faces > 0 else 0.0
        retention = (agg_blur_n / agg_orig_n) if agg_orig_n > 0 else 1.0
        u_drop = 1.0 - retention

        # Tính miss-rate từng slice
        slice_out = {}
        worst_mr = 0.0
        for s in agg_slices:
            t = agg_slices[s]["total"]
            l = agg_slices[s]["leaked"]
            mr = (l / t) if t > 0 else 0.0
            slice_out[s] = {"total": t, "leaked": l, "miss_rate": round(mr, 4)}
            worst_mr = max(worst_mr, mr)

        # --- RELEASE GATE ---
        p_pass = miss_rate <= PRIVACY_THRESHOLD
        u_pass = u_drop <= UTILITY_DROP_THRESHOLD
        gate = "✅ RELEASE" if (p_pass and u_pass) else "❌ BLOCK"

        result = {
            "config": cfg,
            "privacy": {"miss_rate": round(miss_rate, 4), "total": agg_faces,
                        "leaked": agg_leaked, "worst_slice_mr": round(worst_mr, 4), "pass": p_pass},
            "utility": {"retention": round(retention, 4), "utility_drop": round(u_drop, 4),
                        "orig_count": agg_orig_n, "blur_count": agg_blur_n, "pass": u_pass},
            "slices": slice_out,
            "gate": gate,
        }
        all_results.append(result)

        tag_p = "✅" if p_pass else "❌"
        tag_u = "✅" if u_pass else "❌"
        print(f"\n  ── Kết quả ──")
        print(f"  Privacy Miss-Rate : {miss_rate*100:5.1f}%  {tag_p}")
        print(f"  Utility Drop      : {u_drop*100:5.1f}%  {tag_u}")
        print(f"  Worst-Slice MR    : {worst_mr*100:5.1f}%")
        print(f"  >>> GATE: {gate}\n")

    # ============================================================
    #  BÁO CÁO TỔNG KẾT
    # ============================================================
    print("=" * 60)
    print("  RELEASE GATE — BÁO CÁO TỔNG KẾT")
    print("=" * 60)

    rows = []
    for r in all_results:
        rows.append({
            "Config": r["config"]["label"],
            "Miss-Rate(%)": round(r["privacy"]["miss_rate"] * 100, 1),
            "Worst-Slice(%)": round(r["privacy"]["worst_slice_mr"] * 100, 1),
            "Utility-Drop(%)": round(r["utility"]["utility_drop"] * 100, 1),
            "Retention(%)": round(r["utility"]["retention"] * 100, 1),
            "Decision": r["gate"],
        })

    df = pd.DataFrame(rows)
    print(df.to_string(index=False))

    # Lưu CSV
    csv_path = os.path.join(RESULTS_DIR, "release_gate_report.csv")
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    print(f"\n[CSV]  → {csv_path}")

    # Lưu JSON chi tiết
    json_path = os.path.join(RESULTS_DIR, "privacy_utility_report.json")
    report = {
        "timestamp": datetime.now().isoformat(),
        "thresholds": {"privacy": PRIVACY_THRESHOLD, "utility_drop": UTILITY_DROP_THRESHOLD},
        "total_images": len(image_paths),
        "configs": [],
    }
    for r in all_results:
        report["configs"].append({
            "id": r["config"]["id"],
            "label": r["config"]["label"],
            "miss_rate": r["privacy"]["miss_rate"],
            "worst_slice_mr": r["privacy"]["worst_slice_mr"],
            "utility_drop": r["utility"]["utility_drop"],
            "retention": r["utility"]["retention"],
            "slices": r["slices"],
            "gate": r["gate"],
        })
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"[JSON] → {json_path}")

    # Vẽ biểu đồ
    print()
    plot_pareto(all_results, os.path.join(RESULTS_DIR, "pareto_frontier.png"))
    plot_slices(all_results, os.path.join(RESULTS_DIR, "slice_analysis.png"))
    plot_utility_bar(all_results, os.path.join(RESULTS_DIR, "utility_comparison.png"))

    # --- Chọn config tốt nhất ---
    passed = [r for r in all_results if "RELEASE" in r["gate"]]
    print()
    if passed:
        best = min(passed, key=lambda r: r["utility"]["utility_drop"])
        print("=" * 60)
        print(f"  🏆 PHƯƠNG PHÁP ĐƯỢC CHỌN: {best['config']['label']}")
        print(f"     Privacy Miss-Rate : {best['privacy']['miss_rate']*100:.1f}%")
        print(f"     Utility Drop      : {best['utility']['utility_drop']*100:.1f}%")
        print(f"     Worst-Slice MR    : {best['privacy']['worst_slice_mr']*100:.1f}%")
        print("=" * 60)
    else:
        print("=" * 60)
        print("  ⛔ KHÔNG CÓ CONFIG NÀO ĐẠT CHUẨN — BLOCK TẤT CẢ")
        print("     → Cần cải thiện Face Detector hoặc nới ngưỡng.")
        print("=" * 60)

    print(f"\n[DONE] Toàn bộ kết quả nằm trong thư mục '{RESULTS_DIR}/'")


# ================================================================
if __name__ == "__main__":
    run_pipeline()
