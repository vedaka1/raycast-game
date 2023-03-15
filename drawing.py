import pygame
from settings import *
from raycast import raycast 
from map import minimap


class Drawing:
    def __init__(self, screen, screen_map):
        pygame.init()
        self.screen = screen
        self.screen_map = screen_map
        self.font = pygame.font.SysFont('arial', 30)

    def background(self):
        pygame.draw.rect(self.screen, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.screen, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_position, player_angle):
        raycast(self.screen, player_position, player_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.screen.blit(render, FPS_POS )

    def minimap(self, player):
        self.screen_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.screen_map, YELLOW, (map_x, map_y), (map_x + 10 * math.cos(player.angle), 
                                                                   map_y + 10 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.screen_map, RED, (int(map_x), int(map_y)), 5)
     
        for x, y in minimap:
            pygame.draw.rect(self.screen_map, GREEN, (x, y, MAP_TILE, MAP_TILE))
            self.screen.blit(self.screen_map, MAP_POS)
