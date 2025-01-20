import pygame
from sys import exit

from pygame import Surface

from scripts.entity import Entity
from scripts.utils import load_image, load_image_list
from scripts.tilemap import TileMap
from scripts.clouds import Clouds


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.display = Surface((320, 240))
        pygame.display.set_caption('Ninja Game')

        self.assets = {
            'decor': load_image_list('tiles/decor'),
            'grass': load_image_list('tiles/grass'),
            'large_decor': load_image_list('tiles/large_decor'),
            'spawners': load_image_list('tiles/spawners'),
            'stone': load_image_list('tiles/stone'),
            'player': load_image('entities/player.png').convert(),
            'background': load_image('background.png'),
            'clouds': load_image_list('clouds')
        }

        self.clock = pygame.time.Clock()
        self.player = Entity(self, 'player', (50,50), (8,15))
        self.movement = [False, False]

        self.tile_map = TileMap(self, tile_size=16)
        self.scroll = [0,0]

        self.clouds = Clouds(self.assets['clouds'])

    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0,0))


            self.scroll[0]+=(self.player.rect().centerx - self.display.get_width()/ 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_offset = [int(self.scroll[0]), int(self.scroll[1])]
            print(render_offset)

            self.clouds.update()
            self.clouds.render(self.display, offset=render_offset)

            self.player.update(self.tile_map, (self.movement[1] - self.movement[0], 0))
            self.player.render(offset=render_offset)

            self.tile_map.render(self.display, render_offset)



            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))

            pygame.display.update()
            self.clock.tick(60)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True

                    if event.key == pygame.K_SPACE:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

Game().run()