from random import randint


def sort(v):
    vo = []
    for e in sorted(v):
        vo.append(e)

    v.clear()
    for e in vo:
        v.append(e)


li = []
for _ in range(20):
    li.append(randint(0, 99))

print(li)
sort(li)
print(li)