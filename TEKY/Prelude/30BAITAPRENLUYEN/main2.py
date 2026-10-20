name = input("Nhập tên của sản phẩm: ")
price = float(input(f"Nhập giá của {name}: "))
quantity = int(input(f"Nhập số lượng của {name}: "))
discount = -5
while True:
    try:
        discount = int(input(f"Nhập phần trăm được giảm khi mua {name}: "))
        if 0 <= discount <= 100:
            break
    except ValueError:
        continue
discounted = (price*discount/100)*quantity
final_price = price*quantity - discounted

print("\n\n","="*35,f"\nTÊN SẢN PHẨM: {name}\nGIÁ TIỀN TRƯỚC KHI GIẢM: {price}\nTỔNG SỐ TIỀN ĐƯỢC GIẢM: {discounted:.2f}\nTỔNG SỐ TIỀN PHẢI THANH TOÁN: {final_price:.2f}\n","="*35)