import pygame
import settings as set


class Upgrade:
    def __init__(self,player):

		# general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.attribute_nr = len(player.stats)
        self.attribute_names = list(player.stats.keys())
        self.max_values = list(player.max_stats.values())
        self.font = pygame.font.Font(set.UI_FONT, set.UI_FONT_SIZE)

        # # item creation
        # self.height = self.display_surface.get_size()[1] * 0.8
        # self.width = self.display_surface.get_size()[0] // 6
        # self.create_items()

        # # selection system
        # self.selection_index = 0
        # self.selection_time = None
        # self.can_move = True

    def display(self):
        self.display_surface.fill('black')