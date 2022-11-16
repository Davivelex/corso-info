def remove_min(v):
    el = []
    removed = False

    for e in v:
        if e == sorted(v)[0] and not removed:
            removed = True
        else:
            el.append(e)

    v.clear()
    for e in el:
        v.append(e)


li = [1, 2, 5, 1, 6, 3, 6, 3]
print(li)
remove_min(li)
print(li)
