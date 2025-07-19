# SQL Injection Write-ups

Đây là nơi mình lưu lại các write-up về 14 lab Authentication từ **PortSwigger Web Security Academy**. Mình đã làm từ cấp độ Apprentice (3 lab) đến Practitioner (9 lab) và Expert (2 lab), khám phá các kỹ thuật như username enumeration, 2FA bypass, và brute-force attack.

### Tổng quan
- **Số lab**: 14 (Apprentice: 3, Practitioner: 9, Expert: 2).
- **Kỹ thuật chính**:
  - Username enumeration (qua phản hồi khác nhau, thời gian, khóa tài khoản).
  - 2FA bypass (lỗi logic, brute-force).
  - Brute-force attack (chống bảo vệ, cookie, thay đổi mật khẩu).
  - Password reset (lỗi logic, poisoning via middleware).

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như username enumeration, 2FA simple bypass).
- `Practitioner/`: Các lab nâng cao (như brute-force cookie, password reset poisoning).
- `Expert/`: Các lab cao cấp (như brute-force với nhiều thông tin đăng nhập).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng xác thực (username enumeration, 2FA bypass, brute-force).
- Sử dụng Burp Suite để phân tích và gửi payload.
- Hiểu logic ứng dụng và nhận thức bảo mật (kiểm tra xác thực).

### Phòng chống SQLi
- **Bảo vệ thông tin đăng nhập**: Sử dụng HTTPS, chuyển hướng HTTP sang HTTPS, và tránh lộ username/email qua hồ sơ hoặc phản hồi HTTP.
- **Không trông chờ vào người dùng**: Áp dụng chính sách mật khẩu mạnh (ví dụ: zxcvbn) hiển thị phản hồi tức thì để khuyến khích mật khẩu an toàn.
- **Ngăn liệt kê username**: Sử dụng thông báo lỗi giống nhau, đồng bộ mã HTTP và thời gian phản hồi.
- **Chống brute-force**: Giới hạn IP, ngăn giả mạo IP, thêm CAPTCHA khi vượt ngưỡng thử.
- **Kiểm tra logic xác minh**: Xem xét kỹ logic để loại bỏ lỗ hổng, tránh kiểm tra dễ bị qua mặt.
- **Chú ý chức năng phụ trợ**: Bảo vệ chức năng như đặt lại/thay đổi mật khẩu tương tự trang đăng nhập.
- **Áp dụng 2FA đúng cách**: Ưu tiên thiết bị/ứng dụng tạo mã, tránh dùng SMS/email, đảm bảo logic 2FA không bị bypass.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 19/05/2025*