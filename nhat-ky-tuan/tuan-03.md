# Nhật ký tuần 03 · 28/09 – 03/10/2026

**Lead tuần này:** 
- Âu Xuân Mạnh (@ManhAu1111) (Lead 3D Cuboid Annotation)

**Dữ liệu / task CVAT:** 
- Task 1: 3D Cuboid Annotation (LiDAR Point Cloud + 6 Camera Context Images)

## Thành viên và phân công

| Thành viên | Vị trí | Phân công tuần này |
|---|---|---|
| Âu Xuân Mạnh (@ManhAu1111) | Lead (3D Cuboid) | Gán nhãn Job 3974 |
| Nguyễn Hải Nam (@namng11) | Annotator | Gán nhãn Job 3971 |
| Nguyễn Hữu Tài (@tainguyenhuu2509-droid) | Annotator | Gán nhãn Job 3973 |
| Chu Đình Thắng (@thangchudinh1) | Annotator | Gán nhãn Job 3972 |
| Vũ Tuấn Minh (@tuanminh1704) | Reviewer · QA | Đóng vai trò Reviewer chính (chuẩn bị review chéo) |

## Công việc

| # | Nội dung công việc | Annotator | Reviewer | Hoàn thành | Ghi chú |
|---|---|---|---|---|---|
| 1 | Job 3974 (3D Cuboid - 8 frames) | @ManhAu1111 | @tuanminh1704 | 🟡 100% | Đã gán nhãn xong (chưa review chéo) |
| 2 | Job 3971 (3D Cuboid - 11 frames) | @namng11 | @tuanminh1704 | 🟡 100% | Đã gán nhãn xong (chưa review chéo) |
| 3 | Job 3973 (3D Cuboid - 11 frames) | @tainguyenhuu2509-droid | @namng11 | 🟡 100% | Đã gán nhãn xong (chưa review chéo) |
| 4 | Job 3972 (3D Cuboid - 11 frames) | @thangchudinh1 | @ManhAu1111 | 🟡 50% | Đang tiến hành gán nhãn (chưa review chéo) |


Mức hoàn thành: ✅ xong **và đã qua review** · 🟡 đang làm (ghi %) · ⛔ bị chặn (ghi lý do) · ⬜ chưa bắt đầu

## Tổng kết

- Đã gán (3D Cuboid): 35/41 frames (Hoàn thành ~85% tổng số frames của đợt báo cáo giữa tuần, 3/4 job đã gán xong 100%).
- Qua review lần đầu (3D Cuboid): 0/41 frames (Chưa tiến hành review chéo, mới hoàn thành phần gán nhãn giữa tuần).
- Edge case mới / đã chốt (Open Issue trên CVAT): Các thành viên áp dụng chuẩn quy tắc fit 3D cuboid ôm sát vật thể, đáy box tiếp xúc mặt đất, yaw đúng hướng và gộp đồ cá nhân (như vali) vào `pedestrian`. Chỉ ghi nhận ở mức backlog, chưa bổ sung Sổ Quyết Định trong đợt báo cáo giữa tuần.

## Vướng mắc

- Chưa có vướng mắc mới. Tất cả thành viên đều nắm chắc thao tác và quy tắc 3D Cuboid Annotation trên CVAT.

## Kế hoạch tuần sau (và phần còn lại của tuần)

- **Chu Đình Thắng (@thangchudinh1):** Tập trung hoàn thành 50% còn lại của Job 3972 (6 frames còn lại).
- **Vũ Tuấn Minh (@tuanminh1704):** Bắt đầu tiến hành review chéo chi tiết cho Job 3974 và Job 3971.
- **Nguyễn Hải Nam & Nguyễn Hữu Tài:** Chuẩn bị review chéo Job 3973 và hỗ trợ review Job 3972 sau khi Thắng hoàn tất gán nhãn.
- **Lead Âu Xuân Mạnh (@ManhAu1111):** Đôn đốc tiến độ gán nhãn và review chéo toàn nhóm trước khi nộp báo cáo chính thức vào cuối tuần.

## Status từng thành viên

**Nguyễn Hải Nam (@namng11)**

• **Done — Đã hoàn thành:**
Hoàn thành 100% phần Gán nhãn Job 3971 (11 frames) | Self-Review xong.

• **Doing — Đang làm gì:**
Chuẩn bị thực hiện Review chéo cho Job 3973.

• **Blocked — Vướng mắc:**
Không có vướng mắc nào trong job cá nhân.

• **Link — Link code/demo:**
Không có.

• **Questions — Câu hỏi cho Coach:**
Không có.

---

**Âu Xuân Mạnh (@ManhAu1111)**

• **Done — Đã hoàn thành:**
Hoàn thành 100% phần Gán nhãn Job 3974 (8 frames) | Phân công công việc và lập kế hoạch giữa tuần cho nhóm.

• **Doing — Đang làm gì:**
Theo dõi tiến độ gán nhãn chung, đôn đốc các thành viên và chuẩn bị review Job 3972 sau khi Thắng gán xong.

• **Blocked — Vướng mắc:**
Không có vướng mắc nào.

• **Link — Link code/demo:**
Không có.

• **Questions — Câu hỏi cho Coach:**
Không có.

---

**Vũ Tuấn Minh (@tuanminh1704)**

• **Done — Đã hoàn thành:**
Sẵn sàng nhận nhiệm vụ Reviewer chính.

• **Doing — Đang làm gì:**
Chuẩn bị tiến hành Review chéo cho Job 3974 (@ManhAu1111) và Job 3971 (@namng11).

• **Blocked — Vướng mắc:**
Không có vướng mắc nào.

• **Link — Link code/demo:**
Không có.

• **Questions — Câu hỏi cho Coach:**
Không có.

---

**Nguyễn Hữu Tài (@tainguyenhuu2509-droid)**

• **Done — Đã hoàn thành:**
Hoàn thành 100% phần Gán nhãn Job 3973 (11 frames) | Self-Review xong.

• **Doing — Đang làm gì:**
Phối hợp kiểm tra lại các cuboid và chờ bắt đầu review chéo.

• **Blocked — Vướng mắc:**
Không có vướng mắc nào.

• **Link — Link code/demo:**
Không có.

• **Questions — Câu hỏi cho Coach:**
Không có.

---

**Chu Đình Thắng (@thangchudinh1)**

• **Done — Đã hoàn thành:**
Đã gán nhãn 50% Job 3972 (11 frames).

• **Doing — Đang làm gì:**
Tiếp tục hoàn thiện 50% còn lại của Job 3972.

• **Blocked — Vướng mắc:**
Không có vướng mắc nào.

• **Link — Link code/demo:**
Không có.

• **Questions — Câu hỏi cho Coach:**
Không có.
