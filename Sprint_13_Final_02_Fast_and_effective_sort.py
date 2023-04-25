# ID успешной посылки =
# URL успешного отчета =

def fast_effective_sort(arr, left, right):
    if right <= left:
        return
    l_index, r_index = left, right
    pivot = arr[(left + right) // 2]
    while l_index <= r_index:
        while pivot > arr[l_index]:
            l_index += 1
        while pivot < arr[r_index]:
            r_index -= 1
        if l_index <= r_index:
            arr[l_index], arr[r_index] = arr[r_index], arr[l_index]
            l_index += 1
            r_index -= 1

    fast_effective_sort(arr, left, r_index)
    fast_effective_sort(arr, l_index, right)

if __name__ == '__main__':
    array = [(-4, 100, 'alla'), (-6, 1000, 'gena'), (-2, 90, 'gosha'), (-2, 90, 'rita'), (-4, 80, 'timofey')]
    # n_of_people = int(input())
    #array = [(-int(s_tasks), int(shtraf), name) for _ in range(n_of_people) for name, s_tasks, shtraf in [input().split()]]

    fast_effective_sort(array, 0, len(array) - 1)
    print(*(name for _, _, name in array), sep="\n")
