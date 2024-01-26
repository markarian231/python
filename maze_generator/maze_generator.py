import pygame
import random

pygame.init()

window_width = 800
window_height = 600
panel_height = 40
win = pygame.display.set_mode((window_width, window_height))

# Rozdzielczość labiryntu
w = 20
cols = int(win.get_width()/w)
rows = int((window_height - panel_height) / w)

grid = []
unvisited = []

# Funkcja pomocna w znajdowaniu sąsiadów komórek
def index(i, j):
    if i < 0 or j < 0 or i > cols -1 or j > rows - 1:
        return None
    else:
        return i+j*cols

class Cell:
    def __init__(self, i, j):
        self.i, self.j = i, j
        self.walls = [True, True, True, True]
        self.visited = False

    def show(self, win):
        x = self.i * w
        y = self.j * w

        if self.visited:
            pygame.draw.rect(win, "#3FA600", (self.i*w, self.j*w, w, w))
        if self.walls[0]:
            pygame.draw.line(win, (0, 0, 0), (x,y), (x+w,y))
        if self.walls[1]:
            pygame.draw.line(win, (0, 0, 0), (x+w,y), (x+w,y+w))
        if self.walls[2]:
            pygame.draw.line(win, (0, 0, 0), (x+w,y+w), (x,y+w))
        if self.walls[3]:
            pygame.draw.line(win, (0, 0, 0), (x,y+w), (x,y))

    def highlight(self, win):
        x = self.i * w
        y = self.j * w
        if self.visited:
            pygame.draw.rect(win, "#F3F302", (self.i*w, self.j*w, w, w))

    def checkNeighbors(self):
        neighbors = []
        i, j = self.i, self.j
        if index(i, j-1):
            top = grid[index(i, j-1)]
            neighbors.append(top)
        if index(i+1, j):
            right = grid[index(i+1, j)]
            neighbors.append(right)
        if index(i-1, j):
            left = grid[index(i-1, j)]
            neighbors.append(left)
        if index(i, j+1):
            bottom = grid[index(i, j+1)]
            neighbors.append(bottom)

        if len(neighbors) > 0:
            return random.choice(neighbors)
        else:
            return None

# Przy przejściu do kolejnej komórki, usuwane są krawędzie między nimi
def removeWalls(a, b):
    x = a.i - b.i
    if x == 1:
        a.walls[3] = False
        b.walls[1] = False
    elif x == -1:
        a.walls[1] = False
        b.walls[3] = False
    y = a.j - b.j
    if y == 1:
        a.walls[0] = False
        b.walls[2] = False
    elif y == -1:
        a.walls[2] = False
        b.walls[0] = False

def save_maze(grid, cols, rows, filename="maze.txt"):
    with open(filename, "w") as file:
        cell_count = 0
        for j in range(rows):
            row_data = ""
            for i in range(cols):
                cell = grid[cell_count]
                cell_data = "".join(["1" if wall else "0" for wall in cell.walls])
                row_data += cell_data
                cell_count += 1
            file.write(f"{row_data}\n")

for j in range(rows):
    for i in range(cols):
        cell = Cell(i, j)
        grid.append(cell)
        unvisited.append(cell)

# Komórka startowa
n = 0
current = grid[n]

# GUI
panel_y = window_height - panel_height
button_width = 80
button_height = 30
save_button_width = 120
start_button_x = 10
stop_button_x = 100
save_txt_button_x = window_width - save_button_width - 10  # 10 pixeli od prawej krawędzi
save_png_button_x = save_txt_button_x - save_button_width - 10
button_y = panel_y + 5
white = (255, 255, 255)
grey = (200, 200, 200)
black = (0, 0, 0)

start_button = pygame.Rect(start_button_x, button_y, button_width, button_height)
stop_button = pygame.Rect(stop_button_x, button_y, button_width, button_height)
save_txt_button = pygame.Rect(save_txt_button_x, button_y, save_button_width, button_height)
save_png_button = pygame.Rect(save_png_button_x, button_y, save_button_width, button_height)


running = True
start_generation = False

# Pętla gry
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if start_button.collidepoint((mouse_x, mouse_y)):
                start_generation = True
            elif stop_button.collidepoint((mouse_x, mouse_y)):
                start_generation = False
            elif save_txt_button.collidepoint((mouse_x, mouse_y)):
                save_maze(grid, cols, rows)
                print("Saved as text")
            elif save_png_button.collidepoint((mouse_x, mouse_y)):
                pygame.image.save(win, "maze_snapshot.png")
                print("Saved as image")

    # Rysowanie labiryntu
    win.fill(black)

    for cell in grid:
        cell.show(win)

    # Generowanie labiryntu algorytmem Aldous-Broder
    if start_generation:
        current.visited = True
        for cell in unvisited:
            if cell == current:
                unvisited.remove(cell)
        current.highlight(win)
        if len(unvisited) > 0:
            nextcell = current.checkNeighbors()
            if isinstance(nextcell, Cell) and not nextcell.visited:
                removeWalls(current, nextcell)
                nextcell.visited = True
            current = nextcell

    # Rysowanie GUI
    pygame.draw.rect(win, grey, (0, panel_y, window_width, panel_height))
    pygame.draw.rect(win, white, start_button)
    pygame.draw.rect(win, white, stop_button)
    pygame.draw.rect(win, white, save_txt_button)
    pygame.draw.rect(win, white, save_png_button)

    font = pygame.font.SysFont(None, 24)
    win.blit(font.render('Start', True, black), (start_button_x + 20, button_y + 7))
    win.blit(font.render('Stop', True, black), (stop_button_x + 20, button_y + 7))
    win.blit(font.render('Save .txt', True, black), (save_txt_button_x + 20, button_y + 7))
    win.blit(font.render('Save .png', True, black), (save_png_button_x + 20, button_y + 7))

    pygame.display.update()

pygame.quit()
