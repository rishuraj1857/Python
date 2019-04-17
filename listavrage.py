n= int(input("Please enter the number of elment to be entered:->"))
a =[]
for i in range (0,n):
    elem=int(input(f"Please enter {i+1} element:->"))
    a.append(elem)
avg = sum(a)/2
print("The avrage of list is ",avg)