import pygame
import sys
from level import Level


class Menu:
    def __init__(self,) -> None:
        self.display_surf = pygame.display.get_surface()
        self.width = self.display_surf.get_size()[0]
        self.heigth = self.display_surf.get_size()[1]
        self.level = Level()
        self.font = pygame.font.Font("graph/font/game_font.ttf", 50)
        self.exit_surf = self.font.render("EXIT", False, 'black')
        self.exit_rect = self.exit_surf.get_rect(center=(self.width * 0.5, self.heigth * 0.75))
        self.start_surf = self.font.render("START", False, 'black')
        self.start_rect = self.start_surf.get_rect(center=(self.width * 0.5, self.heigth * 0.55))
        self.background = pygame.image.load('menu/ninja.png').convert_alpha()
        self.background_rect = self.background.get_rect(topleft=(0, 0))
        self.close_menu = False

    def choose_options(self):
        m_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if self.exit_rect.collidepoint(mouse_pos) and m_buttons[0]:
            print('you suck')
            pygame.quit()
            sys.exit()
        if self.start_rect.collidepoint(mouse_pos) and m_buttons[0]:
            self.close_menu = True
        if self.close_menu:
            self.exit_rect.x = 4000
            self.display_surf.fill('black')
            self.level.run()

    def draw_options(self):
        mouse_pos = pygame.mouse.get_pos()

        self.display_surf.blit(self.background, self.background_rect)
        pygame.draw.rect(self.display_surf, 'white', self.exit_rect.inflate(20, 20))
        self.display_surf.blit(self.exit_surf, self.exit_rect)
        pygame.draw.rect(self.display_surf, 'white', self.start_rect.inflate(20, 20))
        self.display_surf.blit(self.start_surf, self.start_rect)
        if self.exit_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.display_surf, 'gold', self.exit_rect.inflate(20, 20), 5)
        else:
            pygame.draw.rect(self.display_surf, 'black', self.exit_rect.inflate(20, 20), 5)
        if self.start_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.display_surf, 'gold', self.start_rect.inflate(20, 20), 5)
        else:
            pygame.draw.rect(self.display_surf, 'black', self.start_rect.inflate(20, 20), 5)

    def run(self):
        self.choose_options()
        if not self.close_menu:
            self.draw_options()
