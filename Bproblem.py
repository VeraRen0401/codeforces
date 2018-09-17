n, k = [int(x) for x in input().split()]
remainder = n % (2*k+1)
if remainder == 0:
    step = n // (2*k+1)
else:
    step = n // (2*k+1) + 1
steplist = []
if remainder >= 1 and remainder <= k+1:
    for i in range(step - 1):
        steplist.append(1+i*(2*k+1))
    steplist.append(n-remainder+1)
elif remainder >= k+2 and remainder <= 2*k:
    for i in range(step - 1):
        steplist.append(k+1+i*(2*k+1))
    steplist.append(n+k+1-remainder)
elif remainder == 0:
    for i in range(step):
        steplist.append(k+1+i*(2*k+1))
print(step)
for elem in steplist:
    print(elem, end = ' ')
print()