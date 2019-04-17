x = float(input("Please enter the value of side one:=>"))
y = float(input("Please enter the value of side two:=>"))
z = float(input("Please enter the value of side three:=>"))
p = (x+y+z)/2
q = p*(p-x)*(p-y)*(p-z)
area = q**0.5
print(f"Area of the triangle with side {x}, {y}, {z} is {area}")