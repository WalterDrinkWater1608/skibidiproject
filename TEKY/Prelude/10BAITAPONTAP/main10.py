import random
while True:
    length = int(input("Nhập độ dài N (Với N >= 10): "))
    if length >= 8:
        break
    else:
        continue
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
passwordlist = list(password)
random.shuffle(passwordlist)
finalpassword = "".join(passwordlist)

print(f"Mật khẩu chuẩn ({length} ký tự):", password,)