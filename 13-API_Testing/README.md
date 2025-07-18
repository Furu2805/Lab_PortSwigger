# API Testing Write-ups
Đây là nơi mình lưu lại các write-up về 5 lab API Testing từ PortSwigger Web Security Academy. Mình đã hoàn thành 1 lab cấp độ Apprentice và 3 lab Practitioner, đang làm 1 lab Expert, khám phá các kỹ thuật như parameter pollution, mass assignment, và unused endpoints.

### Tổng quan
- **Số lab**: 5 (Apprentice: 1, Practitioner: 3, Expert: 1).
- **Kỹ thuật chính**:
    - Exploiting API endpoints using documentation.
    - Server-side parameter pollution (query string, REST URL).
    - Finding unused endpoints and mass assignment vulnerabilities.

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như exploit_doc_endpoint).
- `Practitioner/`: Các lab nâng cao (như ssp_query_string, mass_assignment).
- `Expert/`: Các lab cao cấp (như ssp_rest_url).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng API (parameter pollution, mass assignment).
- Sử dụng Burp Suite để phân tích endpoint và gửi payload.
- Hiểu cách API xử lý tham số và kiểm soát quyền truy cập.

### Phòng chống OS Command Injection
- **Bảo vệ tài liệu**: Mã hóa hoặc hạn chế truy cập tài liệu API nếu không công khai.
- **Cập nhật tài liệu**: Giữ tài liệu luôn mới để tester hiểu rõ bề mặt tấn công.
- **Giới hạn phương thức**: Áp dụng allowlist cho HTTP methods được phép.
- **Kiểm tra content type**: Xác thực content type cho mỗi request/response.
- **Dùng lỗi chung**: Sử dụng generic error messages để tránh lộ thông tin.
- **Bảo vệ mọi phiên bản**: Áp dụng biện pháp bảo mật cho tất cả phiên bản API.
- **Ngăn mass assignment**: Dùng allowlist cho thuộc tính cập nhật, blocklist thuộc tính nhạy cảm.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 18/07/2025*