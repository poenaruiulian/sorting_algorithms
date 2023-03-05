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

for i in range(len(a)-1):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            aux = a[i]
            a[i] = a[j]
            a[j] = aux
            count+=1
        k+=1
    
end = time.time()

print("Bubble sort when n=",len(a))
print("Durata executie algoritm:",end-start," secunde")
print("Op dominanta: ",k," Intrare in if: ",count)