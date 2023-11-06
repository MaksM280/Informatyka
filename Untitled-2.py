def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n-1)

liczba = int(input("Podaj liczbę: "))

wynik = silnia(liczba)
print(f"{liczba}! = {wynik}")