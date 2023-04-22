def triangle(b):
    for i in range(len(b) - 2):
        if b[i] < b[i + 1]+b[i + 2]:
            print(b[i] + b[i + 1] + b[i + 2])
            break
        else:
            i += 1

if __name__ == '__main__':
    a = int(input())
    b = sorted([int(_) for _ in input().split()], reverse=True)
    triangle(b)

