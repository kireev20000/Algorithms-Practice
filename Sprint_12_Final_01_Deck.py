# ID успешной посылки = 85645716
# URL успешного отчета = https://contest.yandex.ru/contest/23759/run-report/85645716/

Deck_is_Empty_MSG = 'ОШИБКА! Дека пуста!'
Deck_Overflow_MSG = 'ОШИБКА! В деке больше нет места!'


class DeckIsEmpty(Exception):
    pass


class DeckIsOverflow(Exception):
    pass


class Deck:
    def __init__(self, max_n):
        self.__queue = max_n * [None]
        self.__max_n = max_n
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def _is_empty(self):
        return self.__size == 0

    def _size_limit(self):
        return self.__size == self.__max_n

    def _index_position(self, index, value):
        if value == 1:
            return (index + value) % self.__max_n
        else:
            return (index - 1 + self.__max_n) % self.__max_n

    def push_back(self, value):
        if self._size_limit():
            raise DeckIsOverflow(Deck_Overflow_MSG)
        self.__queue[self.__tail] = value
        self.__tail = self._index_position(self.__tail, +1)
        # self.__tail = (self.__tail + 1) % self.__max_n
        self.__size += 1

    def push_front(self, value):
        if self._size_limit():
            raise DeckIsOverflow(Deck_Overflow_MSG)
        self.__queue[self.__head - 1] = value
        # self.__head = (self.__head - 1) % self.__max_n
        self.__head = self._index_position(self.__head, -1)
        self.__size += 1


    def pop_back(self):
        if self._is_empty():
            raise DeckIsEmpty(Deck_is_Empty_MSG)
        x = self.__queue[self.__tail - 1]
        self.__queue[self.__tail - 1] = None
        # self.__tail = (self.__tail - 1) % self.__max_n
        self.__tail = self._index_position(self.__tail, -1)
        self.__size -= 1
        return x

    def pop_front(self):
        if self._is_empty():
            raise DeckIsEmpty(Deck_is_Empty_MSG)
        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_n
        self.__head = self._index_position(self.__head, +1)
        # self.head = (self.head + 1) % self.max_n
        self.__size -= 1
        return x


def deck(total_commands, max_n):

    deck_arr = Deck(max_n)
    commands_list = {
        'push_front': deck_arr.push_front,
        'push_back': deck_arr.push_back,
        'pop_front': deck_arr.pop_front,
        'pop_back': deck_arr.pop_back,
    }

    # a = ['push_front -201', 'push_back 959', 'push_back 102', 'push_front 20', 'pop_front', 'pop_back']
    a = ['push_back -977', 'pop_back', 'pop_back', 'push_front -86', 'pop_back', 'push_back 81', 'pop_front',
         'pop_back', 'pop_back']
    result_list = []
    # for _ in range(total_commands):
    for _ in a:
        # command, *value = input().split()
        command, *value = _.split()
        if value:
            try:
                result = commands_list[command](int(*value))
                if result is not None:
                    result_list.append(result)
            except (DeckIsOverflow, DeckIsEmpty):
                result_list.append('error')
        else:
            try:
                result = commands_list[command]()
                result_list.append(result)
            except (DeckIsOverflow, DeckIsEmpty):
                result_list.append('error')

    print(*result_list, sep="\n")


if __name__ == '__main__':
    # total_commands, deck_size = int(input()), int(input())
    total_commands, deck_size = 6, 6
    # total_commands, deck_size = 6, 6
    deck(total_commands, deck_size)

