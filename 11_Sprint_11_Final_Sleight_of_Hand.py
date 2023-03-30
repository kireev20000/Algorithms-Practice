# ID успешной посылки = 84851513
# URL успешного отчета = https://contest.yandex.ru/contest/23390/run-report/84851513/

def count_points(k, game_field):
    points = 0
    for i in range(1, 10):
        digits_count = int(game_field.count(str(i)))
        if digits_count == 0:
            continue
        elif digits_count <= (k*2):
            points += 1
    return points


if __name__ == '__main__':
    k = int(input())
    game_field = ''.join([input() for _ in range(4)])
    print(count_points(k, game_field))
