import time
import sys

a = []

for x in range(100):
    with open("input.txt","r") as f:
        r = f.readlines()
        for i in r: 
            row = i.split(" ")
            a += [int(j) for j in row if j !=""]
# with open("input.txt","r") as f:
#     r = f.readlines()
#     for i in r: 
#         row = i.split(" ")
#         a += [int(j) for j in row if j !=""]

def partitionare(a, s, d):
 
    p = a[d]
    i = s - 1

    for j in range(s, d):
        if a[j] <= p:
            i = i + 1
            (a[i], a[j]) = (a[j], a[i])
    (a[i + 1], a[d]) = (a[d], a[i + 1])
    return i + 1
def quick_sort(a, s, d):
    if s < d:
        pi = partitionare(a, s, d)
        quick_sort(a, s, pi - 1)
        quick_sort(a, pi + 1, d)

start = time.time()
quick_sort(a,0,len(a)-1)
end = time.time()

print("Quick sort when n=",len(a))
print("Durata executie algoritm:",end-start," secunde")