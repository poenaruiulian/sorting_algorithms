import time
a = []

for x in range(100):
    with open("generators/input.txt","r") as f:
        r = f.readlines()
        for i in r: 
            row = i.split(" ")
            a += [int(j) for j in row if j !=""]

# with open("input.txt","r") as f:
#         r = f.readlines()
#         for i in r: 
#             row = i.split(" ")
#             a += [int(j) for j in row if j]

start = time.time()


count=dict()
n = len(a)

for i in range(0,n):
    count[i] = 0
         

for i in range(0,n):
    if a[i] in count.keys():
        count[a[i]] += 1
    else:
        count[a[i]] = 1
 
         
sortedArr = []
i = 0
while (n > 0):
    if (count[i] == 0):
        i += 1
    else:
        sortedArr.append(i)
        count[i] -= 1
        n = n - 1
         
    

a = sortedArr

end = time.time()

print("Insertion sort when n=",len(a))
print("Durata executie algoritm:",end-start," secunde")