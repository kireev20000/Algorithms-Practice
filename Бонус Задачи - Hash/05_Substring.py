def substring(s):
    max_s = ''
    max_count = 0
    count = 0
    begin, end = 0, len(s)-1

    while begin <= end:
        if s[begin] not in max_s:
            max_s += s[begin]
            count += 1
        else:
            max_s = max_s[max_s.index(s[begin])+1:] + s[begin]
            count = len(max_s)

        if count > max_count:
            max_count = count

        begin += 1

    return max_count


if __name__ == '__main__':
    print(substring(input()))
