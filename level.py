import pygame
import sys
from magic import MagicPlayer
from particles import AnimationPlayer
from settings import TILESIZE
from tile import Tile
from player import Player
import debug
from pytmx.util_pygame import load_pygame
from weapon import Weapon
from UI import UI
from enemy import Enemy
from particles import AnimationPlayer
from magic import MagicPlayer
from upgrade import Upgrade


class Level:
    def __init__(self) -> None:
        self.display_surf = pygame.display.get_surface()
        self.game_paused = False
        self.toogle_time = 0
        self.can_toggle = True
        self.toggle_duration_cooldown = 200
        self.v_sprites = YSortCameraGroup()
        self.o_sprites = pygame.sprite.Group()
        self.tmx_data = load_pygame("graph/level/map.tmx")

        # font
        self.font = pygame.font.Font("graph/font/game_font.ttf", 50)
        self.width = self.display_surf.get_size()[0]
        self.heigth = self.display_surf.get_size()[1]

        # background
        self.background = pygame.image.load('menu/ninja.png').convert_alpha()
        self.background_rect = self.background.get_rect(topleft=(0, 0))
        self.game_over_surf = self.font.render("GAME OVER", False, 'black')
        self.game_over_rect = self.game_over_surf.get_rect(center=(self.width * 0.5, self.heigth * 0.35))
        self.game_exit_surf = self.font.render("EXIT", False, 'black')
        self.game_exit_rect = self.game_exit_surf.get_rect(center=(self.width * 0.5, self.heigth * 0.75))

        # create map
        self.create_map()

        # user interface
        self.ui = UI()
        self.upgrade = Upgrade(self.player)

        # particles
        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)

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
                    self.player = Player(pos,
                                         [self.v_sprites], self.o_sprites,
                                         self.create_attack, self.destroy_attack, self.create_magic)

    def get_enemys(self, monster_name):
        for layer in self.tmx_data.layers:
            if layer.name in (f"{monster_name}"):
                for x, y, surf in layer.tiles():
                    pos = (x*TILESIZE, y*TILESIZE)
                    Enemy(monster_name,
                          pos, [self.v_sprites, self.attackable_sprites],
                          self.o_sprites, self.damage_player, self.trigger_death_particles, self.add_exp)

    def check_player_death(self, player, v_sprites):
        m_button = pygame.mouse.get_pressed()
        m_pos = pygame.mouse.get_pos()
        if player not in v_sprites:
            self.display_surf.fill("black")
            pygame.draw.rect(self.display_surf, 'white', self.game_over_rect.inflate(20, 20))
            pygame.draw.rect(self.display_surf, 'black', self.game_over_rect.inflate(20, 20), 5)
            self.display_surf.blit(self.game_over_surf, self.game_over_rect)
            pygame.draw.rect(self.display_surf, 'white', self.game_exit_rect.inflate(20, 20))
            pygame.draw.rect(self.display_surf, 'black', self.game_exit_rect.inflate(20, 20), 5)
            self.display_surf.blit(self.game_exit_surf, self.game_exit_rect)
            if self.game_exit_rect.collidepoint(m_pos):
                pygame.draw.rect(self.display_surf, 'gold', self.game_exit_rect.inflate(20, 20), 5)
                if m_button[0]:
                    pygame.quit()
                    sys.exit()

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.v_sprites, self.attack_sprites])

    def create_magic(self, style, strength, cost):
        if style == "heal":
            self.magic_player.heal(self.player, strength, cost, [self.v_sprites])
        if style == "flame":
            self.magic_player.flame(self.player, cost, [self.v_sprites, self.attack_sprites])

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
                        target_sprite.get_damage(self.player, attack_sprite)

    def damage_player(self, amount, attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            self.animation_player.create_particles(attack_type, self.player.rect.center, [self.v_sprites])

    def trigger_death_particles(self, pos, particle_type):
        self.animation_player.create_particles(particle_type, pos, self.v_sprites)

    def add_exp(self, amount):
        self.player.exp += amount

    def toggle_menu(self):
        keys = pygame.key.get_pressed()
        if self.can_toggle:
            if keys[pygame.K_p]:
                self.can_toggle = False
                self.toogle_time = pygame.time.get_ticks()
                self.game_paused = not self.game_paused

    def toogle_cooldown(self):
        current_time = pygame.time.get_ticks()
        if not self.can_toggle:
            if current_time - self.toogle_time >= self.toggle_duration_cooldown:
                self.can_toggle = True

    def run(self):
        self.toggle_menu()
        self.toogle_cooldown()
        self.v_sprites.custom_draw(self.player)
        self.ui.display(self.player)
        if self.game_paused:
            self.upgrade.display()
        else:
            self.check_player_death(self.player, self.v_sprites)
            self.v_sprites.update()
            self.v_sprites.enemy_update(self.player)
            self.player_attack_logic()
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
