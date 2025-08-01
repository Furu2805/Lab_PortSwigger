# Cross-site Scripting Write-ups

Đây là nơi mình lưu lại các write-up về 30 lab Cross-site Scripting (XSS) từ PortSwigger Web Security Academy. Mình đang làm từ cấp độ Apprentice (9 lab) đến Practitioner (15 lab) và Expert (6 lab), khám phá các kỹ thuật như reflected, stored, DOM XSS, và bypass CSP.

### Tổng quan
- **Số lab**: 30 (Apprentice: 9, Practitioner: 15, Expert: 6).
- **Kỹ thuật chính**:
  - Reflected và stored XSS (HTML, attributes, JavaScript string).
  - DOM XSS (document.write, innerHTML, jQuery, AngularJS).
  - Bypass filters (encoded tags, SVG, template literal, CSP).

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như reflected_html_none, dom_jquery_hashchange).
- `Practitioner/`: Các lab nâng cao (như dom_select_search, xss_steal_cookies).
- `Expert/`: Các lab cao cấp (như angular_sandbox_csp, reflected_csp_bypass).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng XSS (reflected, stored, DOM, bypass filters).
- Sử dụng Burp Suite để gửi payload và kiểm tra phản hồi.
- Hiểu cách ứng dụng xử lý đầu vào và áp dụng CSP.

### Phòng chống SQLi
- **Lọc đầu vào**: Encode đặc biệt (HTML, JS) hoặc thoát ký tự nguy hiểm (, <, >, ', ", ).
- **Sử dụng CSP**: Áp dụng Content Security Policy để hạn chế thực thi script không an toàn.
- **Xác thực phía server**: Không tin tưởng dữ liệu từ client, kiểm tra và làm sạch trước khi render.
- **Vô hiệu hóa tính năng không cần thiết**: Tắt inline script hoặc eval nếu không sử dụng.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 30/07/2025*