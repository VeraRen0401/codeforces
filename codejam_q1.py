def flip(arr, k, a):
    for i in range(a, a + k):
        arr[i] = not arr[i]
    return (arr)

t = int(input())
for i in range (1, t+1):
    a, k = [s for s in input().split(" ")]
    k = int(k)
    size = len(a)
    list = []
    count = 0
    for j in range(size):
        if a[j] == "+":
            list.append(True)
        else:
            list.append(False)
    for j in range(size - k + 1):
        if list[j] == False:
            flip(list, k, j)
            count += 1
    flag = True
    for j in range(size - k + 1, size):
        if list[j] == False:
            print("case #{}: IMPOSSIBLE".format(i))
            flag = False
            break
    if flag == True:
        print("case #{}: {}".format(i, count))


