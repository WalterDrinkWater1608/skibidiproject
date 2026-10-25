def rectangle(x,y):
    a = x*y
    return a
def triangle(x,y):
    #x = đáy, y = cao
    a = x*y*1/2
    return a
def circle(x):
    k = x*x*3.141
    return k

while True:
    choice = input("Chọn hàm bạn muốn dùng (a:hcn, b:tamgiacs, c:hinhtronf)")
    if choice == "a":
        x = float(input("Nhập giá trị x (chiều dài): "))
        y = float(input("Nhập giá trị y (chiều rộng): "))
        a = rectangle(x,y)
        string1 = "Kết quả sau khi tính diện tích của hình chữ nhật: "
        break
    elif choice == "b":
        x = float(input("Nhập giá trị x (chiều dài đáy): "))
        y = float(input("Nhập giá trị y (chiều cao): "))
        a = triangle(x,y)
        string1 = "Kết quả sau khi tính diện tích của hình tam giác: "
        break
    elif choice == "c":
        x = float(input("Nhập giá trị x (r): "))
        a = circle(x)
        string1 = "Kết quả sau khi tính diện tích của hình tròn: "
        break
    else:
        continue
print(f"{string1}{a}")