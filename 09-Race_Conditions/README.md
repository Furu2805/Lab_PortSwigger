# Access Control Vulnerabilities Write-ups
Đây là nơi mình lưu lại các write-up về 6 lab Race Conditions từ PortSwigger Web Security Academy. Mình đang làm từ cấp độ Apprentice (1 lab) đến Practitioner (4 lab) và Expert (1 lab), khám phá các kỹ thuật như limit overrun, rate limit bypass, và time-sensitive vulnerabilities.

### Tổng quan
- **Số lab**: 6 (Apprentice: 1, Practitioner: 4, Expert: 1).
- **Kỹ thuật chính**:
    - Limit overrun và bypass rate limits
    - Race conditions trên multi-endpoint, single-endpoint, và time-sensitive.
    - Partial construction race conditions.

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như limit_overrun).
- `Practitioner/`:  Các lab nâng cao (như bypass_rate_limits, time_sensitive).
- `Expert/`: Các lab cao cấp (như partial_construction).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng race conditions (limit overrun, multi-endpoint).
- Sử dụng Burp Suite để gửi yêu cầu đồng thời và kiểm tra trạng thái.
- Hiểu cách ứng dụng xử lý giao dịch và đồng bộ dữ liệu.

### Phòng chống OS Command Injection
- **Tránh trạng thái tạm thời**: Thiết kế mỗi request là đơn vị logic hoàn chỉnh, giảm phụ thuộc sub-states.
- **Thao tác nguyên tử**: Dùng transaction (BEGIN ... COMMIT) để đảm bảo thay đổi đồng bộ.
- **Ràng buộc dữ liệu**: Áp dụng unique constraints, foreign key, NOT NULL tại DB để giảm lỗi logic.
- **Không tin session**: Tránh dùng session để bảo vệ DB do delay hoặc ghi không đồng bộ.
- **Cẩn trọng ORM**: Kiểm tra framework ORM để tránh race do update không nhất quán.
- **Kiến trúc không trạng thái**: Sử dụng JWT mã hóa trạng thái client-side khi phù hợp, bảo vệ key tránh tấn công.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 06/07/2025*