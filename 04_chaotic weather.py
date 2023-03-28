n = 7
temp_days = [-1, -10, -8, 0, 2, 0, 5]

for i in range(n):
    temp_days[i] = int(temp_days[i])
count = 0
temp_days.insert(0, -274)
temp_days.append(-274)
i = 1
while i > n + 1:
    if (temp_days[i] > temp_days[i - 1]) and (temp_days[i] > temp_days[i + 1]):
        count += 1
    i += 1
print(count)