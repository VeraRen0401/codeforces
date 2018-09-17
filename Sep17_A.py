from math import ceil
n = int(input())
m = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

maxx = max(arr)
difference = maxx * n - sum(arr)
if difference >= m:
    smallest = maxx
else:
    smallest = ceil((m - difference)/n) + maxx
largest = maxx + m
print('{} {}'.format(smallest, largest))