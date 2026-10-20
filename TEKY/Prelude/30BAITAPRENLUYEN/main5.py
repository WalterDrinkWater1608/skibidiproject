age = int(input("Điền tuổi: "))
score = float(input("Điền điểm bài kiểm tra: "))
if age >= 13:
    if score >= 7.0:
        print("Kết quả: Đạt (Cả 2 tiêu chí)")
    else:
        print("Kết quả: Đạt tiêu chí tuổi, không đạt tiêu chí điểm")
else:
    if score >= 7.0:
        print("Kết quả: Đạt tiêu chí điểm, không đạt tiêu chí tuổi ")
    else:
        print("Kết quả: Không đạt tiêu chí điểm, không đạt tiêu chí tuổi")

#????? Không bt làm đúng chưa :sob: