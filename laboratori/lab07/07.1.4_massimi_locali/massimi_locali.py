def search_max(v):
    el = []

    for i in range(1, len(v)-1):
        if v[i-1] < v[i] > v[i+1]:
            el.append((i, v[i]))

    return el


inp = '_'
li = []

while inp != '':
    inp = input('Inserisci numero: ')
    if inp.isdigit():
        li.append(int(inp))

if len(search_max(li)) > 0:
    for i, m in search_max(li):
        print(i)
else:
    print("Non ci sono massimi")

if len(search_max(li)) > 2:
    dist = len(li)
    for j in range(1, len(search_max(li))):
        dist = min(search_max(li)[j][0] - search_max(li)[j - 1][0], dist)
    print("La distanza minima tra due massimi è: ", dist)
