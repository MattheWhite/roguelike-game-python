import pygame
import settings as Set


class UI:
    def __init__(self):

        # general
        self.display_surface = pygame.display.get_surface()
        self.exp_font = pygame.font.Font(Set.UI_FONT, Set.UI_FONT_SIZE)
        self.stats_font = pygame.font.Font(Set.UI_FONT, Set.UI_HEALTH_FONT_SIZE)

    def show_stats(self, text, current, max, rect_pos, text_color):
        text_surf = self.stats_font.render(f"{text}  :  {max} / {int(current)}", False, text_color)
        text_rect = text_surf.get_rect(topleft=rect_pos)

        pygame.draw.rect(self.display_surface, Set.UI_BG_COLOR, text_rect.inflate(15, 15))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, Set.UI_BORDER_COLOR, text_rect.inflate(15, 15), 3)

    def show_exp(self, exp):
        text_surf = self.exp_font.render(f'exp : {int(exp)}', False, Set.TEXT_COLOR)
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surf.get_rect(bottomright=(x, y))

        pygame.draw.rect(self.display_surface, Set.UI_BG_COLOR, text_rect.inflate(15, 15))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, Set.UI_BORDER_COLOR, text_rect.inflate(15, 15), 3)

    def display(self, player):
        self.show_stats('Health', player.health, player.stats['health'], (20, 35), Set.HEALTH_TEXT_COLOR)
        self.show_exp(player.exp)
