def even_num(x):
    if x % 2 == 0:
        return True
    else:
        return False
def prime_num(x):
    a = 1
    factors = 0
    while a < x+1:
        if x % a == 0:
            factors += 1
            a += 1
        else:
            a += 1
    if factors == 2:
        return True
    else:
        return False
def perfect_num(x):
    a = 1
    total_factors = 0
    while a < x+1:
        if x % a == 0:
            # print("PLUSPLUS", a)
            total_factors += a
            a += 1
        else:
            a += 1
    total_factors -= x
    # print(total_factors)
    if total_factors == x:
        return True
    else:
        return False
number = int(input("Nhập một số nguyên dương bất kì bạn muốn bỏ vào bộ kiểm tra số học: "))
choice = int(input("Chọn bộ kiểm tra số học (1 = số chẵn, 2 = số nguyên tố, 3 = số hoàn hảo): "))
if choice == 1:
    print("Số đó là số chẵn:", even_num(number))
elif choice == 2:
    print("Số đó là số nguyên tố:", prime_num(number))
elif choice == 3:
    print("Số đó là số hoàn hảo:", perfect_num(number))