import pygame

from pygame.sprite import Sprite

class Soumao(Sprite):
	def __init__(self, ai_settings, screen):
		''' initialize the Leptailurus serval(ls, sometimes refers as soumao) and set its original position '''
		super(Soumao, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		# load the image of LS and get its rect
		# 经验：always put the most complete directory, include the name of the hard disk each time
		self.image = pygame.image.load('C:/Python/project/usmw.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Start each new soumao at the bottom center of the screen.
		# 经验：when using centerx, it will put you in the top-left/right corner, but use center will put you in the direct left
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom  = self.screen_rect.bottom
		# Store a decimal value for the soumao's center
		self.center = float(self.rect.centerx)
		
		# Set the flag to judge continuous movement of the LS:
		self.moving_right = False
		self.moving_left = False

	def update(self):
		'''Update LS's position based on movement flag.'''
		# actually is to judge whether 'self.moving_right/left== True:'
		# Update the ship's center value, not the rect
		# 经验： and is used to block two parts of code, the front part and the back part are two different if sentence
		if self.moving_right == True and self.rect.right < self.screen_rect.right + self.rect.width: 
			self.center += self.ai_settings.soumao_speed_factor
		elif self.moving_left == True and self.rect.left > -self.rect.width:
			self.center -= self.ai_settings.soumao_speed_factor
		
		# Update rect object from self.center
		self.rect.centerx = self.center
	
	def center_soumao(self):
		''' Center the ship on the bottom of the screen. '''
		self.center = self.screen_rect.centerx
	
	def blitme(self):
		'''Draw the soumao at its current location'''
		self.screen.blit(self.image, self.rect)
