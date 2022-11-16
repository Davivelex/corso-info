pin = 6392
attempt = 0

while attempt < 3:
    attempt += 1

    if pin == input("Insert PIN: "):
        print("Your PIN is correct")
    else:
        print("Your PIN is incorrect")

if attempt == 3:
    print("Your bank card is blocked")
