import math
import os
import random
import re
import sys


def swap(arr, i, j, counter):
    counter[arr[i]-1] += 1
    counter[arr[j]-1] += 1
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp 
    return arr

def find(arr, start, end, num):
    for i in range(start, end):
        if arr[i] == num:
            return i
    return -1

# Complete the minimumBribes function below.
def minimumBribes(q):
    n = len(q)
    original = list(range(1, n + 1))
    counter = [0 for s in range(n)]
    num = n
    while num > 0:
        pos = find(q, 0, num, num)
        if pos == -1:
            print("error!")
            return -1
        if num - pos > 3: 
            return("Too chaotic")
        if num - pos == 2:
            swap(q, num - 2, num-1, counter)
            if counter[num -2] > 2:
                return("Too chaotic")
            if counter[num - 1] > 2:
                return("Too chaotic")
        if num - pos == 3:
            swap(q, num - 3, num-2, counter)
            swap(q, num - 1, num-2, counter)
            if counter[num - 3] > 2:
                return("Too chaotic")
            if counter[num - 2] > 2:
                return("Too chaotic")
            if counter[num - 1] > 2:
                return("Too chaotic")
        num -= 1
    sumCounter = 0
    for i in range(n):
        sumCounter += counter[i]
    return sumCounter // 2

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
    

