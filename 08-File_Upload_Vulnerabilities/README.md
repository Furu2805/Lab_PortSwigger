# Access Control Vulnerabilities Write-ups
Đây là nơi mình lưu lại các write-up về 7 lab File Upload Vulnerabilities từ PortSwigger Web Security Academy. Mình đã hoàn thành 2 lab cấp độ Apprentice và đang làm 4 lab Practitioner cùng 1 lab Expert, khám phá các kỹ thuật như RCE qua web shell và bypass hạn chế upload.

### Tổng quan
- **Số lab**: 7 (Apprentice: 2, Practitioner: 4, Expert: 1).
- **Kỹ thuật chính**:
    - Remote code execution (RCE) qua web shell upload.
    - Bypass hạn chế (Content-Type, path traversal, extension blacklist, obfuscated extension).
    - RCE qua polyglot web shell và race condition.

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như rce_web_shell, web_shell_content_bypass).
- `Practitioner/`: Các lab nâng cao (như web_shell_path_traversal, rce_polyglot_shell).
- `Expert/`: Các lab cao cấp (như web_shell_race_condition).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng file upload (RCE, bypass Content-Type, path traversal).
- Sử dụng Burp Suite để phân tích và gửi payload.
- Hiểu cách ứng dụng xử lý file upload và kiểm tra đầu vào.

### Phòng chống OS Command Injection
- **Kiểm tra định dạng**: Xác thực loại file (MIME type) và phần mở rộng trên server.
- **Giới hạn upload**: Chỉ cho phép định dạng file an toàn, dùng whitelist thay blacklist.
- **Lưu trữ an toàn**: Lưu file upload trong thư mục riêng, không thực thi trực tiếp.
- **Ngăn race condition**: Sử dụng khóa file hoặc xử lý đồng bộ để tránh tấn công đa luồng.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 02/07/2025*