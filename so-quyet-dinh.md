# Sổ quyết định

Ghi lại những gì đội đã chốt, và **vì sao**. Ba tuần sau không ai còn nhớ vì sao box lại vẽ
kiểu này — người mới vào đội lại càng không.

**Quyết định đã ghi thì không sửa nội dung.** Đổi ý thì ghi một quyết định mới, và chuyển
trạng thái quyết định cũ thành *Bị thay bởi QĐ-xxx*. Nhờ vậy vẫn truy được vì sao các job
cũ được gán theo cách cũ.

> Các mục bên dưới là **ví dụ**. Mẫu trống để copy nằm cuối file.

## Danh sách

| Mã | Quyết định | Ngày | Xuất phát từ | Trạng thái |
|---|---|---|---|---|
| [QĐ-001](#qđ-001) | Người ngồi sau xe máy có box `nguoi` riêng | 17/09/2026 | [P-001](problem-backlog.md#p-001) | Hiệu lực |
| [QĐ-002](#qđ-002) | Reviewer trả nguyên job khi mẫu kiểm có trên 10% ảnh sai | 19/09/2026 | Họp tuần 01 | Hiệu lực |

**Trạng thái:** Hiệu lực · Bị thay bởi QĐ-xxx · Huỷ (ghi lý do)

---

## QĐ-001

**Người ngồi sau xe máy có box `nguoi` riêng**

- **Ngày:** 17/09/2026
- **Người tham gia:** @thanh-vien-a (chốt), @thanh-vien-b, @thanh-vien-c, @thanh-vien-d
- **Xuất phát từ:** [P-001](problem-backlog.md#p-001)
- **Bối cảnh:** §3.2 của guideline nói mỗi người một box, nhưng hình minh hoạ lại vẽ chung một box.
  Hai annotator đang làm theo hai cách khác nhau.
- **Các phương án đã cân nhắc:**
  1. *Gộp chung một box với xe* — nhanh hơn, nhưng mất số người trên xe, trong khi dữ liệu dùng để
     đếm người tham gia giao thông. Loại.
  2. *Box `nguoi` riêng cho từng người* — đúng câu chữ §3.2 và giữ được số người. **Chọn.**
- **Quyết định:** Mỗi người trên xe máy, kể cả người ngồi sau chỉ lộ đầu, có một box `nguoi` riêng.
  Box xe máy vẫn vẽ như bình thường.
- **Việc phải làm theo:**
  - [x] Rà lại job 101, sửa 37 ảnh đã gộp (@thanh-vien-b)
  - [x] Báo cả đội, ghim trong kênh chat của đội
- **Trạng thái:** Hiệu lực

## QĐ-002

**Reviewer trả nguyên job khi mẫu kiểm có trên 10% ảnh sai**

- **Ngày:** 19/09/2026
- **Người tham gia:** @thanh-vien-a (chốt), @thanh-vien-d
- **Xuất phát từ:** Họp tổng kết tuần 01 — không phải từ backlog
- **Bối cảnh:** Job 101 bị sửa rải rác từng ảnh qua ba vòng review, tốn thời gian của cả hai bên.
- **Các phương án đã cân nhắc:**
  1. *Sửa từng ảnh như cũ* — ổn khi lỗi lẻ tẻ, nhưng khi lỗi có hệ thống thì reviewer đang làm hộ
     annotator. Loại.
  2. *Kiểm mẫu 20%, trên 10% sai thì trả nguyên job* — annotator tự rà cả job theo lỗi đã chỉ ra.
     **Chọn.**
- **Quyết định:** Reviewer kiểm ngẫu nhiên 20% ảnh của mỗi job. Trên 10% số ảnh kiểm bị sai thì trả
  nguyên job kèm danh sách lỗi mẫu; từ 10% trở xuống thì sửa từng ảnh.
- **Việc phải làm theo:**
  - [ ] Áp dụng từ job 106 trở đi (@thanh-vien-d)
- **Trạng thái:** Hiệu lực

## QĐ-003

**Sử dụng Track cho các object xuất hiện liên tục qua nhiều frame**

- **Ngày:** 18/09/2026
- **Người tham gia:** @tuanminh1704 (chốt)
- **Xuất phát từ:** [P-003](problem-backlog.md#p-003)
- **Bối cảnh:** Xe đỗ không di chuyển xuất hiện trong nhiều frame liên tiếp, khiến annotator phải vẽ lại cùng một box nhiều lần và chiếm nhiều thời gian.
- **Các phương án đã cân nhắc:**
  1. *Dùng chức năng Track của CVAT* — giảm thao tác thủ công, cần kiểm tra độ phù hợp với dữ liệu. **Chọn để thử nghiệm.**
  2. *Viết script nhân annotation sang các frame tiếp theo* — có thể tự động hóa nhưng cần xử lý export/import và kiểm tra lỗi. **Để dự phòng.**
- **Quyết định:** Thử nghiệm chức năng Track của CVAT trên một đoạn frame trước. Chỉ áp dụng rộng rãi nếu kết quả track chính xác và vẫn được reviewer kiểm tra.
- **Việc phải làm theo:**
  - [ ] Rà soát và cập nhật các annotation hiện có theo quy định này (@tuanminh1704)
- **Trạng thái:** Hiệu lực

## QĐ-004

**Semantic segmentation cho phép nhiều vùng rời rạc cùng thuộc một class**

- **Ngày:** 18/09/2026
- **Người tham gia:** @tuanminh1704 (chốt)
- **Xuất phát từ:** [P-004](problem-backlog.md#p-004)
- **Bối cảnh:** Building, sidewalk, sky hoặc road có thể bị cây, cột hoặc hàng rào che khuất và bị chia thành nhiều vùng pixel rời rạc.
- **Các phương án đã cân nhắc:**
  1. *Vẽ các polygon/mask rời rạc nhưng cùng class* — phản ánh đúng các pixel nhìn thấy. **Chọn tạm thời.**
  2. *Nối các vùng qua phần bị che* — phải suy đoán vùng không nhìn thấy. **Loại.**
  3. *Bỏ qua các mảng nhỏ* — có nguy cơ mất thông tin segmentation. **Loại tạm thời.**
- **Quyết định:** Các vùng nhìn thấy thuộc cùng một class được annotation riêng nhưng cùng gán một class. Không nối xuyên qua vật thể đang che khuất. Các ranh giới không rõ được đánh dấu `can_xem_lai`.
- **Việc phải làm theo:**
  - [ ] Rà soát và cập nhật các annotation hiện có theo quy định này (@tuanminh1704)
- **Trạng thái:** Hiệu lực


## QĐ-005

**Phụ kiện gắn liền được tạm thời tính vào object chính**

- **Ngày:** 18/09/2026
- **Người tham gia:** @tuanminh1704 (chốt)
- **Xuất phát từ:** [P-005](problem-backlog.md#p-005)
- **Bối cảnh:** Guideline chưa quy định rõ antenna, ống khói, túi xách, cốc hoặc các phụ kiện gắn/mang theo object có được tính vào mask/box hay không.
- **Các phương án đã cân nhắc:**
  1. *Gộp phụ kiện vào object chính* — đơn giản và tránh tạo label không tồn tại. **Chọn tạm thời.**
  2. *Chỉ annotation phần thân chính* — có thể làm mất các phần gắn liền của object. **Loại tạm thời.**
  3. *Đặt ngưỡng hoặc danh sách phụ kiện* — nhất quán hơn nhưng cần guideline chính thức. **Chờ xác nhận.**
- **Quyết định:** Tạm thời gộp phụ kiện vào object chính nếu phụ kiện gắn liền hoặc rõ ràng thuộc object đó. Các trường hợp nhỏ, rời rạc hoặc gây tranh cãi phải gắn `can_xem_lai`.
- **Việc phải làm theo:**
  - [ ] Rà soát và cập nhật các annotation hiện có theo quy định này (@tuanminh1704)
- **Trạng thái:** Hiệu lực


## QĐ-006

**Không gán nhãn object quá mờ nếu không xác định được class**

- **Ngày:** 18/09/2026
- **Người tham gia:** @tuanminh1704 (chốt)
- **Xuất phát từ:** [P-006](problem-backlog.md#p-006)
- **Bối cảnh:** Một số object ở xa hoặc bị blur mạnh không đủ thông tin để xác định class hoặc ranh giới.
- **Các phương án đã cân nhắc:**
  1. *Đặt ngưỡng kích thước tối thiểu* — dễ áp dụng nhưng file hiện tại chưa quy định ngưỡng cụ thể. **Chưa chọn.**
  2. *Cố gắng đoán class* — có nguy cơ tạo annotation sai. **Loại.**
  3. *Không gán khi không thể nhận diện* — tránh suy đoán sai. **Chọn tạm thời.**
- **Quyết định:** Chỉ gán nhãn khi object đủ rõ để xác định class. Object quá nhỏ hoặc quá mờ đến mức không nhận diện được thì tạm thời không gán và ghi nhận để reviewer xem xét. Với building ở xa nhưng vẫn xác định được vùng building, có thể gộp thành vùng lớn.
- **Việc phải làm theo:**
  - [ ] Rà soát và cập nhật các annotation hiện có theo quy định này (@tuanminh1704)
- **Trạng thái:** Hiệu lực


## QĐ-007

**Object foreground có class riêng phải được giữ lại trên background**

- **Ngày:** 18/09/2026
- **Người tham gia:** @tuanminh1704 (chốt)
- **Xuất phát từ:** [P-007](problem-backlog.md#p-007)
- **Bối cảnh:** Trong semantic segmentation, object nhỏ như `traffic_light` có thể nằm trong vùng lớn của `building`. Mỗi pixel chỉ thuộc một class nên cần xác định class nào chiếm pixel chồng lấn.
- **Các phương án đã cân nhắc:**
  1. *Để foreground đè lên background* — giữ được object nhỏ có class riêng. **Chọn.**
  2. *Để background đè lên foreground* — làm mất object nhỏ. **Loại.**
  3. *Đục hole trong mask background* — có thể sử dụng khi cần kiểm soát chính xác vùng foreground. **Chọn khi cần.**
- **Quyết định:** Object foreground có class riêng được ưu tiên tại các pixel tương ứng. Khi `traffic_light` nằm trước `building`, vùng pixel của đèn giao thông thuộc `traffic_light`, không thuộc `building`.
- **Việc phải làm theo:**
  - [ ] Rà soát và cập nhật các annotation hiện có theo quy định này (@tuanminh1704)
- **Trạng thái:** Hiệu lực


## QĐ-008

**Các vùng vegetation cùng class được gộp theo semantic class**

- **Ngày:** 18/09/2026
- **Người tham gia:** @tuanminh1704 (chốt)
- **Xuất phát từ:** [P-008](problem-backlog.md#p-008)
- **Bối cảnh:** Các nhánh của nhiều cây có thể đan xen, đặc biệt tại mép ảnh, gây khó khăn khi xác định ranh giới từng cây.
- **Các phương án đã cân nhắc:**
  1. *Gộp các vùng cùng class vegetation* — phù hợp với semantic segmentation. **Chọn nếu task là semantic segmentation.**
  2. *Tách từng cây* — cần thiết cho instance segmentation nhưng khó thực hiện khi nhánh chồng lấn. **Chỉ áp dụng nếu task yêu cầu instance.**
- **Quyết định:** Với semantic segmentation, các vùng thực vật cùng class được gán cùng class và không cần tách từng cây. Nếu task yêu cầu instance segmentation thì phải tách các cá thể khi ranh giới có thể xác định được.
- **Việc phải làm theo:**
  - [ ] Rà soát và cập nhật các annotation hiện có theo quy định này (@tuanminh1704)
- **Trạng thái:** Hiệu lực


## QĐ-009

**Vạch đường chỉ được tách riêng khi task có label tương ứng**

- **Ngày:** 18/09/2026
- **Người tham gia:** @tuanminh1704 (chốt)
- **Xuất phát từ:** [P-009](problem-backlog.md#p-009)
- **Bối cảnh:** Chưa rõ crosswalk và lane marking có phải class riêng hay được gộp vào `road`.
- **Các phương án đã cân nhắc:**
  1. *Gộp vào `road` khi task không có class riêng* — không tạo thêm label ngoài schema. **Chọn tạm thời.**
  2. *Tách thành `lane_marking` / `crosswalk`* — phù hợp nếu task đã định nghĩa class riêng. **Chọn khi label tồn tại.**
- **Quyết định:** Kiểm tra label schema của task. Nếu không có class riêng cho `lane_marking` hoặc `crosswalk`, không tạo label mới và xử lý theo schema hiện tại của task. Nếu task có class riêng thì phải annotation riêng.
- **Việc phải làm theo:**
  - [ ] Rà soát và cập nhật các annotation hiện có theo quy định này (@tuanminh1704)
- **Trạng thái:** Hiệu lực


## QĐ-010

**Tạm thời chỉ gán `pole` cho cột nhân tạo dạng đứng rõ ràng**

- **Ngày:** 18/09/2026
- **Người tham gia:** @tuanminh1704 (chốt)
- **Xuất phát từ:** [P-010](problem-backlog.md#p-010)
- **Bối cảnh:** Guideline chưa định nghĩa rõ `pole`, đặc biệt với cọc rào, cột camera, cột cờ, thân cây hoặc cột gắn biển báo.
- **Các phương án đã cân nhắc:**
  1. *Chỉ tính các cột nhân tạo đứng rõ ràng như cột đèn/cột điện* — dễ áp dụng và hạn chế nhầm class. **Chọn tạm thời.**
  2. *Bao gồm mọi vật thể dạng cột* — phạm vi quá rộng khi guideline chưa quy định. **Loại.**
  3. *Phân loại theo object gắn trên cột* — cần guideline cụ thể hơn. **Chờ xác nhận.**
- **Quyết định:** Tạm thời gán `pole` cho các cột nhân tạo dạng đứng rõ ràng như cột đèn hoặc cột điện. Không tự động gán thân cây hoặc cọc rào vào `pole`. Trường hợp không rõ được đưa vào `can_xem_lai`.
- **Việc phải làm theo:**
- [ ] Rà soát và cập nhật các annotation hiện có theo quy định này (@tuanminh1704)
- **Trạng thái:** Hiệu lực


## QĐ-011

**Phụ kiện bị cắt ở mép ảnh được đánh dấu `truncated` tạm thời**

- **Ngày:** 18/09/2026
- **Người tham gia:** @tuanminh1704 (chốt)
- **Xuất phát từ:** [P-011](problem-backlog.md#p-011)
- **Bối cảnh:** Người đi bộ không chạm mép ảnh nhưng balo/túi xách là một phần đi kèm lại bị cắt ở mép ảnh. Guideline chưa quy định rõ có đánh dấu `truncated` hay không.
- **Các phương án đã cân nhắc:**
  1. *Đánh dấu `truncated`* — nhất quán nếu phụ kiện được xem là một phần của object. **Chọn tạm thời.**
  2. *Không đánh dấu `truncated` nếu body vẫn nằm trong ảnh* — phù hợp nếu chỉ body được xem xét. **Chờ xác nhận.**
- **Quyết định:** Tạm thời đánh dấu `truncated` khi phần được xem là một phần của object bị cắt ở mép ảnh. Gắn `can_xem_lai` để reviewer cập nhật nếu BTC có quy định khác.
- **Việc phải làm theo:**
 - [ ] Rà soát và cập nhật các annotation hiện có theo quy định này (@tuanminh1704)
- **Trạng thái:** Hiệu lực


## QĐ-012

**Biển báo quay lưng vẫn được gán class `traffic_sign` tạm thời**

- **Ngày:** 18/09/2026
- **Người tham gia:** @tuanminh1704 (chốt)
- **Xuất phát từ:** [P-012](problem-backlog.md#p-012)
- **Bối cảnh:** Một số biển báo chỉ nhìn thấy mặt sau, không thể đọc nội dung mặt trước. Guideline chưa nói rõ có annotation hay không.
- **Các phương án đã cân nhắc:**
  1. *Gán `traffic_sign` cho biển báo nhìn từ phía sau* — vẫn nhận diện được vật thể là biển báo. **Chọn tạm thời.**
  2. *Bỏ qua biển báo quay lưng* — tránh annotation những biển không có nội dung nhìn thấy nhưng có thể làm mất object. **Chờ xác nhận.**
  3. *Tạo class `traffic_sign_back`* — yêu cầu thay đổi label schema. **Loại khi chưa được phép.**
- **Quyết định:** Tạm thời gán `traffic_sign` cho biển báo quay lưng nếu có thể xác định rõ đó là biển báo. Không tạo class mới. Gắn `can_xem_lai` cho trường hợp không chắc chắn.
- **Việc phải làm theo:**
- [ ] Rà soát và cập nhật các annotation hiện có theo quy định này (@tuanminh1704)
- **Trạng thái:** hiệu lực


## QĐ-013

**Object bị che thành nhiều vùng được annotation theo phần nhìn thấy**

- **Ngày:** 18/09/2026
- **Người tham gia:** @tuanminh1704 (chốt)
- **Xuất phát từ:** [P-013](problem-backlog.md#p-013)
- **Bối cảnh:** Một object như ô tô có thể bị vật thể phía trước che ngang, làm phần nhìn thấy bị chia thành hai hoặc nhiều vùng rời nhau.
- **Các phương án đã cân nhắc:**
  1. *Chỉ tô phần nhìn thấy* — không suy đoán phần bị che, phù hợp với visible pixels. **Chọn tạm thời.**
  2. *Tô xuyên qua phần bị che theo amodal segmentation* — cần ước lượng phần không nhìn thấy và guideline hiện chưa yêu cầu. **Loại tạm thời.**
- **Quyết định:** Chỉ annotation các pixel nhìn thấy thực tế của object. Nếu cùng một object bị chia thành nhiều vùng nhìn thấy, các vùng đó vẫn thuộc cùng object. Không tô xuyên qua vật thể đang che khuất. Nếu task có attribute `occluded`, đánh dấu tương ứng.
- **Việc phải làm theo:**
 - [ ] Rà soát và cập nhật các annotation hiện có theo quy định này (@tuanminh1704)
- **Trạng thái:** Hiệu lực
---

## Mẫu để copy

```markdown
## QĐ-NNN

**Quyết định trong một dòng**

- **Ngày:** dd/mm/yyyy
- **Người tham gia:** @ (chốt), @, @
- **Xuất phát từ:** [P-NNN](problem-backlog.md#p-nnn) | Họp tuần NN | …
- **Bối cảnh:** vì sao phải quyết định
- **Các phương án đã cân nhắc:**
  1. *Phương án* — ưu / nhược. Loại hoặc **Chọn.**
  2. *Phương án* — ưu / nhược. Loại hoặc **Chọn.**
- **Quyết định:** đủ rõ để người không dự họp vẫn làm đúng
- **Việc phải làm theo:**
  - [ ] việc (@người phụ trách)
- **Trạng thái:** Hiệu lực
```

Nhớ thêm một dòng vào bảng **Danh sách** ở đầu file, và đóng mục P-xxx tương ứng trong backlog.
