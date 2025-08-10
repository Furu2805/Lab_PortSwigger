# Write-ups: Exploiting DOM clobbering to enable XSS

### Tổng quan
Khai thác lỗ hổng DOM clobbering trong ứng dụng, nơi đoạn mã JavaScript trong `htmlJanitor.js` sử dụng node.attributes để lọc thuộc tính HTML nhưng không kiểm tra an toàn. Bằng cách chèn thẻ `<input>` với `name="attributes"` vào comment của bài post, kẻ tấn công ghi đè `node.attributes` thành một phần tử HTML, khiến vòng lặp lọc thuộc tính bị bỏ qua, cho phép thuộc tính `onfocus=print()` được giữ lại và thực thi XSS. Payload được kết hợp với Exploit Server để điều hướng URL chứa `#x`, kích hoạt `print()` và hoàn thành lab.

### Mục tiêu
- Khai thác lỗ hổng DOM clobbering bằng cách chèn thẻ `<input>` với `name="attributes"` vào comment để ghi đè `node.attributes`, bypass bộ lọc thuộc tính, thực thi lệnh `print()` trên trình duyệt nạn nhân và hoàn thành lab.

### Công cụ sử dụng
- Burp Suite Pro
- Firefox Browser

### Quy trình khai thác
1. **Thu thập thông tin (Reconnaissance)**
- Truy cập trang web và quan sát trong Burp Proxy HTTP history, request tới file JavaScript:
    `GET /resources/js/htmlJanitor.js`
- **Phản hồi:**
    - File chứa đoạn mã:
        ```javascript
        // Sanitize attributes
        for (var a = 0; a < node.attributes.length; a += 1) {
            var attr = node.attributes[a];
            if (shouldRejectAttr(attr, allowedAttrs, node)) {
            node.removeAttribute(attr.name);
            // Shift the array to continue looping.
            a = a - 1;
            }
        }
        ```
- Phân tích:
    - Script lặp qua `node.attributes` để lọc các thuộc tính HTML không an toàn.
    - Nếu `node.attributes` bị ghi đè thành một phần tử HTML (thay vì HTMLCollection), vòng lặp `for` không chạy do `node.attributes.length` là undefined, dẫn đến bypass bộ lọc.
        ![script](./images/1_santisize.png)

2. **Khai thác (Exploitation)**
- **Ý tưởng khai thác:**
    - Chèn thẻ `<form id=x tabindex=0 onfocus=print()><input id=attributes>` vào comment để:
        - Ghi đè `node.attributes` bằng thẻ `<input id=attributes>`, khiến `node.attributes.length` trả về `undefined`.
        - Bỏ qua vòng lặp lọc, giữ lại thuộc tính `onfocus=print()` trên thẻ `<form id=x>`.

- Tạo payload và chèn vào comment của bài post bất kỳ
    ```html
    <form id=x tabindex=0 onfocus=print()><input id=attributes>
    ```
    ![comment](./images/2_comment.png)
    - xác nhận thực hiện lệnh print():
        ![in](./images/3_x.png)

- Sử dụng Exploit Server để gửi payload điều hướng URL, gửi cho nạn nhân và hoàn thành lab
    ```html
    <iframe src="https://0a4d0060039910cc8019034100630007.web-security-academy.net/post?postId=7" onload="setTimeout(() => this.src=this.src+'#x', 500)">
    ```
    ![body](./images/4_body.png)
    ![solved](./images/5_solved.png)

### Bài học rút ra
- Hiểu cách khai thác DOM clobbering bằng cách chèn thẻ `<input>` với `name="attributes"` để ghi đè `node.attributes`, bypass bộ lọc thuộc tính và thực thi mã JavaScript thông qua sự kiện `onfocus`.
- Nhận thức tầm quan trọng của việc kiểm tra an toàn các thuộc tính DOM và tránh sử dụng các thuộc tính dễ bị ghi đè (`node.attributes`) trong mã JavaScript để ngăn chặn các cuộc tấn công XSS.

### Kết luận
Lab này cung cấp kinh nghiệm thực tiễn trong việc khai thác DOM clobbering để bypass bộ lọc thuộc tính và kích hoạt XSS, nhấn mạnh tầm quan trọng của việc kiểm tra an toàn các thuộc tính DOM và xử lý dữ liệu đầu vào để bảo vệ ứng dụng khỏi các cuộc tấn công XSS. Xem portfolio đầy đủ tại https://github.com/Furu2805/Lab_PortSwigger.

*Viết bởi Toàn Lương, Tháng 8/2025.*