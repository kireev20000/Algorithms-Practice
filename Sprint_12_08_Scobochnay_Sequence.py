# классная статья про это - https://medium.com/@vitkarpov/%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D1%81%D0%BA%D0%BE%D0%B1%D0%BE%D1%87%D0%BD%D0%B0%D1%8F-%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C-98699eebd5ac
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
dict_examples = {'(': ')', '{': '}', '[': ']'}

for x in line:
    if x in dict_examples.keys():
        s.push(x)
    elif not s.if_empty() and dict_examples[s.peek()] == x:
        s.pop()
    else:
        s.push(x)
        break

if s.if_empty():
    print('True')
else:
    print('False')
