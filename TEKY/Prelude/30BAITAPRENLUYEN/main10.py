while True:
    code = input("Nhập mã sản phẩm: ")
    if len(code) == 14:
        if code[2] == "-":
            if code[7] == "-":
                break
    continue
code1 = code.strip()
codelist = code1.split("-")
print(codelist[0])
print(codelist[1])
print(codelist[2])
codepart1 = codelist[0]
codepart2 = codelist[1]
codepart3 = codelist[2][0] + codelist[2][1]
codepart4 = codelist[2][2] + codelist[2][3] + codelist[2][4] + codelist[2][5]

# print(codepart1,codepart2,codepart3,codepart4)

print(f"Mã hiển thị mới: {codepart3} / {codepart4} / {codepart2}")