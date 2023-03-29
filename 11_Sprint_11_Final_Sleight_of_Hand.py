# ID успешной посылки = 84815553
# URL успешного отчета = https://contest.yandex.ru/contest/23390/run-report/84815553/

def count_points():
    k = int(input())
    game_field = ''
    game_field = ''.join(map(str, [game_field + input() for x in range(4)]))
    #k = 3
    #game_field = '1111999911119911'
    #game_field = '12312..22..22..2'
    appearance_of_digits = []

    for i in range(1, 10):
        digits_count = game_field.count(str(i))
        appearance_of_digits.append(digits_count)

    points = 0
    for i, digit_quantity in enumerate(appearance_of_digits):
        if digit_quantity == 0:
            continue
        elif int(digit_quantity) <= (k*2):
            points += 1
    return points

print(count_points())
