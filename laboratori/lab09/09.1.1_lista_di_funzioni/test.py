import lista_di_funzioni

if __name__ == '__main__':
    v1 = [1, 2, 3, 4, 5, 6]
    v2 = [1, 4, 9, 16, 25]
    v3 = [1, 2, 3, 4, 5, 6]
    v4 = [1, 2, 9, 5, 7, 8]
    v5 = [1, 2, 3, 4, 5]
    v6 = [1, 2, 3, 4, 5, 6]
    v7 = [1, 2, 3, 4, 5, 6]
    v8 = [1, 2, 3, 4, 5, 6]
    v9 = [1, 2, 3, 4, 5, 6]
    v10 = [6, 5, 4, 3, 2, 1]
    v11 = [1, 2, 3, 3, 4, 5]
    v12 = [1, 2, 3, 4, 5, 6]
    v13 = [1, 2, 3, 1, 5, 6]
    v14 = [1, 2, 3, 4, 5, 6]

    print('Test funzione 1:')
    lista_di_funzioni.switch_first_last(v1)
    print(v1 == [6, 2, 3, 4, 5, 1])

    print('\nTest funzione 2')
    lista_di_funzioni.slide(v2)
    print(v2 == [25, 1, 4, 9, 16])

    print('\nTest funzione 3')
    lista_di_funzioni.change_pair(v3)
    print(v3 == [1, 0, 3, 0, 5, 0])

    print('\nTest funzione 4')
    lista_di_funzioni.change_max(v4)
    print(v4 == [1, 9, 9, 9, 9, 8])

    print('\nTest funzione 5')
    lista_di_funzioni.remove_middle(v5)
    lista_di_funzioni.remove_middle(v6)
    print('Dispari: ', v5 == [1, 2, 4, 5])
    print('Pari: ', v6 == [1, 2, 5, 6])

    print('\nTest funzione 6')
    print(v7 == [2, 4, 6, 1, 3, 5])

    print('\nTest funzione 7')
    print(lista_di_funzioni.second_max(v8) == 5)

    print('\nTest funzione 8')
    print(lista_di_funzioni.is_asc(v9) == True)
    print(lista_di_funzioni.is_asc(v10) == False)

    print('\nTest funzione 9')
    print(lista_di_funzioni.adjacent_pair(v11) == True)
    print(lista_di_funzioni.adjacent_pair(v12) == False)

    print('\nTest funzione 10')
    print(lista_di_funzioni.contains_duplicate(v13) == True)
    print(lista_di_funzioni.contains_duplicate(v14) == False)
