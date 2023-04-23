# ID успешной посылки =
# URL успешного отчета =

def fast_effective_sort(players):
    if len(players) <= 1:
        return players
    mid = players[len(players) // 2]
    r_nums = []
    l_nums = []
    m_nums = []
    for i in players:
        if i[1] > mid[1]:
            r_nums.append(i)
        elif i[1] < mid[1]:
            l_nums.append(i)
        else:
            if i[0] == mid[0]:
                m_nums.append(i)
            elif i[2] != mid[2]:
                r_nums.append(i) if i[2] < mid[2] else l_nums.append(i)
            else:
                r_nums.append(i) if i[0] < mid[0] else l_nums.append(i)
    return fast_effective_sort(r_nums) + m_nums + fast_effective_sort(l_nums)


if __name__ == '__main__':
    #number_of_people = int(input())
    arr2 = ['alla 4 100', 'gena 6 1000', 'gosha 2 90', 'rita 2 90', 'timofey 4 80']
    #array = [[(int(y) if y.isdigit() else y) for y in input().split()] for _ in range(number_of_people)]
    array = [[(int(y) if y.isdigit() else y) for y in _.split()] for _ in arr2]
    # quick_sort(array, 0, len(array)-1)
    # print_results(array)
    result = fast_effective_sort(array)
    players_sort = [i[0] for i in result]
    print(*players_sort, sep='\n')
