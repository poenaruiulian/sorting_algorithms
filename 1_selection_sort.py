import time
a = []

with open("input.txt","r") as f:
    r = f.readlines()
    for i in r: 
        row = i.split(" ")
        a += [int(j) for j in row if j !=""]


start = time.time()
count = 0
k = 0  

for i in range(len(a)):
    pozMin = i
    for j in range(i+1,len(a)):
        if a[pozMin] > a[j]:
            pozMin = j
            count+=1
        k+=1
    aux = a[i]
    a[i] = a[pozMin]
    a[pozMin] = aux
    
end = time.time()

print("Selection sort when n=",len(a))
print("Durata executie algoritm:",end-start," secunde ")
print("Op dominanta: ",k," Intrare in if: ",count)