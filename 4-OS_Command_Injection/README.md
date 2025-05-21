# OS Command Injection Write-ups
Đây là nơi mình lưu lại các write-up về 5 lab OS Command Injection từ PortSwigger Web Security Academy. Mình đã hoàn thành cấp độ Apprentice (1 lab) và đang làm các lab Practitioner (4 lab), khám phá các kỹ thuật như command injection cơ bản và blind injection với thời gian, redirect, và exfiltration.

### Tổng quan
- **Số lab**: 5 (Apprentice: 1, Practitioner: 4).
- **Kỹ thuật chính**:
    - OS command injection cơ bản (truy cập lệnh đơn giản).
    - Blind OS command injection (thời gian, redirect output, out-of-band, data exfiltration).

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như simple_case).
- `Practitioner/`: Các lab nâng cao (như blind_time_delays, blind_data_exfil).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng OS command injection (cơ bản, blind với thời gian và out-of-band).
- Sử dụng Burp Suite để phân tích và gửi payload.
- Hiểu cách ứng dụng xử lý lệnh hệ thống và kiểm tra đầu vào.

### Phòng chống OS Command Injection
- **Kiểm tra đầu vào**: Lọc và xác thực mọi đầu vào để chặn các lệnh độc hại.
- **Sử dụng whitelist**: Chỉ cho phép các lệnh hoặc tham số được định nghĩa trước.
- **Chạy với quyền thấp**: Thực thi ứng dụng ở chế độ least privilege để giảm thiệt hại.
- **Tránh thực thi trực tiếp**: Sử dụng API hệ thống thay vì shell command (như `exec()`).

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 21/05/2025*