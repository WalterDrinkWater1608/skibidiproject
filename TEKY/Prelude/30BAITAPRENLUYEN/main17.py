product = "Aquafina 2L water bottle"
quantity = 6
price = 15000
total_cost = price*quantity
product1 = "TÊN SẢN PHẨM"
quantity1 = "SỐ LƯỢNG"
price1 = "GIÁ TIỀN"
total1 = "TỔNG TIỀN"
print("="*65)
print(" "*25,"BẢN DỮ LIỆU")
print("="*65)
print(f"{product1:<25}{quantity1:>15}{price1:>15}")
print("-"*65)
print(f"{product:<25}{quantity:>15}{price:>15}")

print("-"*65)

print(f"{total1:<40}{total_cost:>15}")