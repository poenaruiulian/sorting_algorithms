#generate inputs with elements nearly ordered

import random

#n = int(input("Write the number of numbers you want to sort: "))
n = 1000000

with open("input.txt","w") as f:
    for i in range(n - n//4):
        f.write(str(i)+" ")
    for i in range(n-n//4,n):
        f.write(str(random.randint(n-n//4,n))+" ")