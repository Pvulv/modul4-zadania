def czy_palindrom(slowo):
    # Sprawdzenie, czy słowo jest równe swojemu odbiciu (odwrócona wersja)
    return slowo == slowo[::-1]

slowo = "kanapka"

if bool(czy_palindrom(slowo)) == True:
    print(True)
else:
    print(False)