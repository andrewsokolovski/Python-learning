import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """  Class for management of game resourses """
    def __init__(self):
        """ That is initialaizing game and create resourses of game"""
        pygame.init()
        self.settings = Settings()

        


        self.screen = pygame.display.set_mode(
            (self.settings.screen_widgth, self.settings.screen_heights))


        #self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion my first program")

        self.ship = Ship(self.screen)




    def run_game(self):
        """ Launch the mane game"""
        while True:
            # Follow events of keyboard and mouth
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Each cicle run the scree redraw
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()


            #Reflects the last drawing screen.
            pygame.display.flip()


if __name__ == '__main__':
    # instance create and launch the game
    ai = AlienInvasion()
    ai.run_game()
