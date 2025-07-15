# XML External Entity Injection Write-ups
Đây là nơi mình lưu lại các write-up về 9 lab XML External Entity (XXE) Injection từ PortSwigger Web Security Academy. Mình đang làm từ cấp độ Apprentice (2 lab) đến Practitioner (6 lab) và Expert (1 lab), khám phá các kỹ thuật như external entities, blind XXE, và XInclude.

### Tổng quan
- **Số lab**: 9 (Apprentice: 2, Practitioner: 6, Expert: 1).
- **Kỹ thuật chính**:
    - Exploiting XXE (external entities, SSRF, XInclude).
    - Blind XXE (out-of-band, parameter entities, error messages, malicious DTD).
    - XXE via image upload và repurposing local DTD.

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như external_entities_files, xxe_ssrf_attacks).
- `Practitioner/`: Các lab nâng cao (như blind_out_of_band, xxe_image_upload).
- `Expert/`: Các lab cao cấp (như repurpose_local_dtd).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng XXE (external entities, blind, XInclude).
- Sử dụng Burp Suite để gửi payload XML và phân tích phản hồi.
- Hiểu cách ứng dụng xử lý XML và lọc đầu vào.

### Phòng chống OS Command Injection
- **Vô hiệu hóa tính năng nguy hiểm**: Tắt resolution của external entities và hỗ trợ XInclude trong thư viện XML parsing.
- **Cấu hình an toàn**: Điều chỉnh cài đặt hoặc override hành vi mặc định theo tài liệu thư viện.
- **Kiểm tra kỹ lưỡng**: Đảm bảo không để lại tính năng không cần thiết trong môi trường production.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 14/07/2025*