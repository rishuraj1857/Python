x = str(input("Please enter a word->"))
vow=[]
con=[]
for i in x:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        vow.append(i)
    else:
        con.append(i)
print(len(vow))
print(len(con))