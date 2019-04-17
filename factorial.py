x = int(input("Please enter a number:=>"))
y=1
if x > 0:
    for i in range (1,x+1):
        y=y*i
        print(f"factorial of {x} is {y}")
elif x==0:
    print("Factorial of 0 is 1")
else:
    print("Sorry, Factorial of Negative number does not exit")