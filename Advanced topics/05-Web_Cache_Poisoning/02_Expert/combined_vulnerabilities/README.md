# Write-up: Combining web cache poisoning vulnerabilities

### Tổng quan

### Công cụ sử dụng

### Quy trình khai thác

1. Xác định vị trí poison
- Trong trang home ta quan sát thấy hàm initTranslations với tham số thứ nhất được concat bởi data.host

- Hàm được định nghĩa như sau:
    ```java
    function initTranslations(jsonUrl)
    {
        const lang = document.cookie.split(';')
            .map(c => c.trim().split('='))
            .filter(p => p[0] === 'lang')
            .map(p => p[1])
            .find(() => true);

        const translate = (dict, el) => {
            for (const k in dict) {
                if (el.innerHTML === k) {
                    el.innerHTML = dict[k];
                } else {
                    el.childNodes.forEach(el_ => translate(dict, el_));
                }
            }
        }

        fetch(jsonUrl)
            .then(r => r.json())
            .then(j => {
                const select = document.getElementById('lang-select');
                if (select) {
                    for (const code in j) {
                        const name = j[code].name;
                        const el = document.createElement("option");
                        el.setAttribute("value", code);
                        el.innerText = name;
                        select.appendChild(el);
                        if (code === lang) {
                            select.selectedIndex = select.childElementCount - 1;
                        }
                    }
                }

                lang in j && lang.toLowerCase() !== 'en' && j[lang].translations && translate(j[lang].translations, document.getElementsByClassName('maincontainer')[0]);
            });
    }
    ```

- Poison giá trị của host trong data thành exploit server
    ![poison](./images/3_poison.png)



1. Khai thác web cache thực hiện xss
- Setup exploit server
    ![exploit](./images/6_exploit.png)

- Gửi với header x-forwarded-host: exploit-server
    - Kết quả: hoàn thành lab
    ![solved](./images/7_solved.png)




### Bài học rút ra

### Kết luận 