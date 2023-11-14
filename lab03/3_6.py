# 3.6
def draw_rectangle(width, height):
    horizontal = '+' + ('---+' * width)
    vertical = '|' + ('   |' * width)

    rectangle = ''
    for _ in range(height):
        rectangle += horizontal + '\n' + vertical + '\n'
    rectangle += horizontal

    return rectangle


width = 6
height = 3
print(draw_rectangle(width, height))
