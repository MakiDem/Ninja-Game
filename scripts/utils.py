import pygame
import os

BASE_IMG_PATH = 'data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH+path).convert()
    img.set_colorkey((0,0,0))
    return img

def load_image_list(path):
    images = list()
    for img_name in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + img_name))

    return images



class Animation:
    def __init__(self, frames, frame_dur=5, loop=True):
        self.frames = frames
        self.loop = loop
        self.frame_dur = frame_dur

        self.frame_index = 0
        self.done = False

    def copy(self): #after previous action, current action will be reset to the start
        return Animation(self.frames, self.frame_dur, self.loop)

    def update(self):
        if self.loop:
            self.frame_index = (self.frame_index + 1) % (len(self.frames) * self.frame_dur)
        else:
            self.frame_index = min(self.frame_index+1, self.frame_dur * len(self.frames) - 1)
            if self.frame_index >= self.frame_dur * len(self.frames) - 1:
                self.done = True

    def curr_frame(self):
        return self.frames[int(self.frame_index / self.frame_dur)]