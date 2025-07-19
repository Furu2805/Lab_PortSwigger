# Information Disclosure Write-ups
Đây là nơi mình lưu lại các write-up về 5 lab Information Disclosure từ PortSwigger Web Security Academy. Mình đang làm từ cấp độ Apprentice (4 lab) đến Practitioner (1 lab), khám phá các kỹ thuật như disclosure qua error messages, debug pages, backup files, và version control history.

### Tổng quan
- **Số lab**: 5 (Apprentice: 4, Practitioner: 1).
- **Kỹ thuật chính**:
    - Disclosure qua error messages và debug pages.
    - Source code leak qua backup files.
    - Authentication bypass qua information disclosure.
    - Disclosure trong version control history.

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như error_messages, debug_page).
- `Practitioner/`: Các lab nâng cao (như version_control_history).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng information disclosure (error messages, debug pages, version control).
- Sử dụng Burp Suite để phân tích và thu thập thông tin nhạy cảm.
- Hiểu cách ứng dụng xử lý dữ liệu và lộ thông tin nhạy cảm.

### Phòng chống OS Command Injection
- **Nâng cao nhận thức**: Đào tạo đội ngũ về thông tin nhạy cảm, tránh để lộ dữ liệu tưởng chừng vô hại nhưng có giá trị với attacker.
- **Kiểm tra mã nguồn**: Tích hợp kiểm tra disclosure vào quy trình QA, tự động hóa việc xóa comment của developer.
- **Dùng lỗi chung**: Sử dụng thông báo lỗi generic, tránh cung cấp manh mối về hành vi ứng dụng.
- **Tắt tính năng debug**: Đảm bảo mọi tính năng debug hoặc diagnostic bị tắt trên môi trường production.
- **Quản lý công nghệ bên thứ ba**: Hiểu rõ cấu hình và tắt các tính năng không cần thiết của công nghệ bên thứ ba.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 01/06/2025*