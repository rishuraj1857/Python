def sum2(*args):
    total=0
    for num in args:
        total+=num
        return total



print(sum2(45,31,151,8,56,87,154))
print(sum2(45,78))