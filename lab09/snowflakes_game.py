import pygame
import random

pygame.init()

# Wymiary
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gra Płatki Śniegu")

WHITE = (255, 255, 255)
BACKGROUND = (61, 37, 255)

class Snowflake:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = 0
        self.size = random.randint(5, 9)
        self.active = True  # Aktywne tzn, płatek nadal spada

    def fall(self):
        if self.active:
            self.y += 3

    def draw(self, surface):
        if self.active:
            pygame.draw.circle(surface, WHITE, (self.x, self.y), self.size)

# Zmienne gry
snowflakes = []
game_over = False
clock = pygame.time.Clock()
snowLevel_height = 0

while not game_over:
    screen.fill(BACKGROUND)

    # Rysowanie poziomu śniegu
    pygame.draw.rect(screen, WHITE, (0, SCREEN_HEIGHT - snowLevel_height, SCREEN_WIDTH, snowLevel_height))

    # Zdarzenia
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN: # Kliknięcie w płatek
            pos = pygame.mouse.get_pos()
            snowflakes = [flake for flake in snowflakes if not (flake.x - flake.size <= pos[0] <= flake.x + flake.size and flake.y - flake.size <= pos[1] <= flake.y + flake.size)]

    # Dodanie nowego płatka
    if random.randint(1, 16) == 1:
        snowflakes.append(Snowflake())

    # Aktualizacja płatków
    for flake in snowflakes:
        flake.fall()
        flake.draw(screen)

        # Zwiększenie wysokości poziomu śniegu
        if flake.y >= SCREEN_HEIGHT - snowLevel_height:
            flake.active = False
            snowLevel_height += flake.size  # Zwiększa wysokość o rozmiar śnieżynki

        # Warunek końcowy
        if snowLevel_height >= SCREEN_HEIGHT:
            game_over = True

    # Usuwanie nieaktywnych płatków
    snowflakes = [flake for flake in snowflakes if flake.active]

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
