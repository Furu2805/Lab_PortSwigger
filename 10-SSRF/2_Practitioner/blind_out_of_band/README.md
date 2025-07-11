# Write-up: Blind SSRF with out-of-band detection

### Tổng quan
Khai thác lỗ hổng Blind Server-Side Request Forgery (SSRF) trong phần mềm phân tích của trang web, sử dụng header Referer để gửi yêu cầu tới Burp Collaborator, xác nhận tương tác qua out-of-band detection, và hoàn thành lab.

### Mục tiêu
- Sử dụng chức năng tải trang sản phẩm để kích hoạt yêu cầu HTTP tới public Burp Collaborator server qua header `Referer`.

### Công cụ sử dụng
- Burp Suite Community
- Firefox Browser

### Quy trình khai thác
1. **Thu thập thông tin (Reconnaissance)**
- Truy cập trang sản phẩm bất kỳ và kiểm tra yêu cầu trong Burp Suite Proxy:
    - **Quan sát**: Trang sản phẩm tải dữ liệu và gửi header Referer tới hệ thống phân tích, gợi ý khả năng tồn tại lỗ hổng Blind SSRF:

2. **Khai thác (Exploitation)**
- Gửi yêu cầu `GET /product?productId=1` tới Burp Repeater.
- Tạo domain trong Burp Collaborator
- Thay đổi header `Referer: http://xyz123.burpcollaborator.net` trong Burp Repeater:
    ![referer](./images/1_referer.png)
- Gửi yêu cầu và kiểm tra Burp Collaborator:
    - **Phản hồi**: Burp Collaborator ghi nhận tương tác HTTP từ server của lab:
        ![out](./images/2_out_of_band.png)

    - **Giải thích**: Hệ thống phân tích của server gửi yêu cầu tới URL trong header `Referer`, xác nhận lỗ hổng Blind SSRF qua out-of-band detection.

- Hoàn thành lab:
    ![sovled](./images/3_solved.png)

### Bài học rút ra
- Hiểu cách khai thác lỗ hổng Blind SSRF bằng cách sử dụng header Referer để kích hoạt yêu cầu tới server bên ngoài và xác nhận qua out-of-band detection.
- Nhận thức tầm quan trọng của việc lọc và kiểm tra các header HTTP như Referer để ngăn chặn SSRF trong hệ thống phân tích.

### Tài liệu tham khảo
- PortSwigger: Server-Side Request Forgery (SSRF)
- PortSwigger: Blind SSRF vulnerabilities

### Kết luận
Lab này cung cấp kinh nghiệm thực tiễn trong việc khai thác lỗ hổng Blind SSRF, sử dụng Burp Collaborator để phát hiện tương tác out-of-band, và kích hoạt yêu cầu tới server bên ngoài. Xem portfolio đầy đủ tại https://github.com/Furu2805/Lab_PortSwigger.

*Viết bởi Toàn Lương, Tháng 7/2025.*