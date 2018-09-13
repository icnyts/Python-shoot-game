import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
	''' A class to manage bullets fired from LS. '''
	
	def __init__(self, ai_settings, screen, soumao):
		''' Create a bullet object at LS's current posistion. '''
		super (Bullet, self). __init__()
		self.screen = screen
		
		# Create a bullet at (0, 0) position and then set correct position
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = soumao.rect.centerx
		self.rect.top = soumao.rect.top
		
		# Store the bullet's position as a decimal value
		self.y = float(self.rect.y)
		
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		''' Move the bullet upward in the scree. '''
		# Update the deicmal vertical position of bullets
		self.y -= self.speed_factor
		# Update the rectangle position of the bullets
		self.rect.y = self.y
	
	def draw_bullets(self):
		''' Draw the bullets to the screen. '''
		pygame.draw.rect(self.screen, self.color, self.rect)
	
	