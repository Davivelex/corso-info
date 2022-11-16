def count_vowels(string):
    count = 0
    for c in string:
        if c.lower() in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count


input_string = input("Inserisci una parola: ")
print(f"Le vocali sono: {count_vowels(input_string)}")
