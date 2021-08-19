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

        self.ship = Ship(self)




    def run_game(self):
        """ Launch the mane game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
         # Follow events of keyboard and mouth
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # move the sheep to the right.
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False



    def _update_screen(self):
        """ Each cicle run the scree redraw """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #Reflects the last drawing screen.
        pygame.display.flip()


if __name__ == '__main__':
    # instance create and launch the game
    ai = AlienInvasion()
    ai.run_game()
