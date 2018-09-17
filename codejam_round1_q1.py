def str2arr(newline):
    size = len(newline)
    line = []
    for i in range(size):
        line.append(newline[i])
    return line

def readline(line, output, temp_list, case_no, r,  c):
    print(line, output, temp_list)
    leftover_size = len(temp_list)
    # i = 0
    # find = False
    letter, location = [], []
    temp_list.append(line)
    for j in range(c):
        if line[j] != "?":
            letter.append(line[j])
            location.append(j)
    # print(letter, location)
    size = len(location)
    if size > 0:
        for index in range(size - 1):
            for i in range(leftover_size + 1):
                j = location[index]
                while  j < c and j < location[index+1]:
                    temp_list[i][j] = letter[index]
                    j += 1
        for i in range(leftover_size + 1):
            for j in range(location[0]):
                temp_list[i][j] = letter[0]
            for j in range(location[size - 1], c):
                temp_list[i][j] = letter[size - 1]
        
        output.extend(temp_list)
        temp_list.clear()
    print(temp_list, output)
    return output

t = int(input())
for case_no in range(1, t+1):
    r, c = [int(s) for s in input().split(" ")]
    output = []
    temp_list = []

    for i in range(r):
        line = str2arr(input())
        readline(line, output, temp_list, case_no, r, c)
    # temp_list might still have info
    # merge them with the last row in output
    last_rows = len(temp_list)
    # print(temp_list)
    if last_rows > 0:
        for i in range(last_rows):
            for j in range(c):
                temp_list[i][j] = output[r - last_rows - 1][j]
        output.extend(temp_list)
    
    print("Case #{}:".format(case_no))
    for i in range(r):
        for j in range(c):
            print(output[i][j], end = '')
        print()