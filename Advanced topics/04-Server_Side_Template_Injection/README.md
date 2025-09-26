# Server-side Template Injection Write-ups

Đây là nơi mình lưu lại các write-up về 7 lab Server-side Template Injection từ **PortSwigger Web Security Academy**. Mình đang làm từ cấp độ Practitioner (5 lab) đến Expert (2 lab), khám phá các kỹ thuật như basic injection, code context, và custom exploits.

### Tổng quan

- **Số lab**: 7 (Practitioner: 5, Expert: 2).
- **Kỹ thuật chính**:
  - Basic server-side template injection (code context, documentation-based).
  - Injection with information disclosure and unknown language exploits.
  - Sandboxed environment and custom exploit injection.

### Cấu trúc thư mục

- `Practitioner/`: Các lab nâng cao (như basic_injection, info_disclosure_objects).
- `Expert/`: Các lab cao cấp (như sandboxed_injection, custom_exploit_injection).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật

- Khai thác lỗ hổng SSTI (basic, code context, custom exploits).
- Sử dụng Burp Suite để phân tích template và gửi payload.
- Hiểu cách ứng dụng xử lý template và sandboxing.

### Phòng thủ Server-side Template Injection

- **Tránh chỉnh sửa template**: Không cho phép người dùng sửa hoặc gửi template mới nếu không cần thiết.
- **Dùng engine không logic**: Sử dụng template engine "logic-less" (như Mustache) để giảm rủi ro.
- **Chạy trong sandbox**: Thực thi mã người dùng trong môi trường sandbox, loại bỏ module/function nguy hiểm.
- **Dùng container**: Triển khai template trong Docker container khóa chặt để sandboxing bổ sung.
- **Tách logic & hiển thị**: Phân tách logic và presentation càng nhiều càng tốt.

### Xem thêm

- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 23/09/2025*