x = float(input("Enter first number="))
y = float(input("Enter second number="))
z = float(input("Enter third number="))
if x>y and x>z:
	print(f"{x} is greater than {y} and {z}")
elif y>x and y>z:
	print(f"{y} is greater than {x} and {z}")
else:
	print(f"{z} is greatr than {x} and {y}")
