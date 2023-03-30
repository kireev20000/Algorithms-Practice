# ID успешной посылки = 84836997
# URL успешного отчета = https://contest.yandex.ru/contest/23390/run-report/84836997/

def calculate_distance(street_length, house_numbers):
    distance = street_length
    result_list = [0] * street_length
    list_index = 0
    for n in house_numbers:
        if n == '0':
            distance = 0
        else:
            distance += 1
        result_list[list_index] = distance
        list_index += 1
    return result_list


if __name__ == '__main__':
    street_length = int(input())
    house_numbers = input().split()
    to_left = calculate_distance(street_length, house_numbers)
    to_right = reversed(calculate_distance(street_length, reversed(house_numbers)))
    print(*map(min, zip(to_left, to_right)))
