# Write-up: SQL injection UNION attack, determining the number of columns returned by the query

### Tổng quan
Ghi lại quá trình khai thác SQLi để xác định số cột trả về bởi truy vấn.

### Mục tiêu
Xác định số cột trả về của truy vấn.

### Công cụ
- Burpsuite Community
- Firefox Browser

### Các bước thực hiện
1. **Thu thập thông tin (Recon)**
- Kiểm tra tham số `category` trong URL (`filter?category=Pets`) và thêm dấu `'` để kích hoạt lỗi SQL
  - **Kết quả**: xuất hiện lỗi SQL, xác nhận lỗ hổng
    ![lỗi](./images/error.png)

2. **Tạo payload**
- Tạo payload kiểu tấn công UNION để xác định số cột trả về.
    ```
    ' UNION SELECT NULL, NULL, NULL--
    ```

3. **Khai Thác (Exploitation)**
- Gửi payload qua Burp Repeater:
    ```
    GET /filter?category=Pets'+UNION+SELECT+NULL,+NULL,+NULL-- HTTP/2
    ```
    - **Kết quả**: xác nhận số cột trả về là 3 và hoàn thành bài lab    
        ![kết quả](./images/determine.png)

### Bài học rút ra
- Xác định sốt cột trả về của truy vấn là bước đầu tiên trong việc khai thác SQLi

### Tài liệu tham khảo
- PortSwigger: SQL Injection cheat sheet

### Kết luận
Lab này giúp tôi hoàn thiện kỹ năng SQL injection và sử dụng Burp Suite. Xem portfolio đầy đủ tại https://github.com/Furu2805/Lab_PortSwigger 

*Viết bởi Toàn Lương, Tháng 5/2025*.