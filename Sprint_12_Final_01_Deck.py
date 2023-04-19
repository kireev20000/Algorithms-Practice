# ID успешной посылки = 85703424
# URL успешного отчета = https://contest.yandex.ru/contest/23759/run-report/85703424/

Deck_is_Empty_MSG = 'ОШИБКА! Дека пуста!!'
Deck_Overflow_MSG = 'ОШИБКА! В деке больше нет места!!!'


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

    def _index_position(self, idx, add=False):
        idx = idx + 1 if add else idx - 1
        return idx % self.__max_n

    def push_back(self, value):
        if self._size_limit():
            raise DeckIsOverflow(Deck_Overflow_MSG)
        self.__queue[self.__tail] = value
        self.__tail = self._index_position(self.__tail, True)
        self.__size += 1

    def push_front(self, value):
        if self._size_limit():
            raise DeckIsOverflow(Deck_Overflow_MSG)
        self.__queue[self.__head - 1] = value
        self.__head = self._index_position(self.__head)
        self.__size += 1


    def pop_back(self):
        if self._is_empty():
            raise DeckIsEmpty(Deck_is_Empty_MSG)
        x = self.__queue[self.__tail - 1]
        self.__queue[self.__tail - 1] = None
        self.__tail = self._index_position(self.__tail)
        self.__size -= 1
        return x

    def pop_front(self):
        if self._is_empty():
            raise DeckIsEmpty(Deck_is_Empty_MSG)
        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self._index_position(self.__head, True)
        self.__size -= 1
        return x

def deck(total_commands, max_n):

    deck_arr = Deck(max_n)

    # a = ['push_front -201', 'push_back 959', 'push_back 102', 'push_front 20', 'pop_front', 'pop_back']
    #a = ['push_back -977', 'pop_back', 'pop_back', 'push_front -86', 'pop_back', 'push_back 81', 'pop_front', 'pop_back', 'pop_back']
    a = ['pop_back', 'pop_back', 'pop_back', 'pop_front', 'pop_back', 'pop_back', 'push_front 284',
         'pop_back', 'push_front 799', 'pop_front', 'pop_back', 'pop_back', 'pop_front', 'push_back 792',
         'push_front 45', 'push_front 374', 'pop_back', 'push_back 740', 'pop_front', 'pop_back', 'push_front 607',
         'push_front -492', 'push_back 661', 'push_front -551', 'pop_front']

    # for _ in range(total_commands):
    for _ in a:
        command, *value = _.split()
        try:
            result = getattr(deck_arr, command)(*value)
            if result is not None:
                print(result)
        except (DeckIsOverflow, DeckIsEmpty):
            print('error')


if __name__ == '__main__':
    # total_commands, deck_size = int(input()), int(input())
    total_commands, deck_size = 213, 34
    # total_commands, deck_size = 6, 6
    deck(total_commands, deck_size)

