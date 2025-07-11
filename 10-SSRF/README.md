# Server-side Request Forgery Write-ups
Đây là nơi mình lưu lại các write-up về 7 lab Server-side Request Forgery (SSRF) từ PortSwigger Web Security Academy. Mình đã hoàn thành 2 lab cấp độ Apprentice và đang làm 3 lab Practitioner cùng 2 lab Expert, khám phá các kỹ thuật như basic SSRF, blind SSRF, và filter bypass.

### Tổng quan
- **Số lab**: 7 (Apprentice: 2, Practitioner: 3, Expert: 2).
- **Kỹ thuật chính**:
    - Basic SSRF (local server, back-end system).
    - Blind SSRF (out-of-band, Shellshock).
    - Filter bypass (blacklist, whitelist, open redirection).

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như basic_local_server, basic_backend_system).
- `Practitioner/`:  Các lab nâng cao (như blind_out_of_band, filter_bypass_redirect).
- `Expert/`: Các lab cao cấp (như blind_shellshock, whitelist_filter).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng SSRF (basic, blind, filter bypass).
- Sử dụng Burp Suite để gửi yêu cầu và kiểm tra phản hồi.
- Hiểu cách ứng dụng xử lý yêu cầu và lọc đầu vào.

### Phòng chống OS Command Injection
- **Kiểm tra đầu vào**: Lọc và xác thực URL, chặn truy cập nội bộ (localhost, 127.0.0.1).
- **Dùng whitelist**: Chỉ cho phép domain hoặc IP được định nghĩa trước.
- **Hạn chế quyền truy cập**: Cấu hình firewall hoặc proxy để ngăn SSRF đến các hệ thống nhạy cảm.
- **Tắt tính năng không cần thiết**: Vô hiệu hóa các endpoint hoặc API không sử dụng.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 11/07/2025*