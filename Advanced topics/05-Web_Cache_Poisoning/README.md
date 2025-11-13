# Web Cache Poisoning Write-ups

Đây là nơi mình lưu lại các write-up về 12 lab Web Cache Poisoning từ **PortSwigger Web Security Academy**. Mình đang làm từ cấp độ Practitioner (9 lab) đến Expert (3 lab), khám phá các kỹ thuật như poisoning với unkeyed headers, query strings, và combined vulnerabilities.

### Tổng quan
- **Số lab**: 13 (Practitioner: 9, Expert: 4).
- **Kỹ thuật chính**:
  - Web cache poisoning with unkeyed headers, cookies, and multiple headers.
  - Targeted poisoning, query string/param manipulation, and parameter cloaking.
  - Exploiting DOM vulnerabilities, cache key injection, and internal poisoning.

### Cấu trúc thư mục
- `Practitioner/`: Các lab nâng cao (như unkeyed_header, fat_get_request).
- `Expert/`: Các lab cao cấp (như dom_vulnerability_exploit, internal_cache_poisoning).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng web cache poisoning (unkeyed inputs, query manipulation).
- Sử dụng Burp Suite để phân tích cache behavior và gửi payload.
- Hiểu cách ứng dụng và CDN xử lý cache và header.

### Phòng thủ Web Cache Poisoning
- **Tắt caching nếu không cần**: Xem xét vô hiệu hóa caching nếu không thực sự cần thiết.
- **Giới hạn caching tĩnh**: Chỉ cache phản hồi tĩnh, kiểm tra kỹ để tránh thay thế bởi dữ liệu độc hại.
- **Đánh giá third-party**: Hiểu rõ rủi ro bảo mật từ công nghệ third-party trước khi tích hợp.
- **Tắt header không cần**: Vô hiệu hóa header không cần thiết để giảm rủi ro từ unkeyed inputs.
- **Rewrite request**: Nếu loại trừ khỏi cache key vì hiệu suất, rewrite request thay vì bỏ qua.
- **Chặn fat GET**: Không chấp nhận fat GET requests, kiểm tra mặc định từ third-party.
- **Sửa lỗi client-side**: Vá lỗ hổng client-side ngay cả khi tưởng không khai thác được.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 29/09/2025*