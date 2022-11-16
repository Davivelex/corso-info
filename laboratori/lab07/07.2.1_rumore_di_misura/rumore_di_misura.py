def error(v):
    for i in range(len(v)):
        if i == 0:
            v[i] = (v[i] + v[i + 1]) / 2
        elif i == len(v) - 1:
            v[i] = (v[i] + v[i - 1]) / 2
        else:
            v[i] = (v[i - 1] + v[i] + v[i + 1]) / 3


li = [11, 12, 67, 59, 91]
error(li)
print(' '.join(f'{x:.2f}' for x in li))
