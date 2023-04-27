first_string, second_string = [], []
first_string, second_string = str(input()), str(input())
M, N = len(first_string), len(second_string)
value = 0

if M == N:
    for i in range(1, M, 1):
        if ((first_string[i] == first_string[i-1] and second_string[i] != second_string[i-1])
                or (first_string[i] != first_string[i-1] and second_string[i] == second_string[i-1])):
            value = 1
            break
        print('YES') if value == 0 else print('NO')
    else:
        print('NO')