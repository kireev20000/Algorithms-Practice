def calculation(lst, n):
    arr = []
    left = lst[0][0]
    right = lst[0][1]
    if n == 1:
        return print(*lst[0])
    for i in range(n):
        if right < lst[i][0]:
            arr.append([left, right])
            left = lst[i][0]
            right = lst[i][1]
        if lst[i][0] <= right <= lst[i][1]:
            right = lst[i][1]
    arr.append([left, right])
    arr.sort(key=lambda x: x[0])
    for sp in arr:
        print(*sp)


if __name__ == '__main__':
    n = int(input())
    flowerbed = []
    for i in range(n):
        flowerbed.append(list(int(_) for _ in input().split()))
    flowerbed.sort(key=lambda x: x[0])
    calculation(flowerbed, n)
