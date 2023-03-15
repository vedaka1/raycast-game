from settings import *
import pygame
import math


class Player:
    def __init__(self):
        self.x, self.y = player_position
        self.angle = player_angle

    @property
    def position(self):
        return (int(self.x), int(self.y))

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
            print('w')
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
            print('s')
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
            print('a')
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
            print('d')
        if pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] < HALF_WIDTH:
                self.angle -= 0.03
                pygame.mouse.set_pos(HALF_WIDTH, HALF_HEIGHT)
            elif mouse_pos[0] > HALF_WIDTH:
                self.angle += 0.03
                pygame.mouse.set_pos(HALF_WIDTH, HALF_HEIGHT)
        # if keys[pygame.K_LEFT]:
        #     self.angle -= 0.03
        # if keys[pygame.K_RIGHT]:
        #     self.angle += 0.03