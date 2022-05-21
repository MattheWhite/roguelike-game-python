import pygame
import settings as set
import sys
import debug


class Upgrade:
    def __init__(self, player):

        # general setup
        self.display_surf = pygame.display.get_surface()
        self.player = player
        self.font = pygame.font.Font(set.UI_FONT, 50)
        self.background = pygame.image.load('menu/ninja_raw.png').convert_alpha()
        self.background_rect = self.background.get_rect(topleft=(0, 0))

        # screen size
        self.height = self.display_surf.get_size()[1]
        self.width = self.display_surf.get_size()[0]

        # selextion system
        self.selection_time = None
        self.can_click = True

    def item_creation(self, player):

        self.attack_surf = self.font.render("ATTACK", False, "white")
        self.attack_rect = self.attack_surf.get_rect(topleft=(self.width*0.02, self.height*0.05))
        self.maxattack_surf = self.font.render(f"max: {player.max_stats['attack']}/ current:{player.stats['attack']}", False, "white")
        self.maxattack_rect = self.maxattack_surf.get_rect(topleft=(self.width*0.2, self.height*0.05))

        self.health_surf = self.font.render("HEALTH", False, "white")
        self.health_rect = self.health_surf.get_rect(topleft=(self.width*0.02, self.height*0.25))
        self.maxhealth_surf = self.font.render(f"max: {player.max_stats['health']}/ current:{player.stats['health']}", False, "white")
        self.maxhealth_rect = self.maxhealth_surf.get_rect(topleft=(self.width*0.2, self.height*0.25))

        self.energy_surf = self.font.render("ENERGY", False, "white")
        self.energy_rect = self.energy_surf.get_rect(topleft=(self.width*0.02, self.height*0.45))
        self.maxenergy_surf = self.font.render(f"max: {player.max_stats['energy']}/current:{player.stats['energy']}", False, "white")
        self.maxenergy_rect = self.maxenergy_surf.get_rect(topleft=(self.width*0.2, self.height*0.45))

        self.magic_surf = self.font.render("MAGIC", False, "white")
        self.magic_rect = self.magic_surf.get_rect(topleft=(self.width*0.02, self.height*0.65))
        self.maxmagic_surf = self.font.render(f"max: {player.max_stats['magic']}/current:{player.stats['magic']}", False, "white")
        self.maxmagic_rect = self.maxmagic_surf.get_rect(topleft=(self.width*0.2, self.height*0.65))

        self.speed_surf = self.font.render("SPEED", False, "white")
        self.speed_rect = self.speed_surf.get_rect(topleft=(self.width*0.02, self.height*0.85))
        self.maxspeed_surf = self.font.render(f"max: {player.max_stats['speed']}/current:{player.stats['speed']}", False, "white")
        self.maxspeed_rect = self.maxspeed_surf.get_rect(topleft=(self.width*0.2, self.height*0.85))

        self.exit_surf = self.font.render("EXIT", False, "white")
        self.exit_rect = self.exit_surf.get_rect(topright=(self.width-40, self.height*0.04))

    def selection_cooldown(self):
        if not self.can_click:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_click = True

    def draw_options(self):
        pygame.draw.rect(self.display_surf, 'black', self.exit_rect.inflate(20, 20))
        pygame.draw.rect(self.display_surf, 'grey', self.exit_rect.inflate(20, 20), 5)
        self.display_surf.blit(self.exit_surf, self.exit_rect)

        pygame.draw.rect(self.display_surf, 'black', self.attack_rect.inflate(20, 20))
        self.display_surf.blit(self.attack_surf, self.attack_rect)
        pygame.draw.rect(self.display_surf, 'grey', self.attack_rect.inflate(20, 20), 5)
        pygame.draw.rect(self.display_surf, 'black', self.maxattack_rect.inflate(20, 20))
        self.display_surf.blit(self.maxattack_surf, self.maxattack_rect)
        pygame.draw.rect(self.display_surf, 'grey', self.maxattack_rect.inflate(20, 20), 5)

        pygame.draw.rect(self.display_surf, 'black', self.health_rect.inflate(20, 20))
        self.display_surf.blit(self.health_surf, self.health_rect)
        pygame.draw.rect(self.display_surf, 'grey', self.health_rect.inflate(20, 20), 5)
        pygame.draw.rect(self.display_surf, 'black', self.maxhealth_rect.inflate(20, 20))
        self.display_surf.blit(self.maxhealth_surf, self.maxhealth_rect)
        pygame.draw.rect(self.display_surf, 'grey', self.maxhealth_rect.inflate(20, 20), 5)

        pygame.draw.rect(self.display_surf, 'black', self.energy_rect.inflate(20, 20))
        self.display_surf.blit(self.energy_surf, self.energy_rect)
        pygame.draw.rect(self.display_surf, 'grey', self.energy_rect.inflate(20, 20), 5)
        pygame.draw.rect(self.display_surf, 'black', self.maxenergy_rect.inflate(20, 20))
        self.display_surf.blit(self.maxenergy_surf, self.maxenergy_rect)
        pygame.draw.rect(self.display_surf, 'grey', self.maxenergy_rect.inflate(20, 20), 5)

        pygame.draw.rect(self.display_surf, 'black', self.magic_rect.inflate(20, 20))
        self.display_surf.blit(self.magic_surf, self.magic_rect)
        pygame.draw.rect(self.display_surf, 'grey', self.magic_rect.inflate(20, 20), 5)
        pygame.draw.rect(self.display_surf, 'black', self.maxmagic_rect.inflate(20, 20))
        self.display_surf.blit(self.maxmagic_surf, self.maxmagic_rect)
        pygame.draw.rect(self.display_surf, 'grey', self.maxmagic_rect.inflate(20, 20), 5)

        pygame.draw.rect(self.display_surf, 'black', self.speed_rect.inflate(20, 20))
        self.display_surf.blit(self.speed_surf, self.speed_rect)
        pygame.draw.rect(self.display_surf, 'grey', self.speed_rect.inflate(20, 20), 5)
        pygame.draw.rect(self.display_surf, 'black', self.maxspeed_rect.inflate(20, 20))
        self.display_surf.blit(self.maxspeed_surf, self.maxspeed_rect)
        pygame.draw.rect(self.display_surf, 'grey', self.maxspeed_rect.inflate(20, 20), 5)

    def chosse_upgrade(self, player):
        m_button = pygame.mouse.get_pressed()
        m_pos = pygame.mouse.get_pos()

        if self.exit_rect.collidepoint(m_pos):
            pygame.draw.rect(self.display_surf, 'gold', self.exit_rect.inflate(20, 20), 5)
            if m_button[0]:
                pygame.quit()
                sys.exit()

        if self.attack_rect.collidepoint(m_pos):
            pygame.draw.rect(self.display_surf, 'gold', self.attack_rect.inflate(20, 20), 5)
            if player.exp >= player.upgrade_cost:
                if m_button[0] and self.can_click:
                    self.selection_time = pygame.time.get_ticks()
                    self.can_click = False
                    player.exp -= player.upgrade_cost
                    player.stats['attack'] += 1

        if self.health_rect.collidepoint(m_pos):
            pygame.draw.rect(self.display_surf, 'gold', self.health_rect.inflate(20, 20), 5)
            if player.exp >= player.upgrade_cost:
                if m_button[0] and self.can_click:
                    self.selection_time = pygame.time.get_ticks()
                    self.can_click = False
                    player.exp -= player.upgrade_cost
                    player.stats['health'] += 10

        if self.energy_rect.collidepoint(m_pos):
            pygame.draw.rect(self.display_surf, 'gold', self.energy_rect.inflate(20, 20), 5)
            if player.exp >= player.upgrade_cost:
                if m_button[0] and self.can_click:
                    self.selection_time = pygame.time.get_ticks()
                    self.can_click = False
                    player.exp -= player.upgrade_cost
                    player.stats['energy'] += 10

        if self.magic_rect.collidepoint(m_pos):
            pygame.draw.rect(self.display_surf, 'gold', self.magic_rect.inflate(20, 20), 5)
            if player.exp >= player.upgrade_cost:
                if m_button[0] and self.can_click:
                    self.selection_time = pygame.time.get_ticks()
                    self.can_click = False
                    player.exp -= player.upgrade_cost
                    player.stats['magic'] += 0.5

        if self.speed_rect.collidepoint(m_pos):
            pygame.draw.rect(self.display_surf, 'gold', self.speed_rect.inflate(20, 20), 5)
            if player.exp >= player.upgrade_cost:
                if m_button[0] and self.can_click:
                    self.selection_time = pygame.time.get_ticks()
                    self.can_click = False
                    player.exp -= player.upgrade_cost
                    player.stats['speed'] *= 1.05

    def display(self):
        self.item_creation(self.player)
        self.selection_cooldown()
        self.draw_options()
        self.chosse_upgrade(self.player)
        debug.debug(self.player.stats)
