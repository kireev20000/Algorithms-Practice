def bubble_sort(n, arr):
    flag = True
    for i in range(n - 1):
        change_flag = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                change_flag = True
                flag = False
        if change_flag:
            print(*arr)
    if flag:
        print(*arr)


if __name__ == '__main__':
    num = int(input())
    mas = [int(_) for _ in input().split()]
    bubble_sort(num, mas)
