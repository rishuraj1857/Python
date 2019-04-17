list1 = []
list2 = []
c = []
x = int(input("Please enter The limit for list :=>"))
for i in range(1,x+1):
    elem=(int(input(f"PLease enter {i} element for 1st list:=>")))
    list1.append(elem)
y = int(input("Please enter the limit for List 2:=>"))
for i in range(1,y+1):
    apple=int(input(f"PLease enter {i} element for 2nd list:=>"))
    list2.append(apple)
new = list1+list2
new.sort()
print(new)