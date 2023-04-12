# ID успешной посылки = 85649719
# URL успешного отчета = https://contest.yandex.ru/contest/23759/run-report/85649719/

class Stack:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        raise IndexError('ОШИБКА! Стек пуст!')


def calculator(input_data):
    stack = Stack()
    for i in input_data:
        if i not in "+, -, *, / ":
            stack.push(int(i))
            continue
        n1, n2 = stack.pop(), stack.pop()
        if i == "+":
            stack.push(n1 + n2)
        elif i == "-":
            stack.push(n1 - n2)
        elif i == "*":
            stack.push(n1 * n2)
        else:
            stack.push(n1 // n2)

    return stack.pop()


if __name__ == '__main__':
    input_data = '7 2 + 4 * 2 +'.split()
    print(calculator(input_data))
