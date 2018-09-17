import math
n = int(input())
mapping = {
    'BA':'AB',
    'CA':'AC',
    'CB':'BC',
    'ACB':'ABC',
    'BAC':'ABC',
    'BCA':'ABC',
    'CAB':'ABC',
    'CBA':'ABC',
}
dic = {}
for i in range(n):
    c,s=input().split()
    c = int(c)
    s = mapping[s] if s in mapping else s    
    dic[s] = min(dic[s],c) if s in dic else c

total = ['A','B','C','AB','AC','BC','ABC']
for s in total:
    if s not in dic:
        dic[s] = math.inf

s = min(dic['ABC'],dic['AB']+dic['C'], dic['AC']+dic['B'], dic['BC']+dic['A'],dic['AB']+dic['AC'], dic['AC']+dic['BC'], dic['BC']+dic['AB'], dic['A']+dic['B']+dic['C'])
s = -1 if s == math.inf else s
print(s)