def compare_number(n1, n2):  # функция-компаратор
    return n1 > n2

def biggest_number(arr, less):
    for i in range(1, len(arr)):
        item_to_sort = arr[i]
        j = i
        while j > 0 and less(
                item_to_sort + arr[j-1],
                arr[j-1] + item_to_sort
                ):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    print(''.join(arr))


if __name__ == '__main__':
    n = int(input())
    string = input().split()
    biggest_number(string, compare_number)
