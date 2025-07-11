# Write-up: SSRF with whitelist-based input filter

### Tổng quan
Khai thác lỗ hổng Server-Side Request Forgery (SSRF) trong chức năng kiểm tra kho hàng (stock check), bypass bộ lọc whitelist bằng kỹ thuật double URL encoding (`%2523` để giả mạo `#`) nhằm truy cập hệ thống nội bộ tại `http://localhost/admin`, sau đó xóa tài khoản `carlos` để hoàn thành lab.

### Mục tiêu
- Bypass bộ lọc whitelist của chức năng check stock để truy cập admin panel tại `http://localhost/admin` và xóa tài khoản `carlos`.

### Công cụ sử dụng
- Burp Suite Community
- Firefox Browser

### Quy trình khai thác
1. **Thu thập thông tin (Reconnaissance)**
- Kiểm tra chức năng check stock trên giao diện web với một sản phẩm bất kì
- Trong Burp Suite Proxy, bắt được yêu cầu:
    ![check](./images/1_check_stock.png)
    - **Quan sát**: Tham số `stockApi` chứa URL gọi tới hệ thống nội bộ, gợi ý khả năng tồn tại lỗ hổng SSRF nhưng bị hạn chế bởi bộ lọc whitelist:

- Thử thay đổi `stockApi` thành `http://localhost/admin` trong Burp Repeater:
    ![check](./images/2_stock_check_hosst.png)
    - **Phản hồi**: `"External stock check host must be stock.weliketoshop.net"`, xác nhận bộ lọc whitelist chỉ cho phép domain `stock.weliketoshop.net`.

2. **Khai thác (Exploitation)**
- Bypass bộ lọc whitelist bằng kỹ thuật double URL encoding, sử dụng `#` (mã hóa thành `%23`, double encode thành `%2523`) để giả mạo domain:
    - **Giải thích**: `http://localhost:80%2523@stock.weliketoshop.net/admin` được server hiểu là truy cập `localhost:80` vì `#` (sau khi decode `%2523`) bỏ qua phần `@stock.weliketoshop.net`, nhưng bộ lọc chỉ kiểm tra domain `stock.weliketoshop.net`.
    
    - **Phản hồi**: Nhận được nội dung admin panel:
    ![admin](./images/3_admin.png)

- Sửa stockApi để xóa tài khoản carlos:
    - **Phản hồi**: Tài khoản carlos bị xóa:
        ![delete](./images/4_delete.png)
    - **Giải thích**: Kỹ thuật double URL encoding bypass bộ lọc whitelist, cho phép gửi yêu cầu tới endpoint nội bộ `/admin/delete?username=carlos` mà không cần xác thực

- Hoàn thành lab:
    ![solved](./images/5_solved.png)

### Bài học rút ra
- Hiểu cách khai thác lỗ hổng SSRF bằng kỹ thuật double URL encoding để bypass bộ lọc whitelist và truy cập hệ thống nội bộ.
- Nhận thức tầm quan trọng của việc triển khai bộ lọc whitelist chặt chẽ, kiểm tra toàn bộ URL và xử lý đúng các ký tự mã hóa để ngăn chặn SSRF.

### Tài liệu tham khảo
- PortSwigger: Server-Side Request Forgery (SSRF)
- PortSwigger: Bypassing SSRF filters

### Kết luận
Lab này cung cấp kinh nghiệm thực tiễn trong việc khai thác lỗ hổng SSRF, sử dụng kỹ thuật double URL encoding để bypass bộ lọc whitelist, truy cập hệ thống nội bộ, và xóa tài khoản mục tiêu. Xem portfolio đầy đủ tại https://github.com/Furu2805/Lab_PortSwigger.

*Viết bởi Toàn Lương, Tháng 7/2025.*