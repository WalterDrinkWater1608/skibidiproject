name = input("Nhập tên của bạn: ")
age = int(input("Nhập tuổi của bạn: "))
print(f"Xin chào {name}! Sang năm bạn {age+1} tuổi.")
while True:
    width = float(input("Nhập chiều rộng của hình chữ nhật: "))
    if width > 0:
        break
    else:  
        continue
while True:
    length = float(input("Nhập chiều dài của hình chữ nhật: "))
    if length > 0:
        break
    else:
        continue

print(f"Chu vi và diện tích của hình chữ nhật với chiều dài là {length} và chiều rộng là {width} lần lượt là {2*(length+width)} và {length*width}")