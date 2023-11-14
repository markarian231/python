# 3.10
# Slownik, innym sposobem byloby wykorzystanie bibliotek w Pythonie np "roman" ktora moze konwertowac te liczby na dziesietne
roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman2int(roman):
    total = 0
    prev_val = 0

    for num in reversed(roman):
        val = roman_numerals[num]
        if val < prev_val:
            total -= val
        else:
            total += val
        prev_val = val

    return total

print(roman2int("CXIV"))
