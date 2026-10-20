import random
length = int(input("Nhập độ dài N (Với N >= 4): "))
a = 1
abc = "abcdefghijklmnopqrstuvwxyz"
abc_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
symbol = "!@#$%^&*"
add = 1
password = ""
for a in range (length):
    if add == 1:
        password += random.choice(abc)
        add += 1
    elif add == 2:
        password += random.choice(abc_1)
        add += 1
    elif add == 3:
        password += random.choice(num)
        add += 1
    elif add == 4:
        password += random.choice(symbol)
        add = 1

print("Mật khẩu chuẩn:", password, "(Đảm bảo có đủ cả 4 loại ký tự)")