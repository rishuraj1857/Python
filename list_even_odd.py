a = []
x = int(input("Please enter a range->"))
for i in range(1,x+1):
    elem=int(input(f"Please enter {i} number->"))
    a.append(elem)
even= []
odd = []
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"Even numbers are {even}")
print(f"Odd numbers are {odd}")