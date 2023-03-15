import pygame
from settings import *
from player import Player
from drawing import Drawing
# import math
from map import world_map
# from raycast import raycast

run = True 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_map = pygame.surface.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen, screen_map)
pygame.mouse.set_visible(False)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()

    drawing.background()
    drawing.world(player.position, player.angle)
    drawing.fps(clock)
    drawing.minimap(player)

    pygame.display.flip()
    clock.tick(FPS)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Game")