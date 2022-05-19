import pygame
import sys
from settings import WIDTH, HEIGTH, FPS
from menu import Menu
from level import Level


class Game:
    def __init__(self) -> None:

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH), pygame.FULLSCREEN)
        pygame.display.set_caption("RogueLike by theboys")
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.menu = Menu()

    def run(self):
        game_is_active = True
        while game_is_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill("black")
            self.menu.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
