MOBILE_NUMBER = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
}


def combinate(n, list_num=[], count=0, s=''):
    if count == len(n):
        list_num.append(s)
    else:
        num = int(n[count])
        for i in MOBILE_NUMBER[num]:
            combinate(n, list_num, count + 1, s + i)


if __name__ == '__main__':
    n = input()
    i = []
    combinate(n, i)
    print(*i)