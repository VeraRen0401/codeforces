n, white, black = [int(x) for x in input().split()]
array = [int(x) for x in input().split()]
mid = (n-1)//2
cost = 0
if white < black:
    min = white
else:
    min = black
#take special care of mid
for i in range(mid):
    if (array[i], array[n-1-i]) == (1, 0) or (array[i], array[n-1-i]) == (0, 1):
        cost = -1
        break
    elif (array[i], array[n-1-i]) == (2, 2):
        cost += 2 * min
    elif (array[i], array[n-1-i]) == (2, 1) or (array[i], array[n-1-i]) == (1, 2):
        cost += black
    elif (array[i], array[n-1-i]) == (2, 0) or (array[i], array[n-1-i]) == (0, 2):
        cost += white

if n%2 == 1 and cost != -1:
    if array[mid] == 2:
        cost += min

if n%2 == 0:
    i = mid
    if cost != -1:
        if (array[i], array[n-1-i]) == (1, 0) or (array[i], array[n-1-i]) == (0, 1):
            cost = -1
        elif (array[i], array[n-1-i]) == (2, 2):
            cost += 2 * min
        elif (array[i], array[n-1-i]) == (2, 1) or (array[i], array[n-1-i]) == (1, 2):
            cost += black
        elif (array[i], array[n-1-i]) == (2, 0) or (array[i], array[n-1-i]) == (0, 2):
            cost += white   

print(cost)