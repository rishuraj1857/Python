x = int(input("Please enter a number:=> "))
sum = 0
temp=x
while x>0:
    digit = temp % 10
    sum+=digit**3
    temp //= 10
    if x==sum:
        print(f"{x} is an arm strong number")
        break
    else:
        print(f"{x} is not an armstrong number")
        break