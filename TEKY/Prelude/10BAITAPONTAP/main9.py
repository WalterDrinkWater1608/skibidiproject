import random
name = input("Nhập họ và tên: ")
name1 = name.strip()
namelist = name1.split()
username = ""
a = 0
while a < len(namelist):
    username += (namelist[a][0])
    a += 1
name2 = name1.replace(" ","")
username += name2[::-1]
username += str(random.randint(10,99))
print(username)