# 3.8
def find_common_and_all_elements(seq1, seq2):
    set1 = set(seq1)
    set2 = set(seq2)

    # Wspolne elementy
    common_elements = list(set1.intersection(set2))

    # Wszystkie elementy
    all_elements = list(set1.union(set2))

    return common_elements, all_elements

seq1 = [1, 2, 3, 4, 5, 'a', 'b']
seq2 = [4, 5, 6, 'a', 'c']
common_elements, all_elements = find_common_and_all_elements(seq1, seq2)

print("Elementy wspolne:", common_elements)
print("Wszystkie elementy:", all_elements)
