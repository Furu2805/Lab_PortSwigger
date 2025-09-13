# GraphQL API Vulnerabilities Write-ups

Đây là nơi mình lưu lại các write-up về 5 lab GraphQL API Vulnerabilities từ **PortSwigger Web Security Academy**. Mình đang làm từ cấp độ Apprentice (1 lab) đến Practitioner (4 lab), khám phá các kỹ thuật như accessing private posts, bypassing brute force, và CSRF exploits.

### Tổng quan
- **Số lab**: 5 (Apprentice: 1, Practitioner: 4).
- **Kỹ thuật chính**:
  - Accessing private GraphQL posts.
  - Accidental exposure of private fields, finding hidden endpoints.
  - Bypassing brute force protections and performing CSRF exploits.

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như access_private_posts).
- `Practitioner/`: Các lab nâng cao (như expose_private_fields, csrf_exploits).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng GraphQL (private fields, brute force bypass).
- Sử dụng Burp Suite để phân tích GraphQL queries và CSRF attacks.
- Hiểu cách ứng dụng cấu hình GraphQL và bảo vệ API.

### Phòng thủ GraphQL API Vulnerabilities
- **Tắt introspection**: Vô hiệu hóa introspection nếu API không công khai, giảm rủi ro lộ thông tin (xem blog Apollo).
- **Xem xét schema**: Kiểm tra schema để tránh lộ trường không mong muốn nếu giữ introspection.
- **Tắt suggestions**: Vô hiệu hóa suggestions để ngăn công cụ như Clairvoyance (xem thread GitHub).
- **Ẩn dữ liệu nhạy cảm**: Đảm bảo schema không lộ trường riêng tư (email, user ID).

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 12/09/2025*