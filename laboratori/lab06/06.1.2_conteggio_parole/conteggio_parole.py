def count_words(string):
    return len(list(filter(lambda x: x != '', string.split(' '))))


input_string = input("Inserisci frase: ")
print(f"Le parole nella frase sono: {count_words(input_string)}")
