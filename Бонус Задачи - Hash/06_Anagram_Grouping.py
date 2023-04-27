def f_sort(s):
    l = list(s)
    l.sort()
    return ''.join(l)


n, i1 = int(input()), input().split()
dict_w = {}

for i, word in enumerate(i1):
    wordkey = f_sort(word)
    if wordkey not in dict_w.keys():
        dict_w[wordkey] = [i]
    else:
        dict_w[wordkey].append(i)

for key in dict_w.keys():
    print(*dict_w[key])
