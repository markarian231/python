# 3.4
while True:
    input_str = input("Wpisz liczbe rzeczywista (float) lub 'stop' aby zakonczyć: ")

    if input_str.lower() == 'stop':
        break

    try:
        x = float(input_str)
        print(f"Wprowadzona liczba: {x}, jej trzecia potega: {x**3}")
    except ValueError:
        print("To nie jest poprawna liczba rzeczywista. Sprobuj ponownie.")
