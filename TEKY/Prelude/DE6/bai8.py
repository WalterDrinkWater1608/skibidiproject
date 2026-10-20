import random
length = int(input("Nhập độ dài N: "))
a = b = c = 1
abc = "abcdefghijklmnopqrstuvwxyz"
abc_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
symbol = "!@#$%^&*"
add = 1
password = ""
password2 = ""
password3 = ""
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

for b in range (length):
    if add == 1:
        password2 += random.choice(abc)
        add += 1
    elif add == 2:
        password2 += random.choice(abc_1)
        add += 1
    elif add == 3:
        password2 += random.choice(num)
        add += 1
    elif add == 4:
        password2 += random.choice(symbol)
        add = 1

for c in range (length):
    if add == 1:
        password3 += random.choice(abc)
        add += 1
    elif add == 2:
        password3 += random.choice(abc_1)
        add += 1
    elif add == 3:
        password3 += random.choice(num)
        add += 1
    elif add == 4:
        password3 += random.choice(symbol)
        add = 1

print(f"--- GỢI Ý MẬT KHẨU ---\n1. {password}\n2. {password2}\n3. {password3}")