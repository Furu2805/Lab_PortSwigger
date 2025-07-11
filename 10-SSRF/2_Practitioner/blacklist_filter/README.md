# Write-up: SSRF with blacklist-based input filter

### Tổng quan
Khai thác lỗ hổng Server-Side Request Forgery (SSRF) trong chức năng kiểm tra kho hàng (stock check), bypass bộ lọc blacklist bằng cách mã hóa URL để truy cập hệ thống nội bộ tại http://localhost/admin, sau đó xóa tài khoản carlos để hoàn thành lab.

### Mục tiêu
- Bypass bộ lọc blacklist của chức năng check stock để truy cập admin panel tại `http://localhost/admin` và xóa tài khoản `carlos`.

### Công cụ sử dụng
- Burp Suite Community
- Firefox Browser

### Quy trình khai thác
1. **Thu thập thông tin (Reconnaissance)**
- Kiểm tra chức năng check stock trên giao diện web với một sản phẩm bất kỳ
- Trong Burp Suite Proxy, bắt được yêu cầu:
    ![check](./images/1_check_stock.png)
    - **Quan sát**: Tham số `stockApi` chứa URL gọi tới hệ thống nội bộ, gợi ý khả năng tồn tại lỗ hổng SSRF. Bộ lọc blacklist có thể chặn `localhost` hoặc `127.0.0.1`:

2. **Khai thác (Exploitation)**
- Gửi yêu cầu `POST /product/stock` tới Burp Repeater, thử thay đổi tham số stockApi thành `http://localhost/admin`:
    - **Phản hồi**: Bị chặn do bộ lọc blacklist

- Bypass bộ lọc bằng cách sử dụng địa chỉ `127.0.1` (biến thể của `127.0.0.1`) và mã hóa `/admin` thành `/%25%36%31dmin`
    - Phản hồi: Nhận được nội dung admin panel:
    ![admin](./images/2_admin.png)

- Sửa tham số `stockApi=http://127.0.1/%25%36%31dmin/delete?username=carlos` :
    - **Phản hồi**: Tài khoản `carlos` bị xóa:
        ![delete](./images/3_delete.png)
    
    - **Giải thích**: Bộ lọc blacklist không chặn `127.0.1` và không xử lý đầy đủ mã hóa URL, cho phép gửi yêu cầu tới endpoint nội bộ `/admin/delete?username=carlos` mà không cần xác thực.

- Hoàn thành lab:
    ![solved](./images/4_solved.png)

### Bài học rút ra
- Hiểu cách khai thác lỗ hổng SSRF bằng cách bypass bộ lọc blacklist thông qua biến thể địa chỉ IP và mã hóa URL.
- Nhận thức tầm quan trọng của việc triển khai bộ lọc whitelist hoặc kiểm tra chặt chẽ đầu vào URL để ngăn chặn SSRF.

### Tài liệu tham khảo
- PortSwigger: Server-Side Request Forgery (SSRF)
- PortSwigger: Bypassing SSRF filters

### Kết luận
Lab này cung cấp kinh nghiệm thực tiễn trong việc khai thác lỗ hổng SSRF, sử dụng Burp Repeater để bypass bộ lọc blacklist, truy cập hệ thống nội bộ, và xóa tài khoản mục tiêu. Xem portfolio đầy đủ tại https://github.com/Furu2805/Lab_PortSwigger.

*(Viết bởi Toàn Lương, Tháng 7/2025.)*