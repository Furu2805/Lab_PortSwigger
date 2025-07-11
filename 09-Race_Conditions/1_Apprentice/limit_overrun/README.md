# Write-up: Limit overrun race conditions

### Tổng quan
Khai thác lỗ hổng race condition trong chức năng áp mã giảm giá, gửi đồng thời nhiều yêu cầu POST để áp mã giảm giá nhiều lần, giảm giá sản phẩm `Lightweight "l33t" Leather Jacket` dưới 20$, và mua sản phẩm để hoàn thành lab.

### Mục tiêu
- Khai thác race condition để áp mã giảm giá nhiều lần, mua sản phẩm `Lightweight "l33t" Leather Jacket` với giá dưới 20$.

### Công cụ sử dụng
- Burp Suite Community
- Firefox Browser

### Quy trình khai thác
1. **Thu thập thông tin (Reconnaissance)**
- Đăng nhập với tài khoản `wiener`:`peter`:
    - Thêm sản phẩm `Lightweight "l33t" Leather Jacket` vào giỏ hàng
    - Áp mã giảm giá:
        **Phản hồi**: Mã giảm giá được áp thành công.
        ![post](./images/post.png)
    - Thử áp mã giảm giá lần thứ hai:
        **Phản hồi**: Server từ chối với thông báo mã đã được áp:
        ![already](./images/already.png)

- **Quan sát**: Hệ thống giới hạn số lần áp mã, gợi ý lỗ hổng race condition.

2. **Khai thác (Exploitation)**
- Trong Burp Repeater, tạo 100 yêu cầu `POST /cart/coupon HTTP/2` để áp mã giảm giá:

- Nhóm 100 yêu cầu, gỡ bỏ mã giảm giá đã áp qua giao diện `/cart`, sau đó chọn `Send group in parallel (single-packet attack)` để gửi đồng thời:
    ![race](./images/race.png)
    - **Phản hồi**: Một số yêu cầu được áp thành công, giảm giá sản phẩm dưới 20$
    ![prove](./images/prove.png)

    - **Giải thích**: Race condition xảy ra khi server xử lý đồng thời nhiều yêu cầu áp mã giảm giá trước khi kiểm tra giới hạn, dẫn đến áp mã nhiều lần.

- Mua sản phẩm và hoàn thành lab
    ![solved](./images/solved.png)

### Bài học rút ra
- Hiểu cách khai thác lỗ hổng race condition trong chức năng áp mã giảm giá bằng cách gửi nhiều yêu cầu song song
- Nhận thức tầm quan trọng của việc đồng bộ hóa xử lý yêu cầu để ngăn chặn vượt giới hạn logic nghiệp vụ

### Tài liệu tham khảo
- PortSwigger: Race Condition
- PortSwigger: Business logic vulnerabilities

### Kết luận
Lab này cung cấp kinh nghiệm thực tiễn trong việc khai thác lỗ hổng race condition, sử dụng Burp Repeater để gửi yêu cầu song song, vượt giới hạn áp mã giảm giá, và mua sản phẩm với giá thấp. Xem portfolio đầy đủ tại https://github.com/Furu2805/Lab_PortSwigger.

*Viết bởi Toàn Lương, Tháng 7/2025.*