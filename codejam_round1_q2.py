import math
total_cases = int(input())
for case_no in range(1, total_cases + 1):
    n, m = [int(s) for s in input().split(" ")]
    standard = [int(s) for s in input().split(" ")]
    # standard = [k1, k2, k3,..,kn] the proportion of different ingredients
    a = []
    for i in range(n):
        list_ = [int(s) for s in input().split(" ")]
        list_.sort()
        a.append(list_)
    count = 0
    for first_elem in range(m):
        start = math.ceil( a[0][first_elem] / ( 1.1 * standard[0] ) )
        end = math.floor( a[0][first_elem] / ( 0.9 * standard[0] ) )
        recipe = [a[0][first_elem]]
        for scalar in range( start, end + 1):
            NewStardard = [scalar * s for s in standard]
            print("newstandard", NewStardard)
            for index in range(1, n):
                find = False
                print(index)
                for j in range( len( a[index] ) ):
                    print(index, j, a[index][j], NewStardard[index])
                    if a[index][j] >= 0.9 * NewStardard[index] and a[index][j] <= 1.1 * NewStardard[index]:
                        # recipe.append(a[index][j])
                        poped_elem = a[index].pop(j)
                        recipe.append(poped_elem)
                        print(poped_elem, a)
                        find = True
                        break
                if find == False:
                    break
            if len(recipe) == n:
                count += 1
                break
        # print(a)
        # print (recipe)
        # print (count)
    print("Case #{}: {}".format(case_no, count))

    