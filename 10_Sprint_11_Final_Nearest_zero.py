# ID успешной посылки = 84809972
# URL успешного отчета = https://contest.yandex.ru/contest/23390/run-report/84809972/

street_length = int(input())
house_numbers = input().split()

def calculate_distance(street_length, house_numbers):
    distance = street_length
    result_list = []
    for n in house_numbers:
        if n == '0':
            distance = 0
        else:
            distance += 1
        result_list.append(distance)
    return result_list


to_left = calculate_distance(street_length, house_numbers)
to_right = reversed(calculate_distance(street_length, reversed(house_numbers)))

print(*map(min, zip(to_left, to_right)))