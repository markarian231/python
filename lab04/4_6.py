# 4.6
def sum_seq(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):  # czy element jest sekwencja
            total += sum_seq(item)           # rekurencyjnie wywoluje dla podsekwencji
        else:
            total += item
    return total

sequence = [1, (2, 3), [4, [5, 6]], 7]
print(sum_seq(sequence))

