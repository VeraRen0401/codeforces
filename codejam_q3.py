def f( N, people, dic ):
    if (N, people) in dic:
        return dic[(N, people)]
    left =  ( N - 1 ) // 2 
    right = N - 1 - left
    if people == 1:
        dic[(N, people)] = [right, left]
        return ([right, left])
    if people == 2:
        temp = f(right, 1, dic)
        dic[(N,2)] = temp
        return temp

    left_people =  (people - 1 ) // 2
    right_people = people - left_people - 1
    list1 = f(left, left_people, dic)
    list2 = f( right, right_people, dic )
    if list1 < list2:
        dic[(N,people)] = list1
        return list1
    else:
        dic[(N, people)] = list2
        return list2

dic = {}
test_no = int(input())
for i in range(1, test_no + 1):
    N, people = [int(s) for s in  input().split(" ")]
    # print("N = {}, people = {}".format(N, people))
    arr = [N]
    maxx, minn = f(N, people, dic)
    # print (space)
    # location = int(space / 2 + 0.5)
    # maxx = space - location
    # minn = space - location - 1
    print("Case #{}: {} {}".format(i, maxx, minn))
# print (dic)