print("[", end='')

with open('password.txt', 'r') as f:
    lines = [line.strip() for line in f]

for i, pwd in enumerate(lines):
    print(f'"{pwd}"', end='')
    if i < len(lines) - 1:
        print(",", end='')

# Thêm phần tử "random" sau dấu phẩy (nếu danh sách ban đầu không rỗng thì thêm dấu , trước đó)
if lines:
    print(',', end='')
print('"random"]', end='')