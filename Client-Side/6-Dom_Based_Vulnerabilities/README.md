# DOM-based Vulnerabilities Write-ups

Đây là nơi mình lưu lại các write-up về 7 lab DOM-based Vulnerabilities từ **PortSwigger Web Security Academy**. Mình đang làm từ cấp độ Practitioner (5 lab) đến Expert (2 lab), khám phá các kỹ thuật như DOM XSS, open redirection, cookie manipulation, và DOM clobbering.

### Tổng quan
- **Số lab**: 7 (Practitioner: 5, Expert: 2).
- **Kỹ thuật chính**:
  - DOM XSS using web messages (with JS URL, JSON.parse).
  - DOM-based open redirection and cookie manipulation.
  - Exploiting DOM clobbering to enable XSS and bypass HTML filters.

### Cấu trúc thư mục
- `Practitioner/`: Các lab nâng cao (như web_messages_xss, open_redirection).
- `Expert/`: Các lab cao cấp (như dom_clobbering_xss, bypass_html_filters).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng DOM-based (XSS, redirection, manipulation).
- Sử dụng Burp Suite để phân tích client-side code và payload.
- Hiểu cách ứng dụng xử lý DOM và lọc đầu vào.

### Phòng thủ DOM-based Vulnerabilities
- **Lọc đầu vào**: Kiểm tra và thoát dữ liệu trước khi sử dụng trong DOM (như `innerHTML`, `document.write`).
- **Tránh eval/dynamic code**: Không dùng `eval` hoặc thực thi mã động từ nguồn không tin cậy.
- **Sử dụng CSP**: Áp dụng Content Security Policy để hạn chế script và nguồn dữ liệu.
- **Xác thực phía server**: Kết hợp server-side validation để giảm phụ thuộc client-side.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 08/08/2025*