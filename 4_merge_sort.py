import time
a = []


for x in range(100):
    with open("input.txt","r") as f:
        r = f.readlines()
        for i in r: 
            row = i.split(" ")
            a += [int(j) for j in row if j !=""]

# with open("input.txt","r") as f:
#         r = f.readlines()
#         for i in r: 
#             row = i.split(" ")
#             a += [int(j) for j in row if j]

def mergeSort(a):
    if len(a) > 1:
  

        mij = len(a)//2
  
        stanga = a[:mij]
        dreapta = a[mij:]
  

        mergeSort(stanga)
        mergeSort(dreapta)
  
        i = j = k = 0
        while i < len(stanga) and j < len(dreapta):
            if stanga[i] <= dreapta[j]:
                a[k] = stanga[i]
                i += 1
            else:
                a[k] = dreapta[j]
                j += 1
            k += 1
  

        while i < len(stanga):
            a[k] = stanga[i]
            i += 1
            k += 1
  
        while j < len(dreapta):
            a[k] = dreapta[j]
            j += 1
            k += 1
  
start = time.time()
mergeSort(a)
end = time.time()

print("Merge sort when n=",len(a))
print("Durata executie algoritm:",end-start," secunde")
