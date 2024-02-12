# Liczby naturalne a i b nazywamy zaprzyjaźnionymi, jeżeli suma dzielników
# właściwych a wynosi b, a suma dzielników właściwych b wynosi a.
# Proszę napisać program, który znajduje wszystkie pary liczb zaprzyjaźnionych
# mniejszych od 1000.

# funkcja oblicza sumę dzielników danej liczby
def suma_dzielnikow(n):
    return sum([i for i in range(1, n) if n % i == 0])

# funkcja szuka par liczb zaprzyjaźnionych w podanym zakresie - mniejsze niż 1000
def szukanie_zaprzyjaznionych(zakres):
    liczby_zaprzyjaznione = []
    for a in range(2, zakres):
        b = suma_dzielnikow(a)
        if a != b and b < zakres and suma_dzielnikow(b) == a:
            para = (min(a, b), max(a, b))
            if para not in liczby_zaprzyjaznione:
                liczby_zaprzyjaznione.append(para)
    return liczby_zaprzyjaznione

zakres = 1000
wynik = szukanie_zaprzyjaznionych(zakres)
print("Pary liczb zaprzyjaźnionych mniejszych od", zakres, "to:", wynik)