# ID успешной посылки = 84836997
# URL успешного отчета = https://contest.yandex.ru/contest/23390/run-report/84836997/

SIZE_LIMIT = 'Дек переполнен'
EMPTY = 'Элементы в Деке отсутсвуют'


class Deck:
    def __init__(self, max_size):
        self.queue = max_size * [None]
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def size_limit(self):
        return not(self.size != self.max_size)

    def push_back(self, value):
        if self.size_limit():
            raise IndexError(SIZE_LIMIT)
        self.queue[self.tail] = value
        self.tail = (self.tail - 1) % self.max_size
        self.size += 1

    def push_front(self, value):
        if self.size_limit():
            raise IndexError(SIZE_LIMIT)
        self.queue[self.head + 1] = value
        self.head = (self.head + 1) % self.max_size
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError(EMPTY)
        x = self.queue[self.tail + 1]
        self.queue[self.tail + 1] = None
        self.tail = (self.tail + 1) % self.max_size
        self.size -= 1
        return x

    def pop_front(self):
        if self.is_empty():
            raise IndexError(EMPTY)
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head - 1) % self.max_size
        self.size -= 1
        return x


def deck(total_commands, max_size):
    output = []
    deck_arr = Deck(max_size)
    commands_list = {
        'push_front': deck_arr.push_front,
        'push_back': deck_arr.push_back,
        'pop_front': deck_arr.pop_front,
        'pop_back': deck_arr.pop_back,
    }

    a = ['push_front 861', 'push_front -819', 'pop_back', 'pop_back']

    # for _ in range(total_commands):
    for _ in a:
        # commands = input()
        command, *value = _.split()
        if value:
            try:
                result = commands_list[command](int(*value))
                if result is not None:
                    output.append(result)
            except IndexError:
                output.append('error')
        else:
            try:
                result = commands_list[command]()
                output.append(result)
            except IndexError:
                output.append('error')
    for result in output:
        print(result)


if __name__ == '__main__':
    # total_commands = int(input())
    # deck_size = int(input())
    total_commands = 4
    deck_size = 4
    deck(total_commands, deck_size)