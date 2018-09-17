# construct a segment tree
# update a value
# query a sum
import math

def calMid(ss, se):
    return ss + (se - ss)//2

def construct(arr):
    height = math.floor(math.log2(len(arr)))+1
    size = pow(2,height)-1
    st = [0]*size
    constructUtil(arr,st,0,len(arr)-1,0)
    return st

def constructUtil(arr,st,ss,se,si):
    if ss == se:
        st[si] = arr[ss]
        print(st)
        return st[si]
    mid = calMid(ss, se)
    print('ss',ss,'se',se)
    st[si] = constructUtil(arr,st,ss,mid,2*si+1) + constructUtil(arr,st,mid+1,se,2*si+2)
    return st[si]


arr = [2,4, 1,3]
st = construct(arr)
print(st)
# def main(arr):
#     # construct a new segment tree
#     st = construct(arr)
#     # query a sum
#     partialSum = partialSum(st, qs, qe)
#     # update a value
#     Newst = update(st, arr, i, value)
