def bracket_generation(count, prefix, left=0, right=0):
    if left == count and right == count:
        print(prefix)
    else:
        if left < count:
            bracket_generation(count, prefix + '(', left+1, right)
        if right < left:
            bracket_generation(count, prefix + ')', left, right+1)


def main():
    n = int(input())
    prefix = ''
    bracket_generation(n, prefix)


if __name__ == '__main__':
    main()
