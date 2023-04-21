def bicycle(arr, cost_of_bicycle, left, days):
    if days <= left:
        return -1
    if arr[left] >= cost_of_bicycle:
        return left + 1
    mid = (left + days) // 2
    if arr[mid - 1] < cost_of_bicycle <= arr[mid]:
        return mid + 1
    elif cost_of_bicycle <= arr[mid]:
        return bicycle(arr, cost_of_bicycle, left, mid)
    else:
        return bicycle(arr, cost_of_bicycle, mid + 1, days)


if __name__ == '__main__':
    days = int(input())
    arr = [int(_) for _ in input().split()]
    cost_of_bicycle = int(input())
    print(bicycle(arr, cost_of_bicycle, 0, days),
          bicycle(arr, cost_of_bicycle * 2, 0, days)
          )
