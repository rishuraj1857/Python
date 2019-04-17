a=int(input("enter any no:- "))
b=0
sum=0
temp=a
while a>0:
    b=a%10
    a=a//10
    sum=sum+ b**3
if sum==temp:
    print(f"{temp} is armstrong number")
else:
    print(f"{temp} is not armstrong number")

