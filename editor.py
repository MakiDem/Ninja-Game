import pygame
from sys import exit

from pygame import Surface

from scripts.utils import load_image, load_image_list
from scripts.tilemap import TileMap
from scripts.clouds import Clouds


class Editor:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.display = Surface((320, 240))
        pygame.display.set_caption('Level Editor')

        self.assets = {
            'decor': load_image_list('tiles/decor'),
            'grass': load_image_list('tiles/grass'),
            'large_decor': load_image_list('tiles/large_decor'),
            'spawners': load_image_list('tiles/spawners'),
            'stone': load_image_list('tiles/stone'),
            'background': load_image('background.png'),
            'clouds': load_image_list('clouds'),
        }

        self.clock = pygame.time.Clock()
        self.movement = [False, False, False, False]

        self.tile_map = TileMap(self, tile_size=16)
        self.scroll = [0,0]

        self.tile_list = list(self.assets)
        self.tile_group = 0
        self.tile_variant = 0

        self.clicking = False
        self.right_click = False

    def run(self):
        while True:
            self.display.fill((0,0,0))

            curr_tile_img = self.assets[self.tile_list[self.tile_group]][self.tile_variant].copy()
            curr_tile_img.set_alpha(100) #make img semi-transparent

            self.display.blit(curr_tile_img, (5,5))

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))

            pygame.display.update()
            self.clock.tick(60)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: #left mouse button
                        clicking = True
                        print('left click')
                    if event.button == 2: #mouse scroll button
                        clicking = True
                        print('scroll click')
                    if event.button == 3: #right mouse button
                        clicking = True
                        print('right click')

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.movement[2] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = True


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pygame.K_UP:
                        self.movement[2] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = False

Editor().run()