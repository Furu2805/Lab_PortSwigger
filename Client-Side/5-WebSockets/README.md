# WebSockets Write-ups

Đây là nơi mình lưu lại các write-up về 3 lab WebSockets từ PortSwigger Web Security Academy. Mình đang làm từ cấp độ Apprentice (1 lab) đến Practitioner (2 lab), khám phá các kỹ thuật như manipulating messages, cross-site hijacking, và handshake manipulation.

### Tổng quan
- **Số lab**: 3 (Apprentice: 1, Practitioner: 2).
- **Kỹ thuật chính**:
  - Manipulating WebSocket messages to exploit vulnerabilities.
  - Cross-site WebSocket hijacking.
  - Manipulating the WebSocket handshake.

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như manipulate_messages).
- `Practitioner/`: Các lab nâng cao (như cross_site_hijacking, handshake_manipulate).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng WebSocket (message manipulation, hijacking).
- Sử dụng Burp Suite để giám sát và gửi WebSocket messages.
- Hiểu cách ứng dụng xử lý WebSocket handshake và dữ liệu.

### Phòng thủ WebSocket
- **Sử dụng wss://**: Áp dụng WebSockets over TLS để mã hóa kết nối.
- **Hardcode URL**: Định nghĩa cố định endpoint WebSocket, tránh dùng dữ liệu người dùng.
- **Bảo vệ handshake**: Thêm CSRF token để ngăn cross-site hijacking.
- **Xử lý dữ liệu an toàn**: Đối xử dữ liệu WebSocket như không tin cậy, lọc và kiểm tra cả server và client.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 04/08/2025*