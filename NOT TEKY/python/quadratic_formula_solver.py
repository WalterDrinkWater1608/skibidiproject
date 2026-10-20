import cmath
def solve_quadratic(a, b, c):
    # Calculate the discriminant (b^2 - 4ac)
    delta = (b**2) - (4*a*c)
    
    # Find two solutions using the quadratic formula
    x1 = (-b - cmath.sqrt(delta)) / (2*a)
    x2 = (-b + cmath.sqrt(delta)) / (2*a)
    
    return x1, x2

print("ax^2 + bx + c = 0")
print("Enter the coefficients a, b, and c:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
print(f"The equation is: {a}x^2 + {b}x + {c} = 0")
root1, root2 = solve_quadratic(a, b, c)
print(f"The x1 and x2 respectively are: {root1} and {root2}")