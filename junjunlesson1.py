# list1 = [0,1]
# def fib(n):
#     if n < len(list1):
#         return list1[n]
#     else:
#         list1.append(fib(n-1)+fib(n-2))
#         return list1[n]

# print(fib(10))
# print(list1)

# def fib2(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         temp = a+b
#         a = b
#         b = temp
#     return a
# print(fib2(10))

from math import sqrt
def fib3(n):
    # n is a natural number

    a1 = ((1+sqrt(5))/2)**n
    # a2 = ((1-sqrt(5))/2)**n
    # print('a1 =', a1, 'a2 =', a2)
    # print('a1 = {}, a2 = {}'.format(a1, a2))
    return int(a1/sqrt(5)+0.5)

for i in range(1,21):
    print(fib3(i))

