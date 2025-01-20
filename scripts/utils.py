import pygame
import os

BASE_IMG_PATH = 'data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH+path)
    img.set_colorkey((0,0,0))
    return img

def load_image_list(path):
    images = list()
    for img_name in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + img_name))

    return images

load_image_list('tiles/grass')