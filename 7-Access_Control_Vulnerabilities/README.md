# Access Control Vulnerabilities Write-ups
Đây là nơi mình lưu lại các write-up về 13 lab Access Control Vulnerabilities từ PortSwigger Web Security Academy. Mình đã hoàn thành 5 lab cấp độ Apprentice và đang làm 4 lab Practitioner, khám phá các kỹ thuật như unprotected admin, user role manipulation, và insecure direct references.

### Tổng quan
- **Số lab**: 13 (Apprentice: 9, Practitioner: 4).
- **Kỹ thuật chính**:
    - Unprotected admin functionality (URL unpredictable).
    - User role/ID control (request param, profile, redirect leak, password disclosure).
    - Insecure direct object references.
    - Access control bypass (URL, method, multi-step, referer-based).

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như unprotected_admin, user_id_password_disclosure).
- `Practitioner/`: Các lab nâng cao (như url_access_circumvent, referer_based_control).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng access control (unprotected admin, role manipulation).
- Sử dụng Burp Suite để thay đổi tham số và kiểm tra quyền truy cập.
- Hiểu cách ứng dụng quản lý quyền và kiểm tra đầu vào.

### Phòng chống OS Command Injection
- **Áp dụng RBAC**: Sử dụng Role-Based Access Control để kiểm soát quyền truy cập chặt chẽ.
- **Xác thực phía server**: Kiểm tra quyền trên server, không tin tưởng client-side controls.
- **Ẩn endpoint nhạy cảm**: Tránh dùng URL dễ đoán cho admin hoặc chức năng quan trọng.
- **Kiểm tra multi-step**: Đảm bảo mọi bước trong quy trình đều có kiểm soát truy cập.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 27/06/2025*