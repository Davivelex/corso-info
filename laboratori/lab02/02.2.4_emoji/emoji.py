formato = "%-15s%-15s%-40s%-15s"

print(formato % ("Posizione", "Numero Unicode", "Nome Unicode", "Emoji"))
print("-"*75)
print(formato % (1, "U+1F602", "Face with Tears of Joy", "\U0001f602"))
print(formato % (2, "U+2764", "Black Heart Symbol", "\U00002764"))
print(formato % (3, "U+1F60D", "Smiling Face with Heart-Shaped Eyes", "\U0001F60D"))
