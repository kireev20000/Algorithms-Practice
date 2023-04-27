n = int(input())
if n >= 2:
    iData = input().split()
    arr = {}
    arr[0] = [-1, 0]
    temp_sum = 0
    for i in range(n):
        temp_sum += 1 if iData[i] == '1' else -1
        if temp_sum not in arr.keys():
            arr[temp_sum] = [i, 0]
        else:
            arr[temp_sum][1] = i
    Lengt_max = arr[0][1] - arr[0][0]
    for el in arr.values():
        if Lengt_max < el[1] - el[0]:
            Lengt_max = el[1] - el[0]
    if Lengt_max == 1:
        print(0)
    else:
        print(Lengt_max)
    pass
else:
    print(0)