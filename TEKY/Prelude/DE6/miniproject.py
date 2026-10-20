import random
print("========================================\n   TRÌNH TẠO MẬT KHẨU NGẨU NHIÊN\n========================================\n")
length = int(input("Nhập độ dài mật khẩu: "))
cond1 = input("Có muốn bao gồm chữ hoa (Y/N):")
cond2 = input("Có muốn bao gồm chữ số (Y/N):")
cond3 = input("Có muốn bao gồm ký tự đặc biệt (Y/N):")

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
        if cond1 == "Y":
            password += random.choice(abc_1)
        add += 1
    elif add == 3:
        if cond2 == "Y":
            password += random.choice(num)
        add += 1
    elif add == 4:
        if cond3 == "Y":
            password += random.choice(symbol)
        add = 1

print(f"========================================\n  Mật khẩu tùy chỉnh: {password}\n========================================")