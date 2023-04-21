def sequence(s, t):
    if len(s) == 0:
        return True
    count = - 1
    for i in s:
        count = t.find(i, count + 1)
        if count == - 1:
            return False
    return True


if __name__ == '__main__':
    s, t = input(), input()
    print(sequence(s, t))