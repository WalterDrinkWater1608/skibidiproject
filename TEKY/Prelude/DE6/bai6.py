import random
skibidi = input("Nhập câu: ")
skibidi1 = skibidi.split()
random.shuffle(skibidi1)
skibidi2 = " ".join(skibidi1)
print("Kết quả xáo trộn: ", skibidi2)