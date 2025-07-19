
# Web Cache Deception Write-ups
Đây là nơi mình lưu lại các write-up về 5 lab Web Cache Deception từ PortSwigger Web Security Academy. Mình đang làm từ cấp độ Apprentice (1 lab) đến Practitioner (3 lab) và Expert (1 lab), khám phá các kỹ thuật như path mapping, normalization, và exact-match rules.
### Tổng quan
- **Số lab**: 5 (Apprentice: 1, Practitioner: 3, Expert: 1).
- **Kỹ thuật chính**:
    - Exploiting path mapping, delimiters, and normalization (origin/cache server).
    - Exploiting exact-match cache rules for web cache deception.

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như path_mapping).
- `Practitioner/`: Các lab nâng cao (như path_delimiters, cache_server_norm).
- `Expert/`: Các lab cao cấp (như exact_match_rules).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng web cache deception (path mapping, normalization).
- Sử dụng Burp Suite để kiểm tra cache và gửi yêu cầu giả mạo.
- Hiểu cách server và CDN xử lý cache và URL.

### Phòng chống OS Command Injection
- **Dùng Cache-Control**: Đánh dấu tài nguyên động với no-store và private.
- **Cấu hình CDN**: Đảm bảo quy tắc cache không ghi đè Cache-Control header.
- **Kích hoạt bảo vệ CDN**: Sử dụng tính năng như Cache Deception Armor (Cloudflare) để kiểm tra Content-Type khớp với phần mở rộng URL.
- **Đồng nhất URL**: Kiểm tra không có sự khác biệt giữa cách origin server và cache giải thích đường dẫn.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 19/07/2025*