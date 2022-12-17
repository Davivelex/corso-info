ALPHA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z']

def ceaser(string):
    string = string.upper()
    to_add = ALPHA.copy()
    text = []

    for element in string:
        if element in to_add:
            text.append(element)
            to_add.remove(element)

    text += to_add

    if len(text) % 2 != 0:
        text += 'Z'

    return text


def matrix(key_text):
    key = []

    for i in range(0, 5):
        key.append(key_text[i * 5:(i + 1)*5])

    return key


def pos(key, element):
    for i in range(5):
        for j in range(5):
            if key[i][j] == element:
                return i, j


def sub_matrix(key, pair):
    A = pos(key, pair[0])
    B = pos(key, pair[1])

    return min(A[0], B[0]), min(A[1], B[1]), max(A[0], B[0]), max(A[1], B[1])


def change(sub):
    corner1 = (sub[0], sub[1])
    corner2 = (sub[2], sub[3])

    if corner1[0] == corner2[0]:
        return (corner1[0], corner2[1]), (corner1[0], corner1[0])
    elif corner1[1] == corner2[1]:
        return (corner2[0], corner1[1]), (corner1[0], corner1[1])
    else:
        return (corner1[0], corner2[1]), (corner2[0], corner1[1])


def main():
    key = matrix(ceaser('PLAYFLAIR'))
    text = ''
    cipher = []

    for pair in [text[i:i + 2] for i in range(0, len(text), 2)]:
        t1, t2 = change(sub_matrix(key, pair))

        cipher.append(key[t1[0]][t1[1]])
        cipher.append(key[t2[0]][t2[1]])

    print(''.join(cipher))


if __name__ == '__main__':
    main()


"""ALPHA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z']


def ceaser(string):
    string = string.upper()
    to_add = ALPHA.copy()
    text = []

    for element in string:
        if element in to_add:
            text.append(element)
            to_add.remove(element)

    text += list((list(to_add)))

    if len(text) % 2 != 0:
        text += 'Z'

    return text


def matrix(key_text):
    key = []

    for i in range(0, 5):
        key.append(key_text[i * 5:(i + 1)*5])

    return key


def pos(key, element):
    for i in range(5):
        for j in range(5):
            if key[i][j] == element:
                return i, j


def sub_matrix(key, pair):
    A = pos(key, pair[0])
    B = pos(key, pair[1])

    return min(A[0], B[0]), min(A[1], B[1]), max(A[0], B[0]), max(A[1], B[1])


def change(sub):
    corner1 = (sub[0], sub[1])
    corner2 = (sub[2], sub[3])

    if corner1[0] == corner2[0]:
        return (corner1[0], corner2[1]), (corner1[0], corner1[0])
    elif corner1[1] == corner2[1]:
        return (corner2[0], corner1[1]), (corner1[0], corner1[1])
    else:
        return (corner1[0], corner2[1]), (corner2[0], corner1[1])


def main():
    key = matrix(ceaser('PLAYFLAIR'))
    text = ''
    cipher = []

    for pair in [text[i:i + 2] for i in range(0, len(text), 2)]:
        t1, t2 = change(sub_matrix(key, pair))

        cipher.append(key[t1[0]][t1[1]])
        cipher.append(key[t2[0]][t2[1]])

    print(''.join(cipher))


if __name__ == '__main__':
    main()
"""