def greedy_child(factor, size):
    happy_child = 0
    for i in range(len(factor)):
        if size and factor[i] <= size[-1]:
            size.pop()
            happy_child += 1
    return print(happy_child)


if __name__ == '__main__':
    child_num = int(input())
    factor_of_greed = sorted(list(map(int, input().split())), reverse=True)
    m_of_cookies = int(input())
    size_of_cookies = sorted(list(map(int, input().split())))
    greedy_child(factor_of_greed, size_of_cookies)

