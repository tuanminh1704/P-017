# Problem backlog

Những chỗ gặp trong lúc gán nhãn mà **guideline chưa trả lời được**, cộng các pain point về công cụ.

Ghi ngay khi gặp, kể cả lúc chưa biết xử lý thế nào. Một edge case không được ghi lại thì
mỗi người sẽ tự xử lý theo một kiểu — và đó là nguồn lớn nhất của nhãn không nhất quán.

> Các mục bên dưới là **ví dụ**, tên và link CVAT đều giả. Mẫu trống để copy nằm cuối file.

## Danh sách

| Mã | Tóm tắt | Loại | Mục guideline | Trạng thái | Kết quả |
|---|---|---|---|---|---|
| [P-001](#p-001) | Người ngồi sau xe máy: box riêng hay gộp với người lái | Guideline mơ hồ | §3.2 | ✅ Đã chốt | [QĐ-001](so-quyet-dinh.md#qđ-001) |
| [P-002](#p-002) | Xe bị che khuất hơn một nửa | Guideline chưa nói tới | §3.4 | ↗️ Hỏi BTC | — |
| [P-003](#p-003) | Phải vẽ lại box y hệt qua nhiều frame liên tiếp | Pain point công cụ | — | 🗣️ Đang bàn | — |
| [P-004](#p-004) | Vật thể bị che khuất/chia cắt thành nhiều mảng rời rạc | Guideline chưa nói tới | — | 🔴 Mở | — |
| [P-005](#p-005) | Các phụ kiện đi kèm (ăng-ten, ống khói, túi xách, cốc...) có tính vào vật thể | Guideline chưa nói tới | — | 🔴 Mở | — |
| [P-006](#p-006) | Vật thể ở quá xa, quá mờ không xác định rõ class hoặc ranh giới | Guideline chưa nói tới | — | 🔴 Mở | — |
| [P-007](#p-007) | Xử lý chồng đè pixel: đối tượng nhỏ nằm lọt trong nền đối tượng khác | Pain point công cụ | — | 🔴 Mở | — |
| [P-008](#p-008) | Tán cây / nhánh cây đan xen chồng lấn ở sát mép ảnh | Guideline mơ hồ | — | 🔴 Mở | — |
| [P-009](#p-009) | Vạch kẻ qua đường và vạch sơn trên mặt đường (road) | Guideline chưa nói tới | — | 🔴 Mở | — |
| [P-010](#p-010) | Định nghĩa cụ thể và phạm vi của class `pole` | Guideline mơ hồ | — | 🔴 Mở | — |
| [P-011](#p-011) | Người đi bộ chỉ có phụ kiện (balo, túi xách) bị cắt ở mép ảnh (truncated) | Guideline chưa nói tới | — | 🔴 Mở | — |
| [P-012](#p-012) | Biển báo quay lưng / không nhìn thấy nội dung mặt trước | Guideline chưa nói tới | — | 🔴 Mở | — |
| [P-013](#p-013) | Xe bị vật thể khác cắt ngang chia thành 2 phần rời rạc | Guideline chưa nói tới | — | 🔴 Mở | — |
| [P-014](#p-014) | Điểm Hông (Hip) bị cắt ngang/che khuất bởi dây đai an toàn | Guideline chưa nói tới | §3.3 | 🔴 Mở | — |
| [P-015](#p-015) | Mắt (Eye) bị che khuất bởi kính râm hoặc gọng kính / kính lóa | Guideline chưa nói tới | §3.1 | 🔴 Mở | — |
| [P-016](#p-016) | Điểm thân trên bị che khuất hoàn toàn bởi vật thể lớn cầm tay (sách, bìa) | Guideline chưa nói tới | §3.2 | 🔴 Mở | — |

**Loại**

| Loại | Nghĩa là |
|---|---|
| Guideline chưa nói tới | Tình huống không có trong guideline |
| Guideline mơ hồ | Đọc guideline ra được hai cách hiểu trở lên |
| Guideline mâu thuẫn | Hai mục trong guideline nói ngược nhau |
| Pain point công cụ | Guideline rõ, nhưng làm trên CVAT chậm hoặc dễ sai |

**Trạng thái:** 🔴 Mở · 🗣️ Đang bàn · ↗️ Hỏi BTC · ✅ Đã chốt (trỏ sang QĐ) · 🛠️ Làm tool (trỏ sang `source-tool/`) · ⚪ Bỏ (ghi lý do)

---

## P-001

**Người ngồi sau xe máy: box riêng hay gộp chung với người lái**

- **Loại:** Guideline mơ hồ
- **Mục guideline:** §3.2 — "mỗi người một bounding box"
- **Người phát hiện:** @thanh-vien-b · 16/09/2026
- **Link CVAT:**
  - https://cvat.example.com/tasks/12/jobs/101?frame=37 — hai người, gần như chồng khít
  - https://cvat.example.com/tasks/12/jobs/101?frame=112 — người ngồi sau chỉ lộ đầu
- **Mô tả:** §3.2 nói mỗi người một box, nhưng hình minh hoạ trong guideline lại vẽ một box
  cho cả xe máy lẫn người trên xe.
- **Các cách hiểu:**
  1. Theo câu chữ: người ngồi sau có box `nguoi` riêng.
  2. Theo hình minh hoạ: không vẽ box `nguoi` cho ai đang ngồi trên xe.
- **Xử lý tạm trong lúc chờ:** vẽ box riêng và gắn tag `can_xem_lai` để dễ lọc ra sửa.
- **Kết quả:** ✅ [QĐ-001](so-quyet-dinh.md#qđ-001)

## P-002

**Xe bị che khuất hơn một nửa**

- **Loại:** Guideline chưa nói tới
- **Mục guideline:** §3.4 — chỉ nói về vật thể bị cắt ở mép ảnh, không nói về bị che
- **Người phát hiện:** @thanh-vien-c · 17/09/2026
- **Link CVAT:**
  - https://cvat.example.com/tasks/12/jobs/103?frame=8 — ô tô sau xe buýt, lộ khoảng 30%
  - https://cvat.example.com/tasks/12/jobs/103?frame=64 — xe máy sau cột điện, lộ khoảng 50%
- **Mô tả:** Không rõ có gán nhãn vật thể bị che không, và nếu có thì box ôm phần nhìn thấy
  hay ôm cả phần ước lượng bị che.
- **Các cách hiểu:**
  1. Bỏ qua khi lộ dưới 50%.
  2. Luôn gán, box chỉ ôm phần nhìn thấy.
  3. Luôn gán, box ôm cả phần ước lượng.
- **Xử lý tạm trong lúc chờ:** dừng job 103, chuyển sang job khác ít ca che khuất.
- **Kết quả:** ↗️ Đã hỏi BTC ngày 18/09/2026, chờ trả lời.

## P-003

**Phải vẽ lại box y hệt qua nhiều frame liên tiếp**

- **Loại:** Pain point công cụ
- **Mục guideline:** —
- **Người phát hiện:** @thanh-vien-d · 18/09/2026
- **Link CVAT:** https://cvat.example.com/tasks/12/jobs/105?frame=200 — frame 200–260, xe đỗ không di chuyển
- **Mô tả:** Ảnh chụp liên tiếp từ camera cố định. Xe đỗ bên đường xuất hiện y nguyên ở hàng chục
  frame, annotator phải vẽ lại ở từng frame. Ước tính chiếm ~40% thời gian job 105.
- **Hướng đang cân nhắc:**
  1. Dùng chế độ *Track* sẵn có của CVAT — cần thử xem có hợp với dữ liệu dạng ảnh rời không.
  2. Viết script đọc file export của CVAT, nhân box sang các frame kế tiếp, rồi import lại.
- **Kết quả:** 🗣️ Đang bàn. Nếu chọn hướng 2 thì đổi trạng thái sang 🛠️ và làm trong
  [`source-tool/`](source-tool/).

## P-004

**Vật thể bị che khuất/chia cắt thành nhiều mảng rời rạc**

- **Loại:** Guideline chưa nói tới
- **Mục guideline:** —
- **Người phát hiện:** @tainguyenhuu2509-droid · 17/09/2026
- **Link CVAT:**
  - `w1/segmentation/G03/G03_S001.jpg` — Tòa nhà (building) bị cây/cột che chia cắt; vỉa hè (sidewalk) bị hàng rào chia thành các phần không dính nhau; ranh giới nối chỉ rộng vài pixel mờ
  - `w1/segmentation/G03/G03_S002.jpg` — 'sky', 'building', 'road', 'sidewalk' bị tách thành 2 hoặc nhiều phần riêng biệt
- **Mô tả:** Trong semantic segmentation, nhiều đối tượng thuộc cùng một nhãn (building, sidewalk, sky, road) bị đối tượng khác nằm phía trước chắn ngang (như cột, hàng rào, tán cây), làm phân mảnh thành nhiều mảng pixel rời rạc (multipolygon). Chưa rõ có gom chung một nhãn hay vẽ các polygon rời rạc, và các vùng kết nối siêu nhỏ (vài pixel mờ) có tính là nối hay bị cắt đứt.
- **Các cách hiểu:**
  1. Vẽ các polygon/mask rời rạc riêng lẻ nhưng gán cùng một class (hỗ trợ multipolygon / disjoint mask).
  2. Nếu vùng che khuất quá hẹp hoặc chỉ còn vài pixel mờ, vẽ nối liền đè qua (hoặc ước lượng).
  3. Bỏ qua các mảng nhỏ lẻ bị tách ra nếu diện tích dưới một ngưỡng nhất định.
- **Xử lý tạm trong lúc chờ:** Vẽ các polygon rời rạc cùng gán class đó; với các pixel mờ không rõ ràng thì ưu tiên vật thể phía trước (foreground).
- **Kết quả:** 🔴 Mở

## P-005

**Các phụ kiện đi kèm (ăng-ten, ống khói, túi xách, cốc...) có tính vào vật thể**

- **Loại:** Guideline chưa nói tới
- **Mục guideline:** —
- **Người phát hiện:** @tainguyenhuu2509-droid · 17/09/2026
- **Link CVAT:**
  - `w1/segmentation/G03/G03_S001.jpg` — Ống khói, ăng-ten của tòa nhà; các chi tiết nhô ra của xe hơi (car)
  - `w1/segmentation/G03/G03_S002.jpg` — Túi xách, cốc cầm trên tay của người đi bộ (pedestrian)
- **Mô tả:** Chưa có quy định rõ về việc các phụ kiện gắn liền hoặc được mang bởi đối tượng có được tính vào mask/polygon của đối tượng đó hay không.
- **Các cách hiểu:**
  1. Tính toàn bộ phụ kiện gắn liền/mang theo vào mask/box của đối tượng (ví dụ: người bao gồm cả balo, túi xách, cốc cầm tay; toà nhà bao gồm cả ống khói, ăng-ten; xe bao gồm gương chiếu hậu, phụ kiện gắn nóc).
  2. Chỉ gán phần thân chính, bỏ qua các phụ kiện rời rạc/nhỏ (như ăng-ten, cốc nước).
  3. Đặt ra ngưỡng kích thước hoặc danh mục phụ kiện được phép tính kèm.
- **Xử lý tạm trong lúc chờ:** Tạm thời gán gộp phụ kiện vào đối tượng mang nó nếu dính liền; gắn tag `can_xem_lai`.
- **Kết quả:** 🔴 Mở

## P-006

**Vật thể ở quá xa, quá mờ không xác định rõ class hoặc ranh giới**

- **Loại:** Guideline chưa nói tới
- **Mục guideline:** —
- **Người phát hiện:** @tainguyenhuu2509-droid · 17/09/2026
- **Link CVAT:**
  - `w1/segmentation/G03/G03_S001.jpg` — Đối tượng ở xa, mờ khó phân biệt car hay truck, 1 toà nhà hay nhiều toà nhà
  - `w1/segmentation/G03/G03_S002.jpg` — Các toà nhà ở hậu cảnh quá xa mờ để tách thành từng toà riêng; người đi bộ ở xa quá mờ để nhận diện cấu trúc
- **Mô tả:** Các vật thể ở hậu cảnh hoặc xa camera bị suy giảm độ phân giải, nhoè mờ (heavy blur), không thể nhận diện chắc chắn class hoặc ranh giới giữa các cá thể.
- **Các cách hiểu:**
  1. Có ngưỡng kích thước tối thiểu (ví dụ: chiều cao/rộng < 10-15 px thì bỏ qua không gán).
  2. Vẫn cố gắng gán class gần giống nhất theo trực giác/bối cảnh.
  3. Với building ở xa không tách được thì gộp chung thành một mảng lớn; với xe/người quá mờ không phân biệt được thì bỏ qua hoặc gán nhãn `unknown/ignore` nếu có.
- **Xử lý tạm trong lúc chờ:** Đối với toà nhà ở xa gộp thành 1 mảng lớn; đối với xe/người quá mờ không nhận diện được hình thể thì tạm thời không gán.
- **Kết quả:** 🔴 Mở

## P-007

**Xử lý chồng đè pixel: đối tượng nhỏ nằm lọt trong nền đối tượng khác**

- **Loại:** Pain point công cụ
- **Mục guideline:** —
- **Người phát hiện:** @tainguyenhuu2509-droid · 17/09/2026
- **Link CVAT:**
  - `w1/segmentation/G03/G03_S002.jpg` — Đèn tín hiệu giao thông (traffic light) nằm gọn lọt bên trong vùng toà nhà (building)
- **Mô tả:** Trong semantic segmentation, mỗi pixel chỉ thuộc về đúng 1 class. Khi vẽ polygon cho toà nhà lớn bao trùm cả đèn tín hiệu, làm thế nào để mask của đèn tín hiệu không bị toà nhà đè lên hoặc ngược lại trên CVAT.
- **Hướng đang cân nhắc:**
  1. Dùng tính năng điều chỉnh thứ tự lớp (Z-Order / Layer stacking) trên CVAT: đưa layer của `traffic_light` lên trên `building`.
  2. Khi vẽ mask `building`, đục lỗ (hole) tại vị trí `traffic_light`.
  3. Dùng công cụ brush/eraser để kiểm soát ranh giới pixel chính xác khi export.
- **Xử lý tạm trong lúc chờ:** Vẽ `building` trước, sau đó vẽ `traffic_light` ở layer cao hơn (Z-Order lớn hơn).
- **Kết quả:** 🔴 Mở

## P-008

**Tán cây / nhánh cây đan xen chồng lấn ở sát mép ảnh**

- **Loại:** Guideline mơ hồ
- **Mục guideline:** —
- **Người phát hiện:** @tainguyenhuu2509-droid · 17/09/2026
- **Link CVAT:**
  - `w1/segmentation/G03/G03_S001.jpg` — Ở sát rìa trái, có 1 nhánh của cây khác chèn vào cây chính đang segment
- **Mô tả:** Các nhánh cây thuộc 2 cây khác nhau đan xen vào nhau, hoặc một nhánh cây ngoài rìa lọt vào tán cây đang gán nhãn. Khó xác định nhánh đó thuộc cây nào nếu gán nhãn dạng instance segmentation, hoặc có cần tách riêng không trong semantic segmentation.
- **Các cách hiểu:**
  1. Nếu là semantic segmentation (chỉ phân loại `vegetation` / `tree`): gộp chung toàn bộ thành 1 vùng thực vật duy nhất, không cần phân biệt từng cây.
  2. Nếu là instance segmentation: chỉ ước lượng theo trục thân cây, nhánh lấn sang thì cắt theo ranh giới dự đoán hoặc gán vào cây chiếm diện tích lớn hơn.
- **Xử lý tạm trong lúc chờ:** Nếu cùng class `vegetation` thì gộp chung vùng mask; nếu cần phân tách cá thể thì cắt theo ranh giới nhìn rõ nhất.
- **Kết quả:** 🔴 Mở

## P-009

**Vạch kẻ qua đường và vạch sơn trên mặt đường (road)**

- **Loại:** Guideline chưa nói tới
- **Mục guideline:** —
- **Người phát hiện:** @tainguyenhuu2509-droid · 17/09/2026
- **Link CVAT:**
  - `w1/segmentation/G03/G03_S001.jpg` — Phần vạch kẻ qua đường (zebra crossing) nằm trên mặt đường
- **Mô tả:** Guideline chưa làm rõ các vạch sơn giao thông, vạch kẻ người đi bộ qua đường (crosswalk) có được gộp chung vào class `road` hay có nhãn riêng (như `lane marking`, `crosswalk`).
- **Các cách hiểu:**
  1. Gộp toàn bộ vạch kẻ đường vào class `road`.
  2. Nếu bộ nhãn có class riêng cho marking/crosswalk thì phải bóc tách riêng.
- **Xử lý tạm trong lúc chờ:** Kiểm tra danh sách labels trong task CVAT; nếu không có class riêng về vạch kẻ đường thì toàn bộ thuộc về `road`.
- **Kết quả:** 🔴 Mở

## P-010

**Định nghĩa cụ thể và phạm vi của class `pole`**

- **Loại:** Guideline mơ hồ
- **Mục guideline:** —
- **Người phát hiện:** @tainguyenhuu2509-droid · 17/09/2026
- **Link CVAT:**
  - `w1/segmentation/G03/G03_S001.jpg` — Cần miêu tả chính xác class `pole`
- **Mô tả:** Thiếu mô tả chuẩn xác cho class `pole`: bao gồm những vật thể hình trụ/cột nào (cột đèn chiếu sáng, cột điện thoại/điện lực, cột biển báo giao thông, cọc rào, thân cây nhỏ có tính không?).
- **Các cách hiểu:**
  1. Chỉ tính các cột nhân tạo thẳng đứng có đường kính nhỏ (cột đèn, cột điện, cột biển báo).
  2. Bao gồm cả cọc rào thấp, cột camera, cột cờ.
  3. Cột gắn liền với biển báo/đèn giao thông thì tính vào `pole` hay tính vào `traffic sign` / `traffic light`.
- **Xử lý tạm trong lúc chờ:** Chỉ gán `pole` cho các cột nhân tạo dạng thẳng đứng độc lập (cột đèn, cột điện); cột biển báo gán chung hoặc tách theo hướng dẫn hiện tại của task.
- **Kết quả:** 🔴 Mở

## P-011

**Người đi bộ chỉ có phụ kiện (balo, túi xách) bị cắt ở mép ảnh (truncated)**

- **Loại:** Guideline chưa nói tới
- **Mục guideline:** —
- **Người phát hiện:** @tainguyenhuu2509-droid · 17/09/2026
- **Link CVAT:**
  - `w1/segmentation/G03/G03_S002.jpg` — Người đi bộ đeo túi xách sau lưng, cơ thể không chạm mép nhưng túi xách bị cắt ở mép ảnh
- **Mô tả:** Khi đánh thuộc tính/tag `truncated` (bị cắt ở mép ảnh), nếu thân thể người đi bộ vẫn nằm trọn trong ảnh nhưng chỉ có phụ kiện (balo, túi xách) chạm mép ảnh bị cắt một phần thì có đánh dấu đối tượng là `truncated` không?
- **Các cách hiểu:**
  1. Đánh dấu `truncated` vì phụ kiện là một phần của bounding box / mask người đó.
  2. Không đánh dấu `truncated` vì phần cơ thể người (body) vẫn nguyên vẹn bên trong khung hình.
- **Xử lý tạm trong lúc chờ:** Đánh dấu `truncated` và gắn tag `can_xem_lai` để dễ lọc ra cập nhật lại sau khi có quyết định.
- **Kết quả:** 🔴 Mở

## P-012

**Biển báo quay lưng / không nhìn thấy nội dung mặt trước**

- **Loại:** Guideline chưa nói tới
- **Mục guideline:** —
- **Người phát hiện:** @tainguyenhuu2509-droid · 17/09/2026
- **Link CVAT:**
  - `w1/bbox_polygon/G03/G03_B025.jpg` — Biển báo giao thông quay lưng vào camera, không thấy nội dung mặt trước
- **Mô tả:** Trong task bbox / polygon, có những biển báo giao thông hướng mặt sau về phía camera (chỉ nhìn thấy mặt kim loại xám/đen và thanh đỡ, không đọc được nội dung). Chưa rõ có cần vẽ box/polygon cho các biển báo này không, hoặc gán nhãn gì.
- **Các cách hiểu:**
  1. Vẫn gán nhãn `traffic_sign` cho tất cả biển báo kể cả nhìn từ phía sau, vì đó vẫn là vật thể biển báo.
  2. Bỏ qua không gán, vì mô hình phát hiện biển báo chỉ quan tâm đến biển báo điều khiển giao thông theo chiều nhìn.
  3. Gán với class chung `traffic_sign_back` hoặc thêm attribute `back_view`.
- **Xử lý tạm trong lúc chờ:** Tạm thời vẽ box/polygon với class biển báo chung và gắn tag `can_xem_lai`.
- **Kết quả:** 🔴 Mở

## P-013

**Xe bị vật thể khác cắt ngang chia thành 2 phần rời rạc (cách tô mask)**

- **Loại:** Guideline chưa nói tới
- **Mục guideline:** —
- **Người phát hiện:** @ManhAu1111 · 17/09/2026
- **Link CVAT:**
  - https://cvat.note.transformerlabs.ai/tasks/190/jobs/1613?frame=88 — Đầu ô tô phía sau bị gương của ô tô phía trước cắt ngang chia thành 2 phần
- **Mô tả:** Khi gán nhãn segmentation cho ô tô, phần đầu xe phía sau bị gương chiếu hậu của xe phía trước che khuất một phần ngang qua, khiến vùng nhìn thấy của đầu xe bị tách làm 2 mảng không liền nhau. Chưa rõ quy tắc tô mask: tô nối qua (ước lượng) hay chỉ tô phần nhìn thấy, và trên CVAT gom 2 mảng này như thế nào.
- **Các cách hiểu:**
  1. *Chỉ tô phần nhìn thấy (visible)*: Dùng công cụ Brush/Mask tô cả 2 mảng rời rạc thuộc cùng 1 object `car`, không tô đè lên gương xe phía trước. Nếu dùng Polygon thì vẽ 2 polygon rồi Group lại.
  2. *Tô ước lượng đè qua (amodal segmentation)*: Tô phủ kín đầu xe xuyên qua cả gương, sau đó dựa vào Z-Order/layer để xe phía trước đè lên xe phía sau.
- **Xử lý tạm trong lúc chờ:** Chỉ tô phần nhìn thấy thực tế (visible pixels). Dùng công cụ Brush tô cả 2 mảng rời rạc trên cùng 1 object xe; nếu dùng Polygon thì vẽ 2 polygon và ấn `G` để Group lại; bật attribute `occluded` nếu có.
- **Kết quả:** 🔴 Mở

---

## P-014

**Điểm Hông (Hip) bị che khuất bởi dây đai an toàn**

- **Loại:** Guideline chưa nói tới
- **Mục guideline:** §3.3
- **Người phát hiện:** @tainguyenhuu2509-droid · 24/09/2026
- **Link CVAT:**https://cvat.note.transformerlabs.ai/tasks/382/jobs/2366?frame=0 - Điểm Hông bị che khuất bởi dây đai an toàn
- **Mô tả:** Guideline §3.3 có hướng dẫn chi dưới bị che bởi vô-lăng, táp-lô nhưng không đề cập vật cản sát người như dây đai an toàn (vắt ngang bụng/hông).
- **Các cách hiểu:**
  1. *Ước lượng vị trí khớp háng từ trục đùi và thân trên* — Ghim điểm và đánh `Occluded`. (Hợp lý nhất với Human Pose).
  2. *Đánh `Outside`* — Nếu coi như không thấy trực tiếp ranh giới khớp.
- **Xử lý tạm trong lúc chờ:** Đang chờ Mentor phản hồi để chốt luật chung.
- **Kết quả:** 🔴 Mở

---

## P-015

**Mắt (Eye) bị che khuất bởi kính râm hoặc gọng kính / kính lóa**

- **Loại:** Guideline chưa nói tới
- **Mục guideline:** §3.1
- **Người phát hiện:** @tainguyenhuu2509-droid · 24/09/2026
- **Link CVAT:**https://cvat.note.transformerlabs.ai/tasks/382/jobs/2366?frame=0 - Mắt bị che bởi gọng kính 
- **Mô tả:** Guideline §3.1 chỉ hướng dẫn điểm mắt đặt ở "tâm đồng tử" hoặc "tâm khe mí" (nếu nhắm), nhưng không hướng dẫn xử lý khi mắt bị che bởi gọng kính lớn, kính râm đen, hoặc kính bị chói sáng.
- **Các cách hiểu:**
  1. *Ước lượng tâm đồng tử phía sau kính* — Ghim điểm và đánh `Occluded` (nếu kính trong/gọng nhỏ).
  2. *Đánh `Outside`* — Nếu kính râm đen kịt hoặc lóa sáng hoàn toàn không thể đoán được vị trí mắt.
- **Xử lý tạm trong lúc chờ:** Đang chờ Mentor phản hồi để chốt mức độ ước lượng cho phép.
- **Kết quả:** 🔴 Mở

---

## P-016

**Thân trên bị che khuất bởi vật thể lớn cầm tay (Sách, bìa hồ sơ)**

- **Loại:** Guideline chưa nói tới
- **Mục guideline:** §3.2
- **Người phát hiện:** @tuanminh1704 · 24/09/2026
- **Link CVAT:**https://cvat.note.transformerlabs.ai/tasks/382/jobs/2367?frame=9 - Tài xế cầm 1 quyển sách che kín phía tay bên trái
- **Mô tả:** Tài xế cầm một tấm bìa/sách rất to che kín hoàn toàn bả vai và khuỷu tay. Model pre-label đang bị lỗi: ghim thẳng các điểm khớp vai/khuỷu tay lên bề mặt của tấm bìa trắng. Guideline §3.3 có cấm ghim chi dưới lên ghế/cần số, nhưng chưa có luật cấm ghim thân trên lên vật thể cầm tay.
- **Các cách hiểu:**
  1. *Cố gắng ước lượng vị trí khớp phía sau tấm bìa* — Xóa điểm trên tấm bìa, đặt lại về phía sau và đánh `Occluded`. (Rủi ro sai số lớn do bị che quá rộng).
  2. *Đánh `Outside` toàn bộ cánh tay bị che* — Vì "bị che đến mức không còn căn cứ ước lượng" (theo §4.1).
- **Xử lý tạm trong lúc chờ:** Đang chờ Mentor phản hồi để chốt xem che tới mức nào thì được ước lượng (`Occluded`), mức nào thì phải loại bỏ (`Outside`).
- **Kết quả:** 🔴 Mở

---

## Mẫu để copy

```markdown
## P-NNN

**Tóm tắt một dòng**

- **Loại:** Guideline chưa nói tới | Guideline mơ hồ | Guideline mâu thuẫn | Pain point công cụ
- **Mục guideline:** §
- **Người phát hiện:** @ · dd/mm/yyyy
- **Link CVAT:** (bỏ trống nếu không có)
  - https://…/tasks/<id>/jobs/<id>?frame=<n> — frame này có gì
- **Mô tả:**
- **Các cách hiểu:** (với pain point công cụ thì ghi **Hướng đang cân nhắc:**)
  1.
  2.
- **Xử lý tạm trong lúc chờ:**
- **Kết quả:** 🔴 Mở
```

Nhớ thêm một dòng vào bảng **Danh sách** ở đầu file.
