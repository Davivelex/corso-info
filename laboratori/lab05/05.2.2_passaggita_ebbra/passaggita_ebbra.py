from random import randint

pos = (0, 0)

for _ in range(100):
    scelta = randint(0, 3)

    if scelta == 0:
        pos = (pos[0]+1, pos[1])
    elif scelta == 1:
        pos = (pos[0]-1, pos[1])
    elif scelta == 2:
        pos = (pos[0], pos[1]+1)
    elif scelta == 3:
        pos = (pos[0], pos[1]-1)


print(f"La posizione finale è {pos}")