# ID успешной посылки = 84892773
# URL успешного отчета = https://contest.yandex.ru/contest/23390/run-report/84892773/

def count_points(k, game_field):
    points = 0
    appearance_of_digits = {'1': 0, '2': 0, '3': 0,
                            '4': 0, '5': 0, '6': 0,
                            '7': 0, '8': 0, '9': 0}
    for i in game_field:
        if i.isdigit():
            appearance_of_digits[i] += 1

    for value in appearance_of_digits.values():
        if value == 0:
            continue
        elif value <= k*2:
            points += 1
    return points


if __name__ == '__main__':
    #k = int(input())
    #game_field = ''.join([input() for _ in range(4)])
    k = 3
    game_field = '12312..22..22..2'
    # game_field = '1111999911119911'

    print(count_points(k, game_field))
