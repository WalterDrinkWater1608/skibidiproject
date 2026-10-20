temperature = float(input("Nhập nhiệt độ: "))
choice = input("Chọn chuyển từ celcius sang fahrenheit hay ngược lại (0 = celcius sang fahrenheit, 1 = ngược lại): ")
if choice == "0":
    temperature2 = temperature*9/5+32
    print(f"Từ celcius chuyển sang fahrenheit: {temperature}C ={temperature2}F")
elif choice == "1":
    temperature2 = 5*(temperature-32)/9
    print(f"Từ fahrenheit chuyển sang celcius: {temperature}F ={temperature2}C")
else:
    print("Lựa chọn không hợp lệ")