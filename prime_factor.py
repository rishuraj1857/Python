x = int(input("Please enter a number to get ts prime factors:=>"))
for i in range (1,x+1):
    if x%i==0:
        print(f"The prime factors of {x} is {i}")
    else:
        continue