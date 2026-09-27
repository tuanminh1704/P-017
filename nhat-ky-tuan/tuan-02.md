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
| Âu Xuân Mạnh (@ManhAu1111) | Annotator | Gán nhãn Job 2369, 2373 (Human Pose) |
| Nguyễn Hữu Tài (@tainguyenhuu2509-droid) | Reviewer · Annotator | Gán nhãn Job 2366, 2370 (Human Pose) |

## Công việc

| # | Nội dung công việc | Annotator | Reviewer | Hoàn thành | Ghi chú |
|---|---|---|---|---|---|
| 1 | Job 2378, 2374 (Face Landmark) | @namng11 | [Chưa có] | 🟡 100% (chờ review) | Job 2378: tự dựng, 2374: prelabel |
| 2 | Các Job Face Landmark khác | [Chờ Lead Face (@thangchudinh1) chia] | | | |
| 3 | Job 2366, 2370 (Human Pose) | @tainguyenhuu2509-droid | @thangchudinh1 | ✅ 100% | Đã gán xong và qua review chéo |
| 4 | Job 2367, 2371 (Human Pose) | @tuanminh1704 | @ManhAu1111 | ✅ 100% | Đã gán xong và qua review chéo |
| 5 | Job 2368, 2372 (Human Pose) | @thangchudinh1 | @tainguyenhuu2509-droid | ✅ 100% | Đã gán xong và qua review chéo |
| 6 | Job 2369, 2373 (Human Pose) | @ManhAu1111 | @tuanminh1704 | ✅ 100% | Đã gán xong và qua review chéo |

Mức hoàn thành: ✅ xong **và đã qua review** · 🟡 đang làm (ghi %) · ⛔ bị chặn (ghi lý do) · ⬜ chưa bắt đầu

## Tổng kết

- Đã gán (Human Pose): 60/60 ảnh (Hoàn thành 100%)
- Qua review lần đầu (Human Pose): 60/60 ảnh (Tất cả đã qua review chéo thành công)
- Đã gán (Face Landmark): Đã xong 2 job của @namng11 (Chờ tổng hợp toàn đội)
- Qua review lần đầu (Face Landmark): [Chờ Lead Face Landmark điền]
- Edge case mới / đã chốt (Open Issue trên CVAT): Đã chốt luật P-014, P-015, P-016 (đã đưa vào Sổ Quyết Định) và mở thêm Issue P-017 về việc che khuất cơ thể do trang phục.

## Vướng mắc

- Task Face Landmark hiện chưa có bảng phân công và danh sách cặp chéo reviewer chi tiết, đang chờ Lead Face Landmark (@thangchudinh1) lên kế hoạch.
- Một số ảnh có góc chụp khuất (quay ngang đầu, mặc áo dày) gây khó khăn cho ước lượng, vẫn đang chờ thêm ý kiến Mentor ở mục P-017.

## Kế hoạch tuần sau (và phần còn lại của tuần)

- **Lead Face Landmark (@thangchudinh1)** chốt danh sách phân công job và người review chéo cho 4 thành viên còn lại.
- Toàn đội tập trung tổng lực sang gán nhãn 60 ảnh của bài toán Face Landmark (Task 2).
- Các thành viên tự học và áp dụng bám sát bản tóm tắt [Sổ tay gán nhãn Face Landmark](face-landmark-summary.md) vừa biên soạn.
- Nhóm sẽ push kết quả bài báo cáo này lên git đúng hạn vào tối cuối tuần.
