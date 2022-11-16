def same_set(a, b):
    for e in a:
        if e not in b:
            return False

    return True


print(same_set([1, 4, 9, 16, 9, 7, 4, 9, 11], [11, 11, 7, 9, 16, 4, 1]))
