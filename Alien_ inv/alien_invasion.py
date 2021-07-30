import sys

import pygame


class AlienInvasion:
    """  Class for management of game resoerses """
    def __init__(self):
        """ That is initialaizing game and create resourses of game"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        #Color of becgraund
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """ Launch the mane game"""
        while True:
            # Follow events of keyboard and mouth
            for event in pygame.event.get():
                if event.type == pygame.QUITE:
                    sys.exit()

                # Each cicle run the scree redraw
                self.screen.fill(self.bg_color)


            #Reflects the last drawing screen.
            pygame.display.flip()


if __name__== '__main__':
    # instance create and launch the game
    ai = AlienInvasion()
    ai.run_game()
    
    
