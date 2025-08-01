# Cross-site Request Forgery Write-ups

Đây là nơi mình lưu lại các write-up về 12 lab Cross-site Request Forgery (CSRF) từ PortSwigger Web Security Academy. Mình đang làm từ cấp độ Apprentice (1 lab) đến Practitioner (11 lab), khám phá các kỹ thuật như token validation, SameSite bypass, và Referer validation.

### Tổng quan
- **Số lab**: 12 (Apprentice: 1, Practitioner: 11).
- **Kỹ thuật chính**:
  - CSRF with no defenses and broken token/session validation.
  - SameSite Lax/Strict bypass (method override, redirect, sibling domain, cookie refresh).
  - Referer-based validation weaknesses.

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như no_defense).
- `Practitioner/`: Các lab nâng cao (như token_method, samesite_strict_sibling).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng CSRF (token validation, SameSite bypass).
- Sử dụng Burp Suite để tạo và gửi yêu cầu giả mạo.
- Hiểu cách ứng dụng xử lý token, cookie, và header.

### Phòng chống SQLi
- **Sử dụng CSRF token**: Tạo token với entropy cao, gắn với session, và kiểm tra nghiêm ngặt trước mọi hành động.
- **Truyền token an toàn**: Đặt token trong hidden field của form POST, tránh URL query string hoặc cookie.
- **Áp dụng SameSite Strict**: Sử dụng SameSite Strict cho cookie, hạ xuống Lax chỉ khi cần, tránh SameSite=None.
- **Ngăn tấn công cùng site**: Cô lập nội dung không an toàn (như file upload) trên domain riêng biệt.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 01/08/2025*