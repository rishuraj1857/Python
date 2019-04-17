p = float(input("Plese enter the principal amount:=>"))
t = float(input("Please enter the time (In Years):=>"))
r = float(input("Please enter the rate:=>"))
si=0
si=(p*r*t)/100
print(f"The Intrest payable is {si} per annum.")
total= p+(si*t)
print(f"Total amount to be pay is {total}")