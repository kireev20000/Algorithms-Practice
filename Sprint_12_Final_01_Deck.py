# ID успешной посылки = 85645716
# URL успешного отчета = https://contest.yandex.ru/contest/23759/run-report/85645716/

Deck_is_Empty_MSG = 'ОШИБКА! Дека пуста!'
Deck_Overflow_MSG = 'ОШИБКА! В деке больше нет места!'


class Deck:
    def __init__(self, max_n):
        self.queue = max_n * [None]
        self.max_n = max_n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def size_limit(self):
        return not(self.size != self.max_n)

    def push_back(self, value):
        if self.size_limit():
            raise IndexError(Deck_Overflow_MSG)
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def push_front(self, value):
        if self.size_limit():
            raise IndexError(Deck_Overflow_MSG)
        self.queue[self.head - 1] = value
        self.head = (self.head - 1) % self.max_n
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError(Deck_is_Empty_MSG)
        x = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return x

    def pop_front(self):
        if self.is_empty():
            raise IndexError(Deck_is_Empty_MSG)
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


def deck(total_commands, max_n):

    deck_arr = Deck(max_n)
    commands_list = {
        'push_front': deck_arr.push_front,
        'push_back': deck_arr.push_back,
        'pop_front': deck_arr.pop_front,
        'pop_back': deck_arr.pop_back,
    }

    # a = ['push_front 861', 'push_front -819', 'pop_back', 'pop_back']
    result_list = []
    for _ in range(total_commands):
        command, *value = input().split()
        if value:
            try:
                result = commands_list[command](int(*value))
                if result is not None:
                    result_list.append(result)
            except IndexError:
                result_list.append('error')
        else:
            try:
                result = commands_list[command]()
                result_list.append(result)
            except IndexError:
                result_list.append('error')

    print(*result_list, sep="\n")


if __name__ == '__main__':
    total_commands, deck_size = int(input()), int(input())
    deck(total_commands, deck_size)
