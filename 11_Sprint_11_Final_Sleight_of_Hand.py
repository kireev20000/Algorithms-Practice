# ID успешной посылки = 84893824
# URL успешного отчета = https://contest.yandex.ru/contest/23390/run-report/84893824/

def count_points(k, game_field):
    points = 0
    appearance_of_digits = {_: 0 for _ in range(1, 10)}
    for i in game_field:
        if i.isdigit():
            appearance_of_digits[int(i)] += 1

    for value in appearance_of_digits.values():
        if value == 0:
            continue
        elif value <= k*2:
            points += 1
    return points


if __name__ == '__main__':
    k = int(input())
    game_field = ''.join([input() for _ in range(4)])

    print(count_points(k, game_field))
