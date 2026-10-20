name = input("Nhập họ và tên của bạn: ").strip()
name = name.title()
namelist = name.split()
if not namelist:
    print("Chưa nhập họ tên")
print(name)
length = len(namelist)
string1 = ""
length -= 1
i = 0
length1 = 0

while i <= length:
    string = namelist[i][0]
    string1 += string
    string1 += "."
    length1 += len(namelist[i])
    i += 1

print(string1)
print(f"Độ dài của tên: {length1}")