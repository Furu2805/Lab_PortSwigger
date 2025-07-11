# Write-up: Bypassing rate limits via race conditions

### Tổng quan
Khai thác lỗ hổng race condition trong cơ chế giới hạn đăng nhập (rate limit), bypass giới hạn 3 lần đăng nhập sai bằng cách gửi nhiều yêu cầu đồng thời qua Turbo Intruder, brute-force mật khẩu của `carlos`, đăng nhập, truy cập trang admin, và xóa tài khoản `carlos` để hoàn thành lab.

### Mục tiêu
- Bypass giới hạn đăng nhập, brute-force mật khẩu của `carlos`, đăng nhập, truy cập trang admin, và xóa tài khoản `carlos`.

### Công cụ sử dụng
- Burp Suite Community
- Firefox Browser

### Quy trình khai thác
1. **Thu thập thông tin (Reconnaissance)**
- Thử đăng nhập với tài khoản `carlos` và mật khẩu sai
    - **Phản hồi**: Đăng nhập thất bại. Sau 3 lần sai, tài khoản bị khóa tạm thời:
        ![login](./images/3rd_login.png)

- Trong Burp Repeater, gửi 20 yêu cầu đăng nhập sai đồng thời:
    - Chọn `Send group in parallel (single-packet attack)`
    - **Phản hồi**: Server xử lý nhiều yêu cầu mà không kích hoạt giới hạn, xác nhận lỗ hổng race condition:
        ![collusion](./images/collusion.png)

2. **Khai thác (Exploitation)**
- Sử dụng Turbo Intruder để brute-force mật khẩu của carlos với danh sách mật khẩu cung cấp. Cấu hình script Turbo Intruder:
    ![race](./race.py)
    - Gửi yêu cầu `POST /login` với danh sách mật khẩu, sử dụng chế độ song song:
        ![turbo](./images/turbo.png)
    - **Phản hồi**: Tìm thấy mật khẩu đúng baseball:
        ![pass](./images/password.png)
    
    - **Giải thích**: Race condition cho phép gửi nhiều yêu cầu đăng nhập đồng thời, bypass giới hạn 3 lần sai, giúp brute-force mật khẩu thành công.

- Đăng nhập với `carlos`:`baseball`:
    - Truy cập vào trang admin panel, xóa tài khoản carlos và hoàn thành lab
        ![solved](./images/solved.png)

### Bài học rút ra
- Hiểu cách khai thác lỗ hổng race condition qua nhiều endpoint để thao túng logic nghiệp vụ, dẫn đến mua sản phẩm với giá không mong muốn.
- Nhận thức tầm quan trọng của việc đồng bộ hóa xử lý yêu cầu giữa các endpoint (thêm sản phẩm, thanh toán) để ngăn chặn race condition.

### Tài liệu tham khảo
- PortSwigger: Race Condition
- PortSwigger: Business logic vulnerabilities

### Kết luận
Lab này cung cấp kinh nghiệm thực tiễn trong việc khai thác lỗ hổng race condition, sử dụng Turbo Intruder để brute-force mật khẩu, bypass giới hạn đăng nhập, và thực hiện hành động quản trị (xóa tài khoản). Xem portfolio đầy đủ tại https://github.com/Furu2805/Lab_PortSwigger.

*Viết bởi Toàn Lương, Tháng 7/2025.*