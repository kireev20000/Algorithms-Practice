n = int(input())
s = int(input())
arr = list(map(int, input().split()))

if n >= 4:
    arr.sort()
    sum2 = {}
    for i in range(n - 1):
        for j in range(i + 1, n):
            s2 = arr[i] + arr[j]
            if s2 in sum2:
                sum2[s2].append([i, j])
            else:
                sum2[s2] = [[i, j]]

    res = []
    for s2 in sum2:
        x = s - s2
        if x in sum2:
            for l in sum2[s2]:
                for r in sum2[x]:
                    if r[0] > l[1]:
                        t = [arr[l[0]], arr[l[1]], arr[r[0]],
                             arr[r[1]]]
                        if t not in res:
                            res.append(t)
    res.sort()
    print(len(res))
    for el in res:
        print(*el)
    pass
else:
    print('0')