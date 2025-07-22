# Write-up: DOM XSS in jQuery anchor `href` attribute sink using `location.search` source

### Tổng quan
Khai thác lỗ hổng DOM-based Cross-Site Scripting (XSS) trong chức năng submit feedback, nơi tham số `returnPath` từ `location.search` được chèn trực tiếp vào thuộc tính href của thẻ `<a>` thông qua jQuery mà không được làm sạch, cho phép thực thi mã JavaScript qua payload `javascript:alert(document.cookie)` để hoàn thành lab.

### Mục tiêu
- Khai thác lỗ hổng DOM XSS trong chức năng submit feedback bằng cách sử dụng tham số returnPath để chèn mã JavaScript vào thuộc tính `href` và thực thi `alert(document.cookie)` để hoàn thành lab.

### Công cụ sử dụng
- Burp Suite Community
- Firefox Browser

### Quy trình khai thác
1. **Thu thập thông tin (Reconnaissance)**
- Truy cập chức năng submit feedback của ứng dụng `/feedback`
- Quan sát URL chứa tham số `returnPath=/`
    - `Phản hồi`: Trang feedback hiển thị liên kết "Back" với thẻ
        `<a id="backLink" href="/"></a>`

- Sử dụng Dev Tools (F12) để kiểm tra, thấy thẻ `<a>` được gán thuộc tính href động: `/feedback?returnPath=abc123`
    - **Phản hồi**: Thẻ `<a>` trở thành:
        `<a id="backLink" href="abc123">Back</a>`
    - **Quan sát**: Tham số returnPath từ `location.search` được jQuery sử dụng để gán trực tiếp vào thuộc tính href của thẻ `<a id="backLink">` mà không được làm sạch, gợi ý khả năng khai thác DOM XSS:

2. **Khai thác (Exploitation)**
- Chèn payload XSS vào tham số `returnPath`: `javascript:alert(document.cookie)`
    - Khi người dùng nhấp vào liên kết `"Back"`, mã JavaScript `alert(document.cookie)` được thực thi, hiển thị hộp thoại chứa cookie của người dùng và hoàn thành lab
        ![solved](./images/1_solved.png)
    
### Bài học rút ra
- Hiểu cách khai thác lỗ hổng DOM XSS bằng cách chèn mã JavaScript vào thuộc tính `href` của thẻ `<a>` thông qua tham số `location.search` được xử lý bởi jQuery.

### Tài liệu tham khảo
- PortSwigger: Cross-Site Scripting (XSS)

### Kết luận
Lab này cung cấp kinh nghiệm thực tiễn trong việc phát hiện và khai thác lỗ hổng DOM XSS thông qua việc sử dụng tham số location.search trong jQuery, nhấn mạnh tầm quan trọng của việc làm sạch input người dùng trong xử lý DOM. Xem portfolio đầy đủ tại https://github.com/Furu2805/Lab_PortSwigger.

*Viết bởi Toàn Lương, Tháng 7/2025.*