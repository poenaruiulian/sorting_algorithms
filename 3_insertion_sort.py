import time
a = []

with open("input.txt","r") as f:
    r = f.readlines()
    for i in r: 
        row = i.split(" ")
        a += [int(j) for j in row if j !=""]


start = time.time()

for i in range(1,len(a)):
    k = a[i]
    j = i-1
    while j>=0 and k<a[j]:
        a[j+1]=a[j]
        j-=1
    a[j+1]=k
 
end = time.time()

print("Insertion sort when n=",len(a))
print("Durata executie algoritm:",end-start," secunde")
