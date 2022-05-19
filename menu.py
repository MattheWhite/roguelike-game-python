import pygame
import sys
from level import Level


class Menu:
    def __init__(self,) -> None:
        self.display_surf = pygame.display.get_surface()
        self.level = Level()
        self.font = pygame.font.Font("graph/font/game_font.ttf", 50)
        self.exit_surf = self.font.render("EXIT", False, 'black')
        self.exit_rect = self.exit_surf.get_rect(center=(800, 500))
        self.start_surf = self.font.render("START", False, 'black')
        self.start_rect = self.start_surf.get_rect(center=(800, 300))
        self.background = pygame.image.load('menu/ninja.png').convert_alpha()
        self.background_rect = self.background.get_rect(topleft=(0, 0))
        self.close_menu = False

    def choose_options(self):
        m_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if self.exit_rect.collidepoint(mouse_pos) and m_buttons[0]:
            pygame.quit()
            sys.exit()
        if self.start_rect.collidepoint(mouse_pos) and m_buttons[0]:
            self.close_menu = True
        if self.close_menu:
            self.level.run()

    def draw_options(self):
        self.display_surf.blit(self.background, self.background_rect)
        pygame.draw.rect(self.display_surf, 'white', self.exit_rect.inflate(20, 20))
        pygame.draw.rect(self.display_surf, 'black', self.exit_rect.inflate(20, 20), 5)
        self.display_surf.blit(self.exit_surf, self.exit_rect)
        pygame.draw.rect(self.display_surf, 'white', self.start_rect.inflate(20, 20))
        pygame.draw.rect(self.display_surf, 'black', self.start_rect.inflate(20, 20), 5)
        self.display_surf.blit(self.start_surf, self.start_rect)

    def run(self):
        self.draw_options()
        self.choose_options()
