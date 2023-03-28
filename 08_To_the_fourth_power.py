while True:
    n = int(input())
    if n == 1:
        print('True')
        break
    n = n / 4
    if (n % 4 > 0 and n != 1):
        print('False')
        break
    print('True')
    break

# Вариант 2
from math import log

n = int(input())

Logn = log(n, 4)
if (Logn == int(Logn)):
  print("True")
else:
  print("False")