class Stack:
    def __init__(self):
            self.items = []
    def if_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

line = list(input())
s = Stack()
d = {'(':')','{':'}','[':']'}


for x in line:
    if x in d.keys():
        s.push(x)
    elif not s.if_empty() and d[s.peek()] == x:
        s.pop()
    else:
        s.push(x)
        break

if s.if_empty():
    print('True')
else:
    print('False')