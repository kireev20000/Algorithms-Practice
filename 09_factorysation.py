n = int(input())
n2 = 2
while n2 ** 2 <= n:
    if n % n2 == 0:
        print(n2, end=' ')
        n //= n2
    else:
        n2 += 1
else:
    if n > 1:
        print(n)
