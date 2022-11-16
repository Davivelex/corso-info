stringa = input("Inserisci una stringa: ")

print(f"Solo lettere maiusole: {', '.join(filter(lambda c: c != '', [c if c.isupper() else '' for c in stringa]))}\n"
      f"\nLettere in posizione "
      f"pari: "
      f"{', '.join(filter(lambda c: c != '', [c[1] if c[0] % 2 == 0 else '' for c in enumerate(stringa)]))}\n\n'_' al "
      f"posto delle vocali: "
      f"{''.join(['_' if c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] else c for c in stringa])}\n\nIl "
      f"numero di cifre numeriche: {len(list(filter(lambda c: c.isdigit(), stringa)))}\n\nIl numero di vocali: "
      f"{len(list(filter(lambda c: c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'], stringa)))}")
