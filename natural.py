x = int(input("Please enter the limit->"))
sum = 0
for i in range(1,x+1):
    sum+=i
    x-=1
    print(sum)