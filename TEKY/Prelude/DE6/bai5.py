import random
length = int(input("Nhập độ dài N: "))
a = 1
abc = "abcdefghijklmnopqrstuvwxyz"
password = ""
for a in range (length):
    password += random.choice(abc)

print("Mật khẩu của bạn:", password)