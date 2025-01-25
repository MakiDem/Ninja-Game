import pygame

pygame.init()

class Entity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0,0]
        self.collisions = {'top': False, 'bottom': False, 'left': False, 'right': False}

        self.action = 'idle'
        self.animation = self.game.assets[f'{self.type}/{self.action}']
        self.anim_offset = (-3,-3) #to counteract the overflow for entity hit-box
        self.flip = False
        self.set_action(self.action)

    def set_action(self, action): # after previous action, current action will be reset to the start(i think)
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[f'{self.type}/{self.action}'].copy()


    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tile_map, movement=(0,0)):
        self.collisions = {'top': False, 'bottom': False, 'left': False, 'right': False}
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        rect = self.rect()

        self.velocity[1] = min(5.0, self.velocity[1] + 0.1)
        # 5 == terminal velocity/max falling speed

        self.pos[0] += frame_movement[0]#x
        for tile in tile_map.check_physics_rect(self.pos):
            if rect.colliderect(tile): #tile collision in the x-axis
                if frame_movement[0] > 0:
                    rect.right = tile.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    rect.left = tile.right
                    self.collisions['left'] = True
                self.pos[0] = rect.x

        self.pos[1] += frame_movement[1]#y
        rect = self.rect()
        for tile in tile_map.check_physics_rect(self.pos):
            if rect.colliderect(tile): #tile collision in the y-axis
                if frame_movement[1] > 0:
                    rect.bottom = tile.top
                    self.collisions['bottom'] = True
                if frame_movement[1] < 0:
                    rect.top = tile.bottom
                    self.collisions['top'] = True
                self.pos[1] = rect.y

        if movement[0] > 0:
            self.flip = False
        if movement[0] < 0:
            self.flip = True

        # y-deceleration
        if self.collisions['bottom'] or self.collisions['top']:
            self.velocity[1] = 0
        # x-deceleration
        if self.collisions['right'] or self.collisions['left']:
            self.velocity[0] = 0

        self.animation.update()


    def render(self, offset):
        self.game.display.blit(pygame.transform.flip(self.animation.curr_frame(), self.flip, False),
                               (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))
        #self.game.display.blit(self.game.assets[self.type], (self.pos[0] - offset[0], self.pos[1] - offset[1]))