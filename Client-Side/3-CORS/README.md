# Cross-origin Resource Sharing Write-ups

Đây là nơi mình lưu lại các write-up về 3 lab Cross-origin Resource Sharing (CORS) từ PortSwigger Web Security Academy. Mình đang làm từ cấp độ Apprentice (2 lab) đến Practitioner (1 lab), khám phá các kỹ thuật như origin reflection, trusted null origin, và insecure protocols.

### Tổng quan
- **Số lab**: 3 (Apprentice: 2, Practitioner: 1).
- **Kỹ thuật chính**:
  - CORS vulnerability with basic origin reflection.    
  - CORS with trusted null origin and insecure protocols.

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như basic_origin_reflection, trusted_null_origin).
- `Practitioner/`: Các lab nâng cao (như trusted_insecure_protocols).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng CORS (origin reflection, null origin).
- Sử dụng Burp Suite để kiểm tra header và gửi yêu cầu cross-origin.
- Hiểu cách ứng dụng cấu hình CORS và kiểm soát truy cập.

### Phòng chống SQLi
- **Cấu hình chính xác**: Chỉ định rõ origin trong Access-Control-Allow-Origin cho tài nguyên nhạy cảm.
- **Chỉ cho phép site tin cậy**: Xác thực origin trước khi phản ánh, tránh phản ánh động không kiểm tra.
- **Tránh whitelist null**: Không dùng Access-Control-Allow-Origin: null, định nghĩa rõ origin tin cậy.
- **Không dùng wildcard nội bộ**: Tránh wildcard trong mạng nội bộ, bổ sung bảo vệ bổ sung.
- **Kết hợp server-side**: Dùng authentication và session management thay vì chỉ dựa vào CORS.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 01/08/2025*