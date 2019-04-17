a = float(input("Enter the marks of Hindi:=>"))
b = float(input("Enter the marks of English:=>"))
c = float(input("Enter the marks of Maths:=>"))
d = float(input("Enter the marks of Science:=>"))
e = float(input("Enter the marks of Social Studies:=>"))
y = a+b+c+d+e
print(f"Total marks obtained is {y} out 500. ")
x = (y*100)/500
print(f"{x} percent marks obtained")
if x>=60:
    print("First division")
elif x>=45:
    print("Second Division")
elif x>=33:
    print("Third Division")
else:
    print("Fail!!")