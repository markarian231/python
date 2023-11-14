# 4.2
def make_ruler(length):
    if length < 0:
        raise ValueError("Długosc miarki musi byc liczba nieujemna")

    top_part = '|....' * length + '|'
    bottom_part = ''

    for i in range(length + 1):
        if i == 9 or i == 99:  # Specjalne przypadki dla 9 i 99
            space_length = 4 - len(str(i))
        else:
            space_length = 5 - len(str(i))

        bottom_part += str(i) + ' ' * space_length

    complete_ruler = top_part + '\n' + bottom_part
    return complete_ruler

def make_grid(rows, cols):
    if rows <= 0 or cols <= 0:
        raise ValueError("Liczba wierszy i kolumn musi być wieksza niż 0")

    row_str = '+---' * cols + '+\n' + '|   ' * cols + '|\n'
    grid_str = row_str * rows + '+---' * cols + '+'

    return grid_str

ruler_result = make_ruler(12)
grid_result = make_grid(2, 4)

print("Ruler:")
print(ruler_result)

print("\nGrid:")
print(grid_result)
