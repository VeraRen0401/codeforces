temp = [int(x) for x in input().split()]
target = temp[1]
size = temp[0]
numArray = [int(x) for x in input().split()]
numArray.sort()
mid = len(numArray) // 2
steps = 0

# print("mid ={} ".format(mid))
# print(numArray)

if numArray[mid] < target:
    index = mid
    while numArray[index] < target and index < size:
        steps += target - numArray[index]
        # print("index = {}, steps = {}".format(index, steps))
        index += 1
elif numArray[mid] > target:
    index = mid
    while numArray[index] > target and index > -1:
        steps += -target + numArray[index]
        index -= 1
print(steps)