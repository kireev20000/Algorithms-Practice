string1, string2 = input(), input()

for i in range(len(string2)):
    letter = string2[i]
    if letter in string1:
        string1 = string1.replace(letter, '', 1)
    else:
        print(letter)

