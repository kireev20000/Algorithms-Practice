class StackMaxEffective:

    def __init__(self):
        self.items = []
        self.max = []

    def if_empty(self):
        return self.items == []

    def get_max(self):
        if self.if_empty():
            return 'None'
        return self.max[len(self.items) - 1]

    def push(self, item):
        if len(self.items) == 0:
            self.max.append(int(item))
        elif int(item) > self.max[len(self.items) - 1]:
            self.max.append(int(item))
        else:
            self.max.append(self.max[len(self.items) - 1])
        self.items.append(item)



def pop(self):
    if self.if_empty():
        return 'error'
    self.max.pop()
    return self.items.pop()


n = int(input())
result = []
s = StackMaxEffective()

for i in range(n):
    command = input().split()
    if command[0] == 'push':
        s.push(command[1])
    if command[0] == 'pop':
        if pop(s) == 'error':
            result.append('error')
    if command[0] == 'get_max':
        result.append(s.get_max())

for i in result:
    print(i)
