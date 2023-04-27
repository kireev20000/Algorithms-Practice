from random import shuffle


def get_hash(s):
    q, m = 1000, 123_987_123
    res = ord(s[0])
    for c in s[1:]:
        res = (res * q + ord(c)) % m
    return res


lst1 = list('ezhgeljkablzwnvuwqvp')
lst2 = list('gbpdcvkumyfxillgnqrv')
while True:
    shuffle(lst1)
    shuffle(lst2)
    s1, s2 = ''.join(lst1), ''.join(lst2)
    if get_hash(s1) == get_hash(s2):
        print(s1, s2, sep='\n')
        break