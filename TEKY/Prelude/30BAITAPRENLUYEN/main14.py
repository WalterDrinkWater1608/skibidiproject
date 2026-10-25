def function(x):
    if 0 <= x <= 10:
        if x >= 9:
            string = "Xuất sắc"
        elif x >= 8:
            string = "Giỏi"
        elif x >= 6.5:
            string = "Khá"
        elif x >= 5:
            string = "Đạt"
        else:
            string = "Chưa đạt"
    else:
        string = "Không hợp lệ"
    return string
hs1 = float(input("Nhập điểm trung bình của học sinh 1: "))
hs2 = float(input("Nhập điểm trung bình của học sinh 2: "))
hs3 = float(input("Nhập điểm trung bình của học sinh 3: "))
hs4 = float(input("Nhập điểm trung bình của học sinh 4: "))
hs5 = float(input("Nhập điểm trung bình của học sinh 5: "))

criths1 = function(hs1)
criths2 = function(hs2)
criths3 = function(hs3)
criths4 = function(hs4)
criths5 = function(hs5)

print(f"Xếp loại học sinh 1: {criths1}\nXếp loại học sinh 2: {criths2}\nXếp loại học sinh 3: {criths3}\nXếp loại học sinh 4: {criths4}\nXếp loại học sinh 5: {criths5}")