n = int(input())
string = input().split()

result = max(string, key=len)
print(result, len(result), end='\n')