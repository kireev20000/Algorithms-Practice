# ID успешной посылки = 84913377
# URL успешного отчета. = https://contest.yandex.ru/contest/23390/run-report/84913377/

def count_points(k, game_field):
    points = 0
    digits = {}
    for i in game_field:
        if i.isdigit():
            if int(i) in digits.keys():
                digits[int(i)] += 1
            else:
                digits[int(i)] = 1
    else:
        for value in digits.values():
            if 0 < value <= k*2:
                points += 1
    return points


if __name__ == '__main__':
    k = int(input())
    game_field = ''.join([input() for _ in range(4)])

    print(count_points(k, game_field))
