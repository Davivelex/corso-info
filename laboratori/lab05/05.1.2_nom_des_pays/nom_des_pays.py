pays = input("Inserisci nazione: ")

e1 = ['Belize', 'Cambodge', 'Mexique', 'Mozambique', 'Zaïre', 'Zimbabwe']
e2 = ['Etats-Unis', 'Pays-Bas']
v = ['A', 'E', 'I', 'O', 'U']

if pays in e1:
    print(f'Le {pays}')
elif pays in e2:
    print(f'Les {pays}')
elif pays[0] in v:
    print(f'L\'{pays}')
else:
    if pays[-1] == 'e':
        print(f'La {pays}')
    else:
        print(f'Le {pays}')

