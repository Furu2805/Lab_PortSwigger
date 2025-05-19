# File Path Traversal Write-ups

Đây là nơi mình lưu lại các write-up về 6 lab File Path Traversal từ PortSwigger Web Security Academy. Mình đã hoàn thành từ cấp độ Apprentice (1 lab) đến Practitioner (5 lab), khám phá các kỹ thuật khai thác lỗ hổng path traversal như traversal sequences, mã hóa URL, null byte, và bypass kiểm tra prefix hoặc đuôi tệp.

### Tổng quan
- **Số lab**: 6 (Apprentice: 1, Practitioner: 5).
- **Kỹ thuật chính**:
  - Traversal sequences (`../`) để truy cập tệp ngoài thư mục dự kiến.
  - Bypass cơ chế chặn bằng đường dẫn tuyệt đối và chuỗi lồng ghép (`..././`)..
  - Mã hóa URL hai lần để vượt qua lọc và URL-decode.
  - Null byte (`%00`) để bypass kiểm tra đuôi tệp.
  - Giữ prefix hợp lệ để qua mặt kiểm tra đường dẫn.

### Cấu trúc thư mục
- `Apprentice/`: Lab cơ bản (File path traversal, simple case).
- `Practitioner/`: Các lab nâng cao (Absolute Path Bypass, Stripped Non-Recursively, Superfluous URL-Decode, Validation of Start of Path, Null Byte Bypass).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng file path traversal với các kỹ thuật như traversal sequences, mã hóa, null byte, và prefix bypass.
- Sử dụng Burp Suite để phân tích yêu cầu HTTP, thử nghiệm trong Repeater, và xây dựng payload.
- Hiểu cơ chế lọc đường dẫn và phát triển tư duy vượt qua các kiểm tra bảo mật.

### Phòng chống File Path Traversal
- **Tránh sử dụng input người dùng**: Không truyền trực tiếp input người dùng vào filesystem APIs; thay bằng cách xử lý an toàn hơn.
- **Kiểm tra input**: Sử dụng danh sách trắng cho các giá trị hợp lệ hoặc chỉ cho phép ký tự chữ và số.
- **Canonicalize đường dẫn**: Nối input với thư mục cơ sở, sử dụng API chuẩn hóa đường dẫn, và xác minh đường dẫn bắt đầu bằng thư mục dự kiến. Ví dụ (Java):
    ```
    File file = new File(BASE_DIRECTORY, userInput);
    if (file.getCanonicalPath().startsWith(BASE_DIRECTORY)) {
        // process file
    }
    ```
- **Hạn chế quyền truy cập**: Chạy ứng dụng với quyền tối thiểu để ngăn truy cập tệp hệ thống nhạy cảm.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 19/05/2025*