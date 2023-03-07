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




MIN_MERGE = 32
def calcMinRun(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertionSort(a, s, d):
    for i in range(s + 1, d + 1):
        j = i
        while j > s and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
 
def merge(a, l, m, r):
 
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(a[l + i])
    for i in range(0, len2):
        right.append(a[m + 1 + i])
 
    i, j, k = 0, 0, l
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
 
    while i < len1:
        a[k] = left[i]
        k += 1
        i += 1
    while j < len2:
        a[k] = right[j]
        k += 1
        j += 1
 
def timSort(a):
    n = len(a)
    minRun = calcMinRun(n)
 
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(a, start, end)
 
    size = minRun
    while size < n:
 
        
        for left in range(0, n, 2 * size):
 
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                merge(a, left, mid, right)
 
        size = 2 * size

startTime = time.time()
timSort(a)
endTime = time.time()


print("Tim sort when n=",len(a))
print("Durata executie algoritm:",endTime-startTime," secunde")