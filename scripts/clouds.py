import pygame
import random

class Cloud:
    def __init__(self, pos, img, speed, depth):
        self.pos = list(pos)
        self.img = img
        self.speed = speed
        self.depth = depth

    def update(self):
        self.pos[0] += self.speed

    def render(self, surf, offset):
        render_pos = (self.pos[0] - offset[0]*self.depth, self.pos[1] - offset[1]*self.depth)
        surf.blit(self.img, (render_pos[0] % (surf.get_width()+ self.img.get_width())-self.img.get_width(),
                                              render_pos[1] % (surf.get_height()+ self.img.get_height())-self.img.get_height()))

class Clouds:
    def __init__(self, cloud_images, count=16):
        self.clouds = list()
        for i in range(count):
            x_pos = random.random() * 99999
            y_pos = random.random() * 99999
            img = random.choice(cloud_images)
            speed = random.random() * 0.05 + 0.05
            depth = random.random() * 0.04 + 0.6
            self.clouds.append(Cloud((x_pos, y_pos), img, speed, depth))

        self.clouds.sort(key=lambda x: x.depth)

    def update(self):
        for cloud in self.clouds:
            cloud.update()

    def render(self, surf, offset):
        for cloud in self.clouds:
            cloud.render(surf, offset)