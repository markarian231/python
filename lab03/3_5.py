# 3.5
def draw_ruler(length):
    top_part = '|....' * length + '|'

    bottom_part = ''
    for i in range(length + 1):
        if i == 9 or i == 99:
            space_length = 4 - len(str(i))
        else:
            space_length = 5 - len(str(i))

        bottom_part += str(i) + ' ' * space_length

    complete_ruler = top_part + '\n' + bottom_part
    return complete_ruler

length = 12
print(draw_ruler(length))
