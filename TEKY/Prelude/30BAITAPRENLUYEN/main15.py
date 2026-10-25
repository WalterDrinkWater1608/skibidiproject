def electricity_price(x):
    price1 = 1800
    price2 = 2000
    price3 = 2500
    if x > 0:
        if x <= 50:
            cost = price1*x
        elif x <= 100:
            cost = price1*50 + price2*(x-50)
        else:
            cost = price1*50 + price2*50 + price3*(x-100)
    else:
        cost = "Nuh uh"
    return cost
while True:
    x = float(input("Nhập kWh điện bạn đã dùng: "))
    if x > 0:
        break
payup = electricity_price(x)
print(f"Số tiền bạn phải trả khi bạn dùng {x} kWh điện trong tháng: {payup} đồng")