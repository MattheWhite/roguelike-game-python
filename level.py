import pygame
from settings import TILESIZE
from tile import Tile
from player import Player
import debug
from pytmx.util_pygame import load_pygame
from weapon import Weapon
from UI import UI
from enemy import Enemy


class Level:
    def __init__(self) -> None:
        self.display_surf = pygame.display.get_surface()
        self.v_sprites = YSortCameraGroup()
        self.o_sprites = pygame.sprite.Group()
        self.tmx_data = load_pygame("graph/level/map.tmx")

        # create map
        self.create_map()

        # user interface
        self.ui = UI()

        # attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        # get enemys
        self.get_enemys('Boss')
        self.get_enemys('spirit')
        self.get_enemys('squid')
        self.get_enemys('bamboo')

    def create_map(self):
        for layer in self.tmx_data.layers:
            if layer.name in ("blocks"):
                for x, y, surf in layer.tiles():
                    pos = (x*TILESIZE, y*TILESIZE)
                    Tile(pos, [self.o_sprites], "invisible", surf)

        for obj in self.tmx_data.objects:
            pos = obj.x, obj.y
            Tile(pos, [self.v_sprites, self.o_sprites], "object", obj.image)

        for layer in self.tmx_data.layers:
            if layer.name in ("Player"):
                for x, y, surf in layer.tiles():
                    pos = (x*TILESIZE, y*TILESIZE)
                    self.player = Player(pos, [self.v_sprites], self.o_sprites, self.create_attack, self.destroy_attack)

    def get_enemys(self, monster_name):
        for layer in self.tmx_data.layers:
            if layer.name in (f"{monster_name}"):
                for x, y, surf in layer.tiles():
                    pos = (x*TILESIZE, y*TILESIZE)
                    Enemy(monster_name,
                          pos, [self.v_sprites, self.attackable_sprites], self.o_sprites, self.damage_player)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.v_sprites, self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        target_sprite.get_damage(self.player, attack_sprite.sprite_type)
                        # target_sprite.kill()

    def damage_player(self, amount, attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()

    def run(self):
        self.v_sprites.custom_draw(self.player)
        self.v_sprites.update()
        self.v_sprites.enemy_update(self.player)
        self.player_attack_logic()
        self.ui.display(self.player)
        debug.debug(f" movement speed: {self.player.speed}")


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.display_surf = pygame.display.get_surface()
        self.half_width = self.display_surf.get_size()[0] // 2
        self.half_height = self.display_surf.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the map
        self.map_surf = pygame.image.load("graph/ground/ground_map.png").convert()
        self.map_rect = self.map_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        map_offset_pos = self.map_rect.topleft - self.offset
        self.display_surf.blit(self.map_surf, map_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surf.blit(sprite.image, offset_pos)

    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type')
                         and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
