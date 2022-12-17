def switch_first_last(v: list):
    temp = v[0]
    v[0] = v[-1]
    v[-1] = temp


def slide(v: list):
    v.insert(0, v.pop())


def change_pair(v: list):
    for i, e in enumerate(v):
        if e % 2 == 0:
            v[i] = 0


def change_max(v: list):
    for i in range(1, len(v) - 1):
        v[i] = max(v[i - 1], v[i + 1])


def remove_middle(v: list):
    i = (len(v) - 1)/2

    if i == int(i):
        v.pop(int(i))
    else:
        v.pop(int(i))
        v.pop(int(i))


def pair_first(v: list):
    v.sort(key= lambda e: e % 2 != 0)


def second_max(v: list):
    v.remove(max(v))
    return max(v)


def is_asc(v: list):
    return sorted(v) == v


def adjacent_pair(v: list):
    for i in range(len(v) - 1):
        if v[i] == v[i + 1]:
            return True

    return False


def contains_duplicate(v: list):
    for e in v:
        if v.count(e) > 1:
            return True

    return False


