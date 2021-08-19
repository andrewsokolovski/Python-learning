import pygame


class Ship():
	""" class for ship running """
	def __init__(self, ai_game):
		""" init ship and assign start posission """
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		#self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		#Load ship drawing and get rectangle
		self.image = pygame.image.load('images/ship1.jpg')
		self.image = pygame.transform.scale(self.image, (80, 70))
		self.rect = self.image.get_rect()

		#Every ship shows up at the bottom of the edge
		self.rect.midbottom = self.screen_rect.midbottom

		#saving вещественной координаты центра коробля
		self.x = float(self.rect.x)

		#Flag of moving
		self.moving_right = False
		self.moving_left = False

	def update(self):
		""" Update ship position in according to the flag"""

		# Update atribite x of ship object, but not rect

		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
			
		elif self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		self.rect.x = self.x




	def blitme(self):
		""" drawing ship in current position """
		self.screen.blit(self.image, self.rect)



