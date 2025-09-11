# Web LLM Attacks Write-ups

Đây là nơi mình lưu lại các write-up về 4 lab Web LLM Attacks từ **PortSwigger Web Security Academy**. Mình đang làm từ cấp độ Apprentice (1 lab) đến Practitioner (2 lab) và Expert (1 lab), khám phá các kỹ thuật như exploiting LLM APIs, indirect injection, và insecure output handling.

### Tổng quan
- **Số lab**: 4 (Apprentice: 1, Practitioner: 2, Expert: 1).
- **Kỹ thuật chính**:
  - Exploiting LLM APIs with excessive agency.
  - Indirect prompt injection and vulnerabilities in LLM APIs.
  - Exploiting insecure output handling in LLMs.

### Cấu trúc thư mục
- `Apprentice/`: Các lab cơ bản (như exploit_excessive_agency).
- `Practitioner/`: Các lab nâng cao (như exploit_vulnerabilities, indirect_injection).
- `Expert/`: Các lab cao cấp (như insecure_output_handling).
- `images/`: Hình ảnh minh họa từ Burp Suite và Firefox.

### Kỹ năng nổi bật
- Khai thác lỗ hổng LLM (excessive agency, indirect injection).
- Sử dụng Burp Suite để phân tích API requests và phản hồi.
- Hiểu cách ứng dụng xử lý prompt và output của LLM.

### Phòng thủ Web LLM Attacks
- **Tách system prompt**: Không ghép nội dung user vào system instruction, phân biệt rõ "system prompt" và "user content".
- **Prompt templates**: Escape/encode user data trong prompt template hoặc cung cấp dữ liệu user như context read-only.
- **Kiểm tra output**: Validate output server-side, dùng whitelist cho API endpoints/params nếu LLM gọi API.
- **Giới hạn quyền**: Hạn chế scope của tools LLM dùng, tránh thao tác phá hủy, dùng service accounts giới hạn.
- **Giám sát & rate-limit**: Theo dõi hành vi bất thường, alert khi gọi endpoint nhạy cảm.
- **Lọc nội dung**: Thêm classifier để phát hiện injection patterns, xử lý (ignore/delete/call API).
- **Tách chuỗi**: Dùng sandboxed summarization cho dữ liệu user, chỉ trả về text, không cho thực thi lệnh.
- **Kiểm tra đối kháng**: Red-team prompts thường xuyên, thử indirect injection qua nội dung.

### Xem thêm
- Mỗi lab có file `README.md` với quy trình khai thác, bài học rút ra, và hình ảnh minh họa.
- Check portfolio của mình tại https://github.com/Furu2805/Lab_PortSwigger.

*Cập nhật: 08/09/2025*