import time
a = []

with open("input.txt","r") as f:
        r = f.readlines()
        for i in r: 
            row = i.split(" ")
            a += [int(j) for j in row if j]


startTime = time.time()

n = len(a)
swapped = True
start = 0
end = n-1

while(swapped):
      
    swapped = False
    for i in range(start, end):
        if (a[i] > a[i + 1]):
            a[i], a[i + 1] = a[i + 1], a[i]
            swapped = True
    if not swapped: break

    swapped = False
    end -= 1
    for i in range(end-1, start-1, -1):
        if (a[i] > a[i + 1]):
            a[i], a[i + 1] = a[i + 1], a[i]
            swapped = True
    start += 1
    

endTime = time.time()

print("Cocktail sort when n=",len(a))
print("Durata executie algoritm:",endTime-startTime," secunde")