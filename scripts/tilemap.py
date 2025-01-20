import pygame

NEIGHBORING_OFFSETS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
PLATFORM_TILES = ['grass', 'stone']

class TileMap:
    def __init__(self, game, tile_size=16):
        self.game = game

        self.tile_size = tile_size
        self.tile_map = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tile_map[str(i+3)+';10'] = {
                'type': 'grass',
                'variant': 1,
                'pos': (i+3, 10)
            }
            self.tile_map['10;' + str(i + 5)] = {
                'type': 'stone',
                'variant': 1,
                'pos': (10, i + 5)
            }
    def check_tiles_around(self, pos):
        tiles = []
        loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBORING_OFFSETS:
            check_loc = str(loc[0] + offset[0]) + ';' + str(loc[1] + offset[1])
            if check_loc in self.tile_map:
                tiles.append(self.tile_map[check_loc])
        return tiles

    def check_physics_rect(self, pos):
        rects = []
        for tile in self.check_tiles_around(pos):
            if tile['type'] in PLATFORM_TILES:
                rects.append(pygame.Rect(tile['pos'][0]*self.tile_size, tile['pos'][1]*self.tile_size, self.tile_size, self.tile_size))
        return rects

    def render(self, surf, offset=(0,0)):
        for x in range(offset[0] // self.tile_size, (surf.get_width()+offset[0]) // self.tile_size + 1):
            for y in range(offset[1] // self.tile_size, (surf.get_height() + offset[1]) // self.tile_size + 1):
                loc = str(x) + ';' + str(y)

                if loc in self.tile_map:
                    tile = self.tile_map[loc]
                    surf.blit(self.game.assets[tile['type']][tile['variant']],
                            (tile['pos'][0]*self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))

        # for pos in self.tile_map:
        #     tile = self.tile_map[pos]
        #     surf.blit(self.game.assets[tile['type']][tile['variant']],
        #               (tile['pos'][0]*self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))
        #
        # for tile in self.offgrid_tiles:
        #     surf.blit(self.game.assets[tile['type']][tile['variant']],
        #               (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))