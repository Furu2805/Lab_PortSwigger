# Write-up: Multi-endpoint race conditions

### Tổng quan
Khai thác lỗ hổng race condition trong quy trình mua hàng bằng cách gửi đồng thời các yêu cầu qua nhiều endpoint, thao túng giỏ hàng để thêm `Lightweight "l33t" Leather Jacket` với giá không mong muốn (ví dụ: giá của gift card), và hoàn thành thanh toán để giải lab.

### Mục tiêu
- Khai thác race condition qua nhiều endpoint để mua `Lightweight "l33t" Leather Jacket` với giá thấp hơn dự kiến.

### Công cụ sử dụng
- Burp Suite Community
- Firefox Browser

### Quy trình khai thác
1. **Thu thập thông tin (Reconnaissance)**
- Đăng nhập với tài khoản `wiener`:`peter`:
- Thử thanh toán một sản phẩm bất kỳ (gift card) qua `/cart/checkout`:
    - **Quan sát**: Trong Burp Suite Proxy, quá trình thanh toán mất một khoảng thời gian ngắn, gợi ý khả năng tồn tại lỗ hổng race condition
    ![check](./images/check_out.png)

2. **Khai thác (Exploitation)**
- Chuẩn bị các yêu cầu trong Burp Repeater:
    - Yêu cầu 3: Thêm gift card vào giỏ hàng
        ![gift](./images/gift_card.png)
    - Yêu cầu 1: Thanh toán đơn hàng:
        ![checkk](./images/check_out.png)
    - Yêu cầu 2: Thêm `Lightweight "l33t" Leather Jacket` vào giỏ hàng:
        ![leather](./images/leather.png)

- Trong Burp Repeater:
    - Gửi Yêu cầu 3 (thêm gift card) trước để đảm bảo giỏ hàng chứa gift card.
    - Nhóm Yêu cầu 1 và Yêu cầu 2, chọn `Send group in parallel (single-packet attack)` để gửi đồng thời:
    - **Phản hồi**: Lightweight "l33t" Leather Jacket được thêm vào giỏ hàng và thanh toán với giá của gift card (ví dụ: từ 100$ xuống 10$) và hoàn thành lab.
        ![solved](./images/solved.png)
        
        - **Giải thích**: Race condition xảy ra khi yêu cầu thêm sản phẩm đắt tiền (`Lightweight "l33t" Leather Jacket`) và yêu cầu thanh toán được xử lý đồng thời, khiến server áp dụng giá của gift card (sản phẩm rẻ hơn) cho đơn hàng.

### Bài học rút ra
- Hiểu cách khai thác lỗ hổng race condition qua nhiều endpoint để thao túng logic nghiệp vụ, dẫn đến mua sản phẩm với giá không mong muốn.
- Nhận thức tầm quan trọng của việc đồng bộ hóa xử lý yêu cầu giữa các endpoint (thêm sản phẩm, thanh toán) để ngăn chặn race condition.
### Tài liệu tham khảo
- PortSwigger: Race conditions
- PortSwigger: Business logic vulnerabilities

### Kết luận
Lab này cung cấp kinh nghiệm thực tiễn trong việc khai thác lỗ hổng race condition qua nhiều endpoint, sử dụng Burp Repeater để gửi yêu cầu song song, thao túng giỏ hàng, và mua sản phẩm với giá thấp. Xem portfolio đầy đủ tại https://github.com/Furu2805/Lab_PortSwigger.

*Viết bởi Toàn Lương, Tháng 7/2025.*