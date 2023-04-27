n = int(input())
result = {}
for i in range(n):
    s = input()
    if s not in result.keys():
        result[s] = 1
for key in result.keys():
    print(key)