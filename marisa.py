import pygame

from pygame.sprite import Sprite

class Marisa(Sprite):
	''' A class to represent single Marisa in the fleet. '''
	
	def __init__(self, ai_settings, screen):
		'''initalize the Marisa and set its starting position'''
		super (Marisa, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		# Load the Marisa image and set its rect attribute
		self.image = pygame.image.load('C:/Python/project/Marisa.bmp')
		self.rect = self.image.get_rect()
	
		# Start each new Marisa near the top left of the corner
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
	
		# Store Marisa's exact position
		self.x = float(self.rect.x)
	
	def blitme(self):
		''' Draw the Marisa at its current location'''
		self.screen.blit(self.image, self.rect)
		
	def check_edges(self):
		''' Return True when a marisa hit or cross the edge of the screen. '''
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
	
	def update(self):
		''' Move marisa to the right side of screen, change direction whenever her hit the edge of screen. '''
		self.x += (self.ai_settings.marisa_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x
		
		
		
