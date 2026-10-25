math = float(input("Nhập điểm toán: "))
literature = float(input("Nhập điểm văn: "))
crit1 = math >= 5 and literature >= 5
crit2 = math >= 8 or literature >= 8
crit3 = math < 3 or literature < 3
crit4 = (math+literature)/2 >= 8 and math >= 6 and literature >= 6
print(f"TC1: Cả 2 môn đều >= 5: {crit1}\nTC2: Có ít nhất một môn >= 8: {crit2}\nTC3: Học sinh này có bị điểm liệt (<3 ở bất kì môn nào) hay không: {crit3}\nTC4: Đạt 'học sinh giỏi' nếu điểm trung bình >= 8 và không có môn nào dưới 6: {crit4}")
