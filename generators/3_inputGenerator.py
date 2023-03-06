#generates elements in reverse order

import random

#n = int(input("Write the number of numbers you want to sort: "))
n = 100000

with open("input.txt","w") as f:
    for i in range(n-1,-1,-1):
        f.write(str(i)+" ")
