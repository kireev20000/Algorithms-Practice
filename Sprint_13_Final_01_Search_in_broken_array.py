# ID успешной посылки =
# URL успешного отчета =

def broken_search(arr, obj):
    left, right = 0, len(arr)-1
    if arr[right] == obj:
        return right
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == obj:
            return middle
        elif arr[left] <= arr[middle]:
            if arr[left] <= obj < arr[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if arr[middle] < obj <= arr[right]:
                left = middle + 1
            else:
                right = middle - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6

if __name__ == '__main__':
    test()
