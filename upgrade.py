import pygame
import settings as set
import sys


class Upgrade:
    def __init__(self, player):

        # general setup
        self.display_surf = pygame.display.get_surface()
        self.player = player
        self.font = pygame.font.Font(set.UI_FONT, 50)

        # item creation
        self.height = self.display_surf.get_size()[1]
        self.width = self.display_surf.get_size()[0]

        self.attack_surf = self.font.render("ATTACK", False, "black")
        self.attack_rect = self.attack_surf.get_rect(topleft=(self.width*0.02, self.height*0.05))
        self.maxattack_surf = self.font.render(f"max: {self.player.max_stats['attack']}/ current:{self.player.stats['attack']}", False, "black")
        self.maxattack_rect = self.maxattack_surf.get_rect(topleft=(self.width*0.2, self.height*0.05))

        self.health_surf = self.font.render("HEALTH", False, "black")
        self.health_rect = self.health_surf.get_rect(topleft=(self.width*0.02, self.height*0.25))
        self.maxhealth_surf = self.font.render(f"max: {self.player.max_stats['health']}/ current:{self.player.stats['health']}", False, "black")
        self.maxhealth_rect = self.maxhealth_surf.get_rect(topleft=(self.width*0.2, self.height*0.25))
        
        self.energy_surf = self.font.render("ENERGY", False, "black")
        self.energy_rect = self.energy_surf.get_rect(topleft=(self.width*0.02, self.height*0.45))
        self.maxenergy_surf = self.font.render(f"max: {self.player.max_stats['energy']}/current:{self.player.stats['energy']}", False, "black")
        self.maxenergy_rect = self.maxenergy_surf.get_rect(topleft=(self.width*0.2, self.height*0.45))

        self.magic_surf = self.font.render("MAGIC", False, "black")
        self.magic_rect = self.magic_surf.get_rect(topleft=(self.width*0.02, self.height*0.65))
        self.maxmagic_surf = self.font.render(f"max: {self.player.max_stats['magic']}/current:{self.player.stats['magic']}", False, "black")
        self.maxmagic_rect = self.maxmagic_surf.get_rect(topleft=(self.width*0.2, self.height*0.65))
        
        self.speed_surf = self.font.render("SPEED", False, "black")
        self.speed_rect = self.speed_surf.get_rect(topleft=(self.width*0.02, self.height*0.85))
        self.maxspeed_surf = self.font.render(f"max: {self.player.max_stats['speed']}/current:{self.player.stats['speed']}", False, "black")
        self.maxspeed_rect = self.maxspeed_surf.get_rect(topleft=(self.width*0.2, self.height*0.85))

        self.exit_surf = self.font.render("EXIT", False, "black")
        self.exit_rect = self.exit_surf.get_rect(bottomright=(self.width-40, self.height-40))

    def display(self):
        self.display_surf.fill('black')
        self.draw_options()
        self.chosse_upgrade()

    def draw_options(self):
        pygame.draw.rect(self.display_surf, 'white', self.exit_rect.inflate(20, 20))
        pygame.draw.rect(self.display_surf, 'grey', self.exit_rect.inflate(20, 20), 5)
        self.display_surf.blit(self.exit_surf, self.exit_rect)

        pygame.draw.rect(self.display_surf, 'white', self.attack_rect.inflate(20, 20))
        self.display_surf.blit(self.attack_surf, self.attack_rect)
        pygame.draw.rect(self.display_surf, 'grey', self.attack_rect.inflate(20, 20), 5)
        pygame.draw.rect(self.display_surf, 'white', self.maxattack_rect.inflate(20, 20))
        self.display_surf.blit(self.maxattack_surf, self.maxattack_rect)

        pygame.draw.rect(self.display_surf, 'white', self.health_rect.inflate(20, 20))
        self.display_surf.blit(self.health_surf, self.health_rect)
        pygame.draw.rect(self.display_surf, 'grey', self.health_rect.inflate(20, 20), 5)
        pygame.draw.rect(self.display_surf, 'white', self.maxhealth_rect.inflate(20, 20))
        self.display_surf.blit(self.maxhealth_surf, self.maxhealth_rect)

        pygame.draw.rect(self.display_surf, 'white', self.energy_rect.inflate(20, 20))
        self.display_surf.blit(self.energy_surf, self.energy_rect)
        pygame.draw.rect(self.display_surf, 'grey', self.energy_rect.inflate(20, 20), 5)
        pygame.draw.rect(self.display_surf, 'white', self.maxenergy_rect.inflate(20, 20))
        self.display_surf.blit(self.maxenergy_surf, self.maxenergy_rect)

        pygame.draw.rect(self.display_surf, 'white', self.magic_rect.inflate(20, 20))
        self.display_surf.blit(self.magic_surf, self.magic_rect)
        pygame.draw.rect(self.display_surf, 'grey', self.magic_rect.inflate(20, 20), 5)
        pygame.draw.rect(self.display_surf, 'white', self.maxmagic_rect.inflate(20, 20))
        self.display_surf.blit(self.maxmagic_surf, self.maxmagic_rect)

        pygame.draw.rect(self.display_surf, 'white', self.speed_rect.inflate(20, 20))
        self.display_surf.blit(self.speed_surf, self.speed_rect)
        pygame.draw.rect(self.display_surf, 'grey', self.speed_rect.inflate(20, 20), 5) 
        pygame.draw.rect(self.display_surf, 'white', self.maxspeed_rect.inflate(20, 20))
        self.display_surf.blit(self.maxspeed_surf, self.maxspeed_rect)

    def chosse_upgrade(self):
        m_button = pygame.mouse.get_pressed()
        m_pos = pygame.mouse.get_pos()

        if self.exit_rect.collidepoint(m_pos):
            pygame.draw.rect(self.display_surf, 'gold', self.exit_rect.inflate(20, 20), 5)
            if m_button[0]:
                pygame.quit()
                sys.exit()

        if self.attack_rect.collidepoint(m_pos):
            pygame.draw.rect(self.display_surf, 'gold', self.attack_rect.inflate(20, 20), 5)
            if self.player.exp >= self.player.upgrade_cost:
                if m_button[0]:
                    self.player.stats['attack'] += 5

        if self.health_rect.collidepoint(m_pos):
            pygame.draw.rect(self.display_surf, 'gold', self.health_rect.inflate(20, 20), 5)
            if self.player.exp >= self.player.upgrade_cost:
                if m_button[0]:
                    self.player.stats['health'] += 5

        if self.energy_rect.collidepoint(m_pos):
            pygame.draw.rect(self.display_surf, 'gold', self.energy_rect.inflate(20, 20), 5)
            if self.player.exp >= self.player.upgrade_cost:
                if m_button[0]:
                    self.player.stats['energy'] += 5

        if self.magic_rect.collidepoint(m_pos):
            pygame.draw.rect(self.display_surf, 'gold', self.magic_rect.inflate(20, 20), 5)
            if self.player.exp >= self.player.upgrade_cost:
                if m_button[0]:
                    self.player.stats['magic'] += 5

        if self.speed_rect.collidepoint(m_pos):
            pygame.draw.rect(self.display_surf, 'gold', self.speed_rect.inflate(20, 20), 5)
            if self.player.exp >= self.player.upgrade_cost:
                if m_button[0]:
                    self.player.stats['speed'] += 5

