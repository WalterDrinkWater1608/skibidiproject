password = input("Nhập mật khẩu: ")
password1 = password.strip(" ")
length_crit = len(password1) >= 10
lower_crit = False
upper_crit = False
numbers = False
special = False
specials = "! @ # $ % ^ & * ( )"
specials1 = specials.split()
a = 0
b = 0
# print(specials1)
while a != len(password1):
    if password1[a].islower():
        lower_crit = True
    elif password1[a].isupper():
        upper_crit = True
    elif password1[a].isdigit():
        numbers = True
    else:
        while b != 10:
            if password1[a] == specials1[b]:
                special = True
                break
            else:
                b += 1
    a += 1
if lower_crit == upper_crit == numbers == special == True:
    goodgood = "mạnh"
else:
    goodgood = "yếu"
print(f"Trạng thái của mật khẩu:\nCó chữ thường: {lower_crit}\nCó chữ hoa: {upper_crit}\nCó số: {numbers}\nCó kí tự đặc biệt: {special}\nTỔNG QUÁT: Mật khẩu này là mật khẩu {goodgood}!")