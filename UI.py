import pygame
import settings as set


class UI:
    def __init__(self):

        # general
        self.display_surface = pygame.display.get_surface()
        self.info_font = pygame.font.Font(set.UI_FONT, set.UI_FONT_SIZE)

        # bar setup
        self.health_bar_rect = pygame.Rect(10, 70, set.HEALTH_BAR_WIDTH, set.BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 140, set.HEALTH_BAR_WIDTH, set.BAR_HEIGHT)

        # convert weapon dictionary
        self.weapon_graphics = []
        for weapon in set.weapon_data.values():
            path = weapon['graphic']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)

        # convert magic dictionary
        self.magic_graphics = []
        for magic in set.magic_data.values():
            path = magic['graphic']
            magic = pygame.image.load(path).convert_alpha()
            self.magic_graphics.append(magic)

    def show_health_info(self):
        health_text_surf = self.info_font.render('health:', False, set.TEXT_COLOR)
        health_text_rect = health_text_surf.get_rect(topleft=(10, 40))

        pygame.draw.rect(self.display_surface, set.UI_BG_COLOR, health_text_rect.inflate(15, 15))
        self.display_surface.blit(health_text_surf, health_text_rect)
        pygame.draw.rect(self.display_surface, set.UI_BORDER_COLOR, health_text_rect.inflate(15, 15), 5)

    def show_energy_info(self):
        health_text_surf = self.info_font.render('energy:', False, set.TEXT_COLOR)
        health_text_rect = health_text_surf.get_rect(topleft=(10, 110))

        pygame.draw.rect(self.display_surface, set.UI_BG_COLOR, health_text_rect.inflate(15, 15))
        self.display_surface.blit(health_text_surf, health_text_rect)
        pygame.draw.rect(self.display_surface, set.UI_BORDER_COLOR, health_text_rect.inflate(15, 15), 5)

    def show_bar(self, current, max_amount, bg_rect, color):
        # draw bg
        pygame.draw.rect(self.display_surface, set.UI_BG_COLOR, bg_rect)

        # converting stat to pixel
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # drawing the bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, set.UI_BORDER_COLOR, bg_rect, 5)

    def show_exp(self, exp):
        text_surf = self.info_font.render(f'exp : {int(exp)}', False, set.TEXT_COLOR)
        x = self.display_surface.get_size()[0] - 200
        y = self.display_surface.get_size()[1] - 50
        text_rect = text_surf.get_rect(bottomright=(x, y))

        pygame.draw.rect(self.display_surface, set.UI_BG_COLOR, text_rect.inflate(15, 15))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, set.UI_BORDER_COLOR, text_rect.inflate(15, 15), 3)

    def selection_box(self, left, top, has_switched):
        bg_rect = pygame.Rect(left, top, set.ITEM_BOX_SIZE, set.ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, set.UI_BG_COLOR, bg_rect)
        if has_switched:
            pygame.draw.rect(self.display_surface, set.UI_BORDER_COLOR_ACTIVE, bg_rect, 5)
        else:
            pygame.draw.rect(self.display_surface, set.UI_BORDER_COLOR, bg_rect, 5)
        return bg_rect

    def weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.selection_box(10, 800, has_switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center=bg_rect.center)

        self.display_surface.blit(weapon_surf, weapon_rect)

    def magic_overlay(self, magic_index, has_switched):
        bg_rect = self.selection_box(90, 700, has_switched)
        magic_surf = self.magic_graphics[magic_index]
        magic_rect = magic_surf.get_rect(center=bg_rect.center)

        self.display_surface.blit(magic_surf, magic_rect)

    def display(self, player):
        self.show_health_info()
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, set.HEALTH_COLOR)
        self.show_energy_info()
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect,  set.ENERGY_COLOR)
        self.show_exp(player.exp)
        self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
        self.magic_overlay(player.magic_index, not player.can_switch_magic)
