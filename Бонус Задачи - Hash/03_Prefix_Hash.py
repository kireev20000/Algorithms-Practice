def prefix_hash(i1, i2, i3):

    temp = [0] * (len(i3) + 1)
    for i in range(len(i3)):
        temp[i + 1] = (temp[i] * i1) % i2 + ord(i3[i])

    t = int(input())
    for i in range(t):
        lb, rb = list(map(int, input().split()))
        t_len = rb - lb + 1
        calcHash = (temp[rb] - temp[lb - 1] * pow(i1, t_len, i2)) % i2
        print(calcHash)


if __name__ == '__main__':
    i1, i2, i3 = int(input()), int(input()), input()
    prefix_hash(i1, i2, i3)
