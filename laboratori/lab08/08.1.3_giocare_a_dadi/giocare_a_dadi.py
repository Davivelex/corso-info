import random


def genera_lanci(n=20):
    lanci = []

    for _ in range(20):
        lanci.append(random.randint(1, 6))

    return lanci


def longest_sequence(v):
    current = [0, 0, v[0]]
    longest = [0, 0]

    for k in range(1, len(v)):
        if v[k] == current[2]:
            current[1] = k
        else:
            if abs(longest[1] - longest[0]) < abs(current[1] - current[0]):
                longest = [current[0], current[1]]

            current = [k, k, v[k]]

    if abs(longest[1] - longest[0]) < abs(current[1] - current[0]):
        longest = [current[0], current[1]]

    return longest


def main():
    lanci = genera_lanci()
    longest = longest_sequence(lanci)
    print(' '.join([str(x) for x in lanci[:longest[0]]]),
          f'({" ".join([str(x) for x in lanci[longest[0]:longest[1] + 1]])})',
          ' '.join([str(x) for x in lanci[1 + longest[1]:]]))


if __name__ == '__main__':
    main()
