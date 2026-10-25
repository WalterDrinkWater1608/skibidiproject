a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
print(f"{a} + {b} = {a+b}\n{a} - {b} = {a-b}\n{a} * {b} = {a*b}\n{a} / {b} = {a/b}\n{a} // {b} = {a//b}\n{a} % {b} = {a%b}\n{a} ** {b} = {a**b}")
a_1 = a%2 == 0
b_1 = b%2 == 0
print(f"Số a ({a}) là số chẵn: {a_1}\nSố b ({b}) là số chẵn: {b_1}")