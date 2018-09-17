def num2arr(num):
    size = len(num)
    list = []
    for i in range(size):
        list.append(int(num[i]))
    return (list)

def arr2num(arr):
    size = len(arr)
    sum = 0
    for i in range(size):
        sum = arr[i] + 10 * sum
    return (sum)

t = int(input())
for i in range(1, t+1):
    num_str = input()
    size = len(num_str)
    num = num2arr(num_str)
    if size != 1: 
        j = 0
        while j < (size - 1) and num[j] <= num[j+1]:
            # print (j)
            j += 1
        if j != size - 1:
            test = j
            # print("changing point = {}".format(test))
            # print("{}, {}".format(num[test-1], num[test]))
            while test > 0 and num[test] == num[test-1]:
                test -= 1
                # print ("begining is {}".format(test))
            num[test] -= 1
            start = test + 1
            for k in range(start, size):
                num[k] = 9            
    print("case #{}: {}".format(i, arr2num(num)))