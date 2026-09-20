# Nhật ký tuần 01 · 15/09 – 21/09/2026

> **File ví dụ** — tên, số liệu và link đều là giả. Tuần mới thì copy
> [`_mau-tuan.md`](_mau-tuan.md) thành `tuan-02.md`.

**Lead tuần này:** @thanh-vien-a
**Dữ liệu / task CVAT:** Ảnh giao thông đô thị — [task 12](https://cvat.example.com/tasks/12)

## Thành viên và phân công

| Thành viên | Vị trí | Phân công tuần này |
|---|---|---|
| Vũ Tuấn Minh (@tuanminh1704) | Lead | Chia job, chốt edge case, review xác suất 10% mọi job |
| Âu Xuân Mạnh (@ManhAu1111) | Annotator | Job 1613 |
| Chu Đình Thắng (@thangchudinh1) | Annotator | Job 1612 |
| Nguyễn Hải Nam (@namng11) | Annotator | Job 1611 |
| Nguyễn Hữu Tài (@tainguyenhuu2509-droid) | Reviewer · Annotator | Review job 1611,1612,1613; gán job 1610 |

Nguyễn Hữu Tài vừa review vừa gán, nên job 1610 do Lead review.

## Công việc

| # | Nội dung công việc | Annotator | Reviewer | Hoàn thành | Ghi chú |
|---|---|---|---|---|---|
| 1 | Job 1613 — 25 ảnh| @ManhAu1111 | @tuanminh1704 | ✅ 100% | Hoàn thành |
| 2 | Job 1612 — 25 ảnh | @thangchudinh1 | @tuanminh1704| 🟡 96% | Review trả về 1 ảnh |
| 3 | Job 1611 — 25 ảnh | @namng11| @tuanminh1704| ✅ 100% |Hoàn thành |
| 4 | Job 1610 — 25 ảnh | @tainguyenhuu2509-droid | @tuanminh1704 | ✅ 100%  | Hoàn thành |
| ̀5 | Job 1397 — 25 ảnh| @ManhAu1111 | @tainguyenhuu2509-droid | |  |
| 6 | Job 1396 — 25 ảnh | @thangchudinh1 | @tainguyenhuu2509-droid| |  |
| 7 | Job 1395 — 25 ảnh | @namng11| tainguyenhuu2509-droid|  | |
| 8 | Job 1394 — 25 ảnh | @tuanminh1704 | @tainguyenhuu2509-droid |  |  |
| 9 | Đọc lại guideline §3, gom các ca chưa rõ | @tuanminh1704 | — |  | |


Mức hoàn thành: ✅ xong **và đã qua review** · 🟡 đang làm (ghi %) · ⛔ bị chặn (ghi lý do) · ⬜ chưa bắt đầu

## Tổng kết

- Đã gán: 425 / 1.250 ảnh (34%)
- Qua review lần đầu: 88% (trả lại 51 ảnh)
- Edge case mới: P-001, P-002, P-003 — đã chốt P-001 thành [QĐ-001](../so-quyet-dinh.md#qđ-001)

## Vướng mắc

- P-002 (xe bị che khuất) chưa chốt nên job 103 phải dừng. Lead đã gửi câu hỏi lên BTC.
- P-003: vẽ lại box y hệt qua các frame liên tiếp mất ~40% thời gian job 105.
  Đang cân nhắc làm tool trong [`source-tool/`](../source-tool/).

## Kế hoạch tuần 02

- Chốt P-002, mở lại job 103.
- Xong job 102, 104, 105.
- Quyết định có làm tool cho P-003 hay dùng chế độ Track sẵn có của CVAT.
