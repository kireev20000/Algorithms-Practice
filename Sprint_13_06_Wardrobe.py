def wardrobe(wardrobe):
    pink = []
    yellow = []
    raspberry = []
    for _ in wardrobe:
        if _ == '0':
            pink.append(_)
        elif _ == '1':
            yellow.append(_)
        else:
            raspberry.append(_)
    result_hanger = pink + yellow + raspberry
    print(*result_hanger)


if __name__ == '__main__':
    count = int(input())
    wardrobe(input().split())
