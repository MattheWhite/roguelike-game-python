import pygame
import settings as set
from random import randint


class MagicPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player
        self.sounds = {
            'heal': pygame.mixer.Sound('audio/heal.wav'),
            'flame': pygame.mixer.Sound('audio/Fire.wav')
        }

    def heal(self, player, strength, cost, groups):
        if player.energy >= cost:
            self.sounds['heal'].play()
            player.health += strength
            player.energy -= cost
            if player.health >= player.stats["health"]:
                player.health = player.stats["health"]
            self.animation_player.create_particles("aura", player.rect.center, groups)
            self.animation_player.create_particles("heal", player.rect.center, groups)

    def flame(self, player, cost, groups):
        if player.energy >= cost:
            self.sounds['flame'].play()
            player.energy -= cost
            if player.status.split("_")[0] == "right":
                direction = pygame.math.Vector2(1, 0)
            elif player.status.split("_")[0] == "left":
                direction = pygame.math.Vector2(-1, 0)
            elif player.status.split("_")[0] == "up":
                direction = pygame.math.Vector2(0, -1)
            else:
                player.status.split("_")[0] == "down"
                direction = pygame.math.Vector2(0, 1)

            for i in range(1, 6):
                if direction.x:
                    offset_x = (direction.x * i)*set.TILESIZE
                    x = player.rect.centerx + offset_x + randint(-set.TILESIZE // 3, set.TILESIZE // 3)
                    y = player.rect.centery + randint(-set.TILESIZE // 3, set.TILESIZE // 3)
                    self.animation_player.create_particles("flame", (x, y), groups)
                else:
                    offset_y = (direction.y * i)*set.TILESIZE
                    x = player.rect.centerx + randint(-set.TILESIZE // 3, set.TILESIZE // 3)
                    y = player.rect.centery + offset_y + randint(-set.TILESIZE // 3, set.TILESIZE // 3)
                    self.animation_player.create_particles("flame", (x, y), groups)
