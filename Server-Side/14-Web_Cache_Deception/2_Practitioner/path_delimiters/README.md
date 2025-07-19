# Write-up: Exploiting path delimiters for web cache deception

### Tổng quan
Khai thác lỗ hổng web cache deception bằng cách sử dụng ký tự phân cách đường dẫn `;` để lừa hệ thống cache lưu trữ trang `/my-account` của tài khoản `carlos`, lấy API key của `carlos`, và submit key để hoàn thành lab.

### Mục tiêu 
- Khai thác web cache deception thông qua ký tự phân cách `;` để lấy API key của tài khoản `carlos` và submit key để hoàn thành lab.

### Công cụ sử dụng
- Burp Suite Community
- Firefox Browser
- Exploit Server (PortSwigger)

### Quy trình khai thác
1. **Thu thập thông tin (Reconnaissance)**
- Đăng nhập tài khoản `wiener`:`peter`, quan sát yêu cầu:
    `GET /my-account`
    - Thử thêm phần mở rộng đường dẫn:
        `GET /my-account/abc`
        - **Phản hồi**: `404 Not Found`, cho thấy ký tự `/` không khả thi để thao túng cache:
        ![not](./images/1_not-found.png)

- Dò ký tự đặc biệt bằng Burp Intruder:
    `GET /my-account§§abc.js`
    - **Kết quả**: Ký tự `;` và `?` được server chấp nhận:
        ![delimiter](./images/2_delimiter.png)

- Kiểm tra cache với ký tự `;`:
    `GET /my-account;abc.js`
    - Lần 1: **Phản hồi**: `X-Cache: miss`, nội dung chưa được cache.
        ![mis](./images/4_miss.png)
    - Lần 2: **Phản hồi**: `X-Cache: hit`, xác nhận hệ thống cache lưu trữ nội dung /my-account;abc.js
        ![hit](./images/5_hit.png)
    - **Quan sát**: Hệ thống cache xử lý `/my-account;abc.js` như file tĩnh, lưu trữ nội dung trang `/my-account`, gợi ý khả năng web cache deception.

2. **Khai thác (Exploitation)**
- Sử dụng Exploit Server để lừa nạn nhân (carlos) truy cập URL:
    ```javascript
    <script>document.location="https://lab-id.web-security-academy.net/my-account;abc.js"</script> 
    ```
    - Lưu payload vào body của Exploit Server và gửi tới nạn nhân qua chức năng "Deliver exploit to victim":
        ![body](./images/3_body.png)

- Kiểm tra cache để lấy nội dung trang `/my-account` của `carlos`:
    `GET /my-account;abc.js`
    - `Phản hồi`: `X-Cache: hit`, trả về trang `/my-account` của `carlos`, chứa API key `bBHPLaaDPXqqz7cGtUPWqnAhyblRQmQA`:
        ![api](./images/6_api.png)

- Submit API key `bBHPLaaDPXqqz7cGtUPWqnAhyblRQmQA` qua chức năng submit của lab
    - **Phản hồi**: Lab hoàn thành:
        ![solved](./images/7_solved.png)
        
- Giải thích: Lỗ hổng web cache deception xảy ra do hệ thống cache sai lầm lưu trữ trang `/my-account` như file tĩnh khi thêm `;abc.js`, cho phép truy xuất API key của carlos mà không cần xác thực.

### Bài học rút ra
- Hiểu cách khai thác lỗ hổng web cache deception bằng cách sử dụng ký tự phân cách ; để lừa hệ thống cache lưu trữ trang nhạy cảm.
- Nhận thức tầm quan trọng của việc kiểm tra và làm sạch ký tự phân cách trong URL để ngăn chặn web cache deception.

### Tài liệu tham khảo
- PortSwigger: Web Cache Deception

### Kết luận
Lab này cung cấp kinh nghiệm thực tiễn trong việc khai thác web cache deception thông qua ký tự phân cách ; để lấy API key của người dùng, và hiểu cách bảo vệ hệ thống cache khỏi các cuộc tấn công tương tự. Xem portfolio đầy đủ tại https://github.com/Furu2805/Lab_PortSwigger.

*Viết bởi Toàn Lương, Tháng 7/2025.*