# Business Logic Vulnerabilities Write-ups
Đây là nơi mình lưu lại các write-up về 12 lab Business Logic Vulnerabilities từ PortSwigger Web Security Academy. Mình đang làm từ cấp độ Apprentice (4 lab), Practitioner (7 lab), đến Expert (1 lab), khám phá các kỹ thuật như logic flaws, authentication bypass, và email parsing discrepancies.

### Tổng quan
- **Số lab**: 12 (Apprentice: 4, Practitioner: 7, Expert: 1).
- **Kỹ thuật chính**:
    - Logic flaws (high-level, low-level, infinite money).
    - Authentication bypass (state machine, encryption oracle).
    - Inconsistent handling (security controls, exceptional input, email parsing).

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như excessive_trust_client_controls, flawed_business_rules).
- `Practitioner/`: Các lab nâng cao (như low_level_logic_flaw, auth_bypass_encryption_oracle).
- `Expert/`: Các lab cao cấp (như bypass_access_email_parsing).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng business logic (logic flaws, authentication bypass).
- Sử dụng Burp Suite để phân tích và gửi payload.
- Hiểu cách ứng dụng xử lý logic nghiệp vụ và kiểm tra đầu vào.

### Phòng chống OS Command Injection
- **Kiểm tra logic nghiệp vụ**: Rà soát kỹ logic để phát hiện lỗ hổng, đặc biệt trong workflow và state machine.
- **Xác thực phía server**: Không tin tưởng dữ liệu từ client, luôn kiểm tra lại trên server.
- **Cô lập endpoint**: Tách biệt các endpoint có chức năng khác nhau để tránh dual-use.
- **Xử lý ngoại lệ**: Đảm bảo ứng dụng xử lý đúng các đầu vào bất thường, tránh bypass.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 24/05/2025*