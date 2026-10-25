username = input("Tên người dùng: ").strip()
email = input("Email: ").strip().lower()

username_ok = len(username) >= 5 and " " not in username
vi_tri_a = email.find("@")
email_ok = vi_tri_a > 0 and "." in email[vi_tri_a + 1:] and not email.endswith(".")

print("Tên người dùng hợp lệ:", username_ok)
print("Email có dạng cơ bản hợp lệ:", email_ok)