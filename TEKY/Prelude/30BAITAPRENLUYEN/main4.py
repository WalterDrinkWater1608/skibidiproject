time = int(input("Nhập tổng số giây không âm: "))
hour = time // 3600
minute = (time % 3600)//60
second = time % 60

print(f"THỜI GIAN IN THEO ĐỊNH DẠNG: {hour:02d}:{minute:02d}:{second:02d}")