def simultaneous_equations(a,b,c,d,e,f):
    #ax + bx = e
    #cx + dx = f
    main_determinant = a*d - b*c
    x_determinant = e*d - b*f
    y_determinant = a*f - c*e
    x = x_determinant/main_determinant
    y = y_determinant/main_determinant
    return x, y

print("Simultaneous equations calculator!\n\nax + by = e\ncx + dy = f\n")

a = float(input("Please input variable a:"))
b = float(input("Please input variable b:"))
c = float(input("Please input variable c:"))
d = float(input("Please input variable d:"))
e = float(input("Please input variable e:"))
f = float(input("Please input variable f:"))

sign1 = "+"
sign2 = "+"
b_1 = b
d_1 = d
if b < 0:
    b_1 = b*-1
    sign1 = "-"

if d < 0:
    d_1 = d*-1
    sign2 = "-"

print(f"\nHere's the complete simultaneous equations you've typed:\n\n{a}x {sign1} {b_1}y = {e}\n{c}x {sign2} {d_1}y = {f}\n")
x,y = simultaneous_equations(a,b,c,d,e,f)
print(f"The answer to x and y are:\nx = {x}\ny = {y}")
