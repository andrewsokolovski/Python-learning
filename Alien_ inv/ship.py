import pygame

class Ship():
	""" class for ship running """
	def __init__(self, ai_game):
		""" init ship and assign start posission """
		self.screen = ai_game
		self.screen_rect = ai_game.get_rect()

		#Load ship drawing and get rectangle
		self.image = pygame.image.load('images/ship1.jpg')
		self.image = pygame.transform.scale(self.image, (80, 70))
		self.rect = self.image.get_rect()

		#Every ship shows up at the bottom of the edge
		self.rect.midbottom = self.screen_rect.midbottom

		#Flag of moving
		self.moving_right = False
		self.moving_left = False

	def update(self):
		""" Update ship position in according to the flag"""
		if self.moving_right:
			self.rect.x += 1
		elif self.moving_left:
			self.rect.x -= 1

	def blitme(self):
		""" drawing ship in current position """
		self.screen.blit(self.image, self.rect)



