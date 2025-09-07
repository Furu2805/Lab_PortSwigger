# Insecure Deserialization Write-ups

Đây là nơi mình lưu lại các write-up về 10 lab Insecure Deserialization từ **PortSwigger Web Security Academy**. Mình đang làm từ cấp độ Apprentice (1 lab) đến Practitioner (6 lab) và Expert (3 lab), khám phá các kỹ thuật như modifying objects, PHP/Java deserialization, và custom gadget chains.

### Tổng quan
- **Số lab**: 10 (Apprentice: 1, Practitioner: 6, Expert: 3).
- **Kỹ thuật chính**:
  - Modifying serialized objects and data types.
  - Exploiting deserialization (PHP, Java, Ruby) with gadget chains.
  - Developing custom gadget chains and PHAR deserialization.

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như modify_objects).
- `Practitioner/`: Các lab nâng cao (như php_object_injection, ruby_gadget_chain).
- `Expert/`: Các lab cao cấp (như java_custom_gadget, phar_deserialization).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng deserialization (object injection, gadget chains).
- Sử dụng Burp Suite để phân tích payload và phản hồi.
- Hiểu cách ứng dụng xử lý serialization và lọc dữ liệu.

### Phòng thủ Insecure Deserialization
- **Tránh deserialization**: Không deserialization dữ liệu người dùng nếu không cần thiết.
- **Dùng digital signature**: Kiểm tra tính toàn vẹn trước khi deserialization.
- **Kiểm tra kiểu dữ liệu**: Chỉ cho phép class mong đợi, loại bỏ dữ liệu không mong muốn.
- **Chuyển sang định dạng an toàn**: Sử dụng JSON thay vì native serialization.
- **Chạy trong sandbox**: Thực hiện deserialization trong môi trường tách biệt.
- **Giám sát bất thường**: Theo dõi bộ nhớ và CPU trong quá trình deserialization.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 05/09/2025*