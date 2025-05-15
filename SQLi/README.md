# SQL Injection Write-ups

Đây là nơi mình lưu lại các write-up về 18 lab SQL Injection từ **PortSwigger Web Security Academy**. Mình đã làm từ cấp độ Apprentice (2 lab) đến Practitioner (16 lab), khám phá đủ thứ như UNION attack, blind SQLi, và bypass login.

### Tổng quan
- **Số lab**: 18 (Apprentice: 5, Practitioner: 13).
- **Kỹ thuật chính**:
  - SQLi cơ bản (WHERE clause, login bypass).
  - UNION attack (đếm cột, tìm cột text, trích dữ liệu đa cột).
  - Blind SQLi (phản hồi điều kiện, lỗi, delay, out-of-band).
  - Error-based SQLi và bypass filter (XML encoding).

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như WHERE clause, login bypass).
- `Practitioner/`: Các lab nâng cao (như UNION attack, blind SQLi).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác SQLi (UNION, blind, error-based, out-of-band).
- Dùng Burp Suite để phân tích và gửi payload.
- Hiểu DBMS (Oracle, MySQL, Microsoft) và nhận thức bảo mật (kiểm tra đầu vào).

### Phòng chống SQLi
- Dùng **prepared statements** hoặc parameterized queries để tránh injection.
- Kiểm tra kỹ đầu vào (sanitize input) trước khi đưa vào SQL.
- Giới hạn quyền truy cập database, chỉ cho phép những gì cần thiết.
- Chạy ứng dụng ở chế độ least privilege để giảm thiệt hại.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 15/05/2025*