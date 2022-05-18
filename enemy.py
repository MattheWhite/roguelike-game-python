import pygame
from settings import *
from entities import Entity
from support import import_folder


class Enemy(Entity):
    def __init__(self, monster_name, pos, groups, o_sprites):
        super().__init__(groups)

        # graphics setup
        self.import_graphics(monster_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]

        # movement
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.o_sprites = o_sprites

    def import_graphics(self, name):
        self.animations = {'idle': [], 'move': [], 'attack': []}
        main_path = f'graph/monsters/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)
