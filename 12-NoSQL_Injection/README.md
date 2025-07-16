# XML External Entity Injection Write-ups
Đây là nơi mình lưu lại các write-up về 4 lab NoSQL Injection từ PortSwigger Web Security Academy. Mình đang làm từ cấp độ Apprentice (2 lab) đến Practitioner (2 lab), khám phá các kỹ thuật như detecting injection, bypass authentication, và extract data.

### Tổng quan
- **Số lab**: 4 (Apprentice: 2, Practitioner: 2).
- **Kỹ thuật chính**:
    - Detecting NoSQL injection.
    - Exploiting operator injection (bypass authentication, extract unknown fields).
    - Extracting data via NoSQL injection.

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như detect_injection, bypass_auth).
- `Practitioner/`: Các lab nâng cao (như extract_data, extract_unknown_fields).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng NoSQL injection (detecting, operator injection).
- Sử dụng Burp Suite để gửi payload và phân tích phản hồi.
- Hiểu cách ứng dụng xử lý query NoSQL và lọc đầu vào.

### Phòng chống OS Command Injection
- **Xác thực đầu vào**: Sử dụng allowlist để lọc ký tự chấp nhận từ người dùng.
- **Sử dụng parameterized query**: Chèn đầu vào người dùng qua parameterized queries thay vì nối trực tiếp.
- **Kiểm soát key**: Áp dụng allowlist cho các key chấp nhận để ngăn operator injection.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 16/07/2025*