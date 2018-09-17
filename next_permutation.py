def swapIndex(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def reverse(arr,a,b):
    for i in range((b-a)//2+1):
        swapIndex(arr, a+i, b-i)
    
def next_permutation(arr):
    # 在这里回答吧 mua~
    if not arr:
        # Empty arr!
        # len(arr) - 1 will be -ve!!!!!!!
        return False
    size = len(arr)
    i = size - 2
    while arr[i] > arr[i + 1]:
        i -= 1
    # arr[i] < arr[i+1]
    # arr[i+1] > arr[i+2] > ... > arr[size-1] 
    if i == -1:
        return False
    else:
        if arr[i] > arr[size - 1]:
            next_index = i + 1
            before_index = size - 1
            mid = (next_index + before_index) // 2
            while next_index + 1 != before_index:
                if arr[mid] > arr[i]:
                    next_index = mid
                else:
                    before_index = mid
                mid = (next_index + before_index) // 2
        else:
            next_index = size - 1
        swapIndex(arr, i, next_index)
        reverse(arr, i + 1, size - 1)
        return True

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)    

arr = [1, 2, 3, 4]

# num = factorial(len(arr))
# for i in range(num):
#     print(arr)
#     next_permutation(arr)

# Bonus: return False if arr is changed from the last permutation to first permutation;
# return True otherwise
# The benefit is that you don't have to start from the first permutation
# and you can write the loop like this:
count = 0
while True:
    count += 1
    print(arr)
    if not next_permutation(arr):
        break
print(count)


##############################################################################
# 答案在这里
# 没做出来不要看了啦
# 人家会害羞的啦
# 嘤嘤嘤
##############################################################################



def next_permutation_answer(arr):
    if not arr:
        # Empty arr!
        # len(arr) - 1 will be -ve!!!!!!!
        return False
    peakPtr = len(arr) - 1
    while (peakPtr > 0):
        if arr[peakPtr - 1] < arr[peakPtr]:
            break
        peakPtr -= 1
    reverse(arr, peakPtr, len(arr) - 1)
    prePeak = peakPtr - 1
    if prePeak < 0:
        return False
    # In the reversed part, 
    # find the smallest element that is larger than prePeak
    # then swap it with prePeak
    for i in range(peakPtr, len(arr)):
        if arr[prePeak] < arr[i]:
            swapIndex(arr, prePeak, i)
            return True
