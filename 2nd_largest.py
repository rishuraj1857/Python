a = []
x = int(input("Please enter the range:=>"))
for  i in range(1,x+1):
    elem=int(input("Please enter the element:=>"))
    a.append(elem)
a.sort()
b = a[x-2]
print(f"The second largest number in the List is {b}")