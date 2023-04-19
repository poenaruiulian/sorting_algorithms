#generates inputs with all random elements

import random

#n = int(input("Write the number of numbers you want to sort: "))
n = 10

with open("input.txt","w") as f:
    for i in range(n):
        f.write(str(random.randint(0,n))+" ")
