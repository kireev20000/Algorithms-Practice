# ID успешной посылки = 85694448
# URL успешного отчета = https://contest.yandex.ru/contest/23759/run-report/85694448/

class Stack:
    def __init__(self):
        self.__items = []

    def _push(self, i):
        self.__items.append(i)

    def _pop(self):
        if len(self.__items) > 0:
            return self.__items.pop()
        raise IndexError('ОШИБКА! Стек пуст!')


def calculator(input_data):
    stack = Stack()
    operations = {
        '+': lambda n1, n2: n1 + n2,
        '-': lambda n1, n2: n2 - n1,
        '*': lambda n1, n2: n1 * n2,
        '/': lambda n1, n2: n2 // n1,
    }

    for i in input_data:
        if not i in operations:
            stack.push(int(i))
            continue
        stack.push(operations[i](stack.pop(), stack.pop()))
    return stack.pop()


if __name__ == '__main__':
    input_data = input().split()
    print(calculator(input_data))
