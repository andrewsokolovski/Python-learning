import pygame

class Smth():
    def __init__(self, ai_game):
        self.screen = ai_game
        self.screen_rect = ai_game.get_rect()

        # Load ship drawing and get rectangle
        self.image = pygame.image.load('images/particle.jpg')
        self.image = pygame.transform.scale(self.image, (80, 70))
        self.rect = self.image.get_rect()
        # Every ship shows up at the bottom of the edge
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """ drawing ship in current position """
        self.screen.blit(self.image, self.rect)

