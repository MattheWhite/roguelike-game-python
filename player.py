import pygame
from settings import weapon_data
from support import import_folder
from entities import Entity


class Player(Entity):
    def __init__(self, pos, groups, o_sprites, create_attack, destroy_attack) -> None:
        super().__init__(groups)
        self.image = pygame.image.load("graph/player/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -20)

        # movement
        self.attacking = False
        self.range_attacking = False
        self.cooldown = 400
        self.attack_time = 0
        self.o_sprites = o_sprites
        self.superspeed = 20

        # animation
        self.import_player_assets()
        self.status = "down"

        # weapon
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 200

        # stats
        self.stats = {'health': 100, 'stamina': 60, 'attack': 10, 'magic': 4, 'speed': 5}
        self.health = self.stats['health'] * 0.5
        self.stamina = self.stats['stamina']
        self.speed = self.stats['speed']
        self.exp = 10

        # damage timer
        self.vulnerable = False
        self.hurt_time = 0
        self.invulnerability_duartion = 500

    def input(self):
        keys = pygame.key.get_pressed()
        m_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        # move
        if not self.attacking:
            if keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            if keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'left'
            elif keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'right'
            else:
                self.direction.x = 0

            # meele attack
            if m_buttons[0]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()

            # range attack
            for sprite in self.o_sprites:
                if m_buttons[2] and sprite.rect.collidepoint(mouse_pos):
                    self.attacking = True
                    self.range_attacking = True
                    self.attack_time = pygame.time.get_ticks()

        if keys[pygame.K_q] and self.can_switch_weapon:
            self.can_switch_weapon = False
            self.weapon_switch_time = pygame.time.get_ticks()
            if self.weapon_index < len(list(weapon_data.keys())) - 1:
                self.weapon_index += 1
            else:
                self.weapon_index = 0
            self.weapon = list(weapon_data.keys())[self.weapon_index]

        if keys[pygame.K_r] and keys[pygame.K_u]:
            self.speed = self.superspeed
        if keys[pygame.K_LALT]:
            self.speed = self.stats['speed']

    def import_player_assets(self):
        caracter_path = "graph/player/"
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                           'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': []}

        for animation in self.animations.keys():
            full_path = caracter_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_status(self):

        # idle
        if self.direction.x == 0 and self.direction.y == 0:
            if 'idle' not in self.status and 'attack' not in self.status:
                self.status = self.status + '_idle'

        # attack
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if 'attack' not in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
        if not self.attacking and 'attack' in self.status:
            self.status = self.status.replace('_attack', '')

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.cooldown + weapon_data[self.weapon]["cooldown"]:
                self.attacking = False
                self.destroy_attack()

        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_duartion:
                self.vulnerable = True

    def animate(self):
        animation = self.animations[self.status]

        # loop over the fame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

        # flicker
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def get_full_weapon_damage(self):
        base_damage = self.stats["attack"]
        weapon_damage = weapon_data[self.weapon]["damage"]
        return base_damage + weapon_damage

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
