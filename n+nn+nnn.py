x =int(input("Please enter a number:=>"))
if x<0:
    print(0)
else:
    a = str(x)
    b = int(a+a)
    c = int(a+a+a)
    d = x+b+c
    print(f"The value is {d}")