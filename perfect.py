x = int(input("Please enter a number to know if its a perfect number :=>"))
sum = 0
for i in range (1,x):
    if x%i==0:
        sum= sum+i
if sum==x:
    print(f"yes! {x} is a perfect number")
else:
    print(f"Nope! {x} is not a perfect number")