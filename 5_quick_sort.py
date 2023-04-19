import time
import sys

a = []

# for x in range(100):
#     with open("generators/input.txt", "r") as f:
#         r = f.readlines()
#         for i in r:
#             row = i.split(" ")
#             a += [int(j) for j in row if j != ""]


with open("generators/input.txt","r") as f:
    r = f.readlines()
    for i in r:
        row = i.split(" ")
        a += [int(j) for j in row if j !=""]

def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]

    for j in range(l, h):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)

def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        p = partition(arr, l, h)

        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

n = len(a)
start = time.time()
quickSortIterative(a, 0, n - 1)
end = time.time()
print("Quicksort sort when n=",len(a))
print("Durata executie algoritm:",end-start," secunde")
