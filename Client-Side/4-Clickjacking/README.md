# Clickjacking Write-ups

Đây là nơi mình lưu lại các write-up về 5 lab Clickjacking từ **PortSwigger Web Security Academy**. Mình đang làm từ cấp độ Apprentice (3 lab) đến Practitioner (2 lab), khám phá các kỹ thuật như basic clickjacking, frame buster bypass, và DOM-based XSS trigger.

### Tổng quan
- **Số lab**: 5 (Apprentice: 3, Practitioner: 2).
- **Kỹ thuật chính**:
  - Basic clickjacking (with CSRF token, form URL param, frame buster).
  - Exploiting clickjacking for DOM-based XSS and multistep attacks.

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như basic_csrf_token, frame_buster).
- `Practitioner/`: Các lab nâng cao (như dom_xss_trigger, multistep).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng clickjacking (frame buster bypass, DOM XSS).
- Sử dụng Burp Suite để kiểm tra iframe và gửi yêu cầu giả mạo.
- Hiểu cách ứng dụng quản lý frame và header bảo mật.

### Phòng thủ Clickjacking
- **Dùng X-Frame-Options**: Áp dụng `DENY`, `SAMEORIGIN`, hoặc `ALLOW-FROM` để hạn chế iframe (kiểm tra hỗ trợ trình duyệt).
- **Sử dụng CSP**: Thêm `frame-ancestors 'none'` hoặc `'self'` trong Content Security Policy.
- **Chiến lược đa lớp**: Kết hợp X-Frame-Options và CSP trong chiến lược bảo mật tổng thể.
- **Kiểm tra kỹ lưỡng**: Phát triển, triển khai, và kiểm tra CSP cẩn thận.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 02/08/2025*