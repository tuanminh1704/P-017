# Nhật ký tuần 02 · 22/09 – 26/09/2026

**Lead tuần này:** 
- Nguyễn Hải Nam (@namng11) (Lead Human Pose)
- Chu Đình Thắng (@thangchudinh1) (Lead Face Landmark)

**Dữ liệu / task CVAT:** 
- Task 1: Human-Pose (Pre-label & Without pre-label)
- Task 2: Face Landmark (Pre-label & Without pre-label)

## Thành viên và phân công

| Thành viên | Vị trí | Phân công tuần này |
|---|---|---|
| Nguyễn Hải Nam (@namng11) | Lead (Human Pose) | Gán nhãn Job 2378, 2374 (Face Landmark) |
| Chu Đình Thắng (@thangchudinh1) | Lead (Face Landmark) | Gán nhãn Job 2368, 2372 (Human Pose) |
| Vũ Tuấn Minh (@tuanminh1704) | Annotator | Gán nhãn Job 2367, 2371 (Human Pose) |
| Vũ Tuấn Minh (@tuanminh1704) | Annotator | Gán nhãn Job 2376, 2380 (Face Landmark) |
| Âu Xuân Mạnh (@ManhAu1111) | Annotator | Gán nhãn Job 2369, 2373 (Human Pose) |
| Âu Xuân Mạnh (@ManhAu1111) | Annotator | Gán nhãn Job 2377, 2381 (Face Landmark) |
| Nguyễn Hữu Tài (@tainguyenhuu2509-droid) | Reviewer · Annotator | Gán nhãn Job 2366, 2370 (Human Pose) |
| Nguyễn Hữu Tài (@tainguyenhuu2509-droid) | Reviewer · Annotator | Gán nhãn Job 2375, 2379 (Face Landmark) |

## Công việc

| # | Nội dung công việc | Annotator | Reviewer | Hoàn thành | Ghi chú |
|---|---|---|---|---|---|
| 1 | Job 2366, 2370 (Human Pose) | @tainguyenhuu2509-droid | @thangchudinh1 | ✅ 100% | Đã gán xong và qua review chéo |
| 2 | Job 2367, 2371 (Human Pose) | @tuanminh1704 | @ManhAu1111 | ✅ 100% | Đã gán xong và qua review chéo |
| 3 | Job 2368, 2372 (Human Pose) | @thangchudinh1 | @tainguyenhuu2509-droid | ✅ 100% | Đã gán xong và qua review chéo |
| 4 | Job 2369, 2373 (Human Pose) | @ManhAu1111 | @tuanminh1704 | ✅ 100% | Đã gán xong và qua review chéo |
| 5 | Job 2376, 2380 (Face Landmark) | @tuanminh1704 | @thangchudinh1 | ✅ 100% | Đã gán xong và qua review chéo |
| 6 | Job 2374, 2378 (Face Landmark) | @namng11 | @tuanminh1704 | ✅ 100% | Đã gán xong và qua review chéo |
| 7 | Job 2375, 2379 (Face Landmark) | @tainguyenhuu2509-droid | @namng11 | ✅ 100% | Đã gán xong và qua review chéo |
| 8 | Job 2377, 2381 (Face Landmark) | @ManhAu1111 | @tainguyenhuu2509-droid | ✅ 100% | Đã gán xong và qua review chéo |


Mức hoàn thành: ✅ xong **và đã qua review** · 🟡 đang làm (ghi %) · ⛔ bị chặn (ghi lý do) · ⬜ chưa bắt đầu

## Tổng kết

- Đã gán (Human Pose): 60/60 ảnh (Hoàn thành 100%)
- Qua review lần đầu (Human Pose): 60/60 ảnh (Tất cả đã qua review chéo thành công)
- Đã gán (Face Landmark): 70/70 ảnh (Hoàn thành 100%)
- Qua review lần đầu (Face Landmark): 70/70 ảnh (Tất cả đã qua review chéo thành công)
- Edge case mới / đã chốt (Open Issue trên CVAT): Đã chốt luật P-014, P-015, P-016 (đã đưa vào Sổ Quyết Định) và mở thêm Issue P-017 về việc che khuất cơ thể do trang phục.

## Vướng mắc

- Một số ảnh có góc chụp khuất (quay ngang đầu, mặc áo dày) gây khó khăn cho ước lượng, vẫn đang chờ thêm ý kiến Mentor ở mục P-017.

## Kế hoạch tuần sau (và phần còn lại của tuần)

- **Lead Face Landmark (@thangchudinh1)** chốt danh sách phân công job và người review chéo cho 4 thành viên còn lại.
- Toàn đội tập trung tổng lực sang gán nhãn 60 ảnh của bài toán Face Landmark (Task 2).
- Các thành viên tự học và áp dụng bám sát bản tóm tắt [Sổ tay gán nhãn Face Landmark](face-landmark-summary.md) vừa biên soạn.
- Nhóm sẽ push kết quả bài báo cáo này lên git đúng hạn vào tối cuối tuần.

## Status từng thành viên

**Nguyễn Hải Nam (@namng11)**

• **Done — Đã hoàn thành:**
Hoàn thành 2 job Face Landmark (Job 2374, 2378) | Self-Review xong | Đã hoàn thành Cross-Review cho các thành viên khác.

• **Doing — Đang làm gì:**
Tự review và sửa lại các annotation bị sai so với guideline.

• **Blocked — Vướng mắc:**
Chưa có vướng mắc nào trong 2 job cá nhân đã làm.

• **Link — Link code/demo:**
Không có.

• **Questions — Câu hỏi cho Coach:**
Không có.

---

**Âu Xuân Mạnh (@ManhAu1111)**

• **Done — Đã hoàn thành:**
Hoàn thành toàn bộ các job được phân công (Human Pose & Face Landmark) | Self-Review xong | Đã hoàn thành Cross-Review.

• **Doing — Đang làm gì:**
Tự review và sửa lại các annotation bị sai do chưa bám sát kỹ và chưa hiểu sâu guideline (đã thảo luận và rút kinh nghiệm cùng nhóm).

• **Blocked — Vướng mắc:**
Trường hợp tài xế mặc áo khoác dày, áo phao làm biến dạng form cơ thể thật (đã ghi nhận thành Issue P-017).

• **Link — Link code/demo:**
Không có.

• **Questions — Câu hỏi cho Coach:**
Về case áo khoác dày (P-017), nên ghim điểm ở mặt ngoài của áo phồng hay ước lượng trừ hao lùi vào vị trí xương thịt thật bên trong rồi đánh Occluded?

---

**Vũ Tuấn Minh (@tuanminh1704)**

• **Done — Đã hoàn thành:**
Hoàn thành toàn bộ các job được phân công (Human Pose & Face Landmark) | Self-Review xong | Đã hoàn thành Cross-Review.

• **Doing — Đang làm gì:**
Sửa lỗi annotation cá nhân do đọc sót guideline. Đã trao đổi kỹ với nhóm để thống nhất cách làm.

• **Blocked — Vướng mắc:**
Không còn vướng mắc. Trải nghiệm khó khăn khi thân trên bị sách/bìa che khuất (P-016) đã được Mentor giải đáp và chốt luật.

• **Link — Link code/demo:**
Không có.

• **Questions — Câu hỏi cho Coach:**
Không có.

---

**Nguyễn Hữu Tài (@tainguyenhuu2509-droid)**

• **Done — Đã hoàn thành:**
Hoàn thành toàn bộ các job được phân công (Human Pose & Face Landmark) | Self-Review xong | Đã hoàn thành Cross-Review.

• **Doing — Đang làm gì:**
Review lại các frame dễ nhầm lẫn và sửa annotation sai lệch do chưa nắm chắc guideline ban đầu.

• **Blocked — Vướng mắc:**
Không còn vướng mắc. Các trường hợp điểm cơ thể bị dây đai an toàn che (P-014) và mắt bị che bởi kính râm/kính lóa (P-015) đều đã được Mentor giải đáp và chốt luật rõ ràng.

• **Link — Link code/demo:**
Không có.

• **Questions — Câu hỏi cho Coach:**
Không có.

---

**Chu Đình Thắng (@thangchudinh1)**

• **Done — Đã hoàn thành:**
Hoàn thành toàn bộ các job cá nhân được phân công | Self-Review xong | Đã hoàn thành Cross-Review. Lên kế hoạch chia job Face Landmark cho toàn đội.

• **Doing — Đang làm gì:**
Tự sửa lại annotation cá nhân bị lỗi do chưa bám sát guideline. Hỗ trợ team rà soát lại các case lấn cấn.

• **Blocked — Vướng mắc:**
Chưa có vướng mắc nào phát sinh. 

• **Link — Link code/demo:**
Không có.

• **Questions — Câu hỏi cho Coach:**
Không có.
