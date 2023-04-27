def Hash(i1, i2, i3) -> int:
    if len(i3) == 0:
        return 0
    else:
        h = ord(i3[0])
        for i in range(1, len(i3)):
            h = (h * i1) % i2 + ord(i3[i])
        return h % i2


i1 = int(input())
i2 = int(input())
i3 = input()
print(Hash(i1, i2, i3))