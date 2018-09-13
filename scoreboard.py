import pygame.font

from pygame.sprite import Group

from usm import Soumao

class Scoreboard():
	''' a class to collect&report information. '''
	
	def __init__(self, screen, ai_settings, stats):
		''' Initialize scorekeeping attributes. '''
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		# Font settings for scoring information
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		
		# Prepare the initial score image.
		self.prep_score()
		
		# Prepare the highest score image
		self.prep_high_score()
		
		# Prepare the current game level
		self.prep_level()
		
		# Prepare the left soumao image
		self.prep_soumaos()
		
	def prep_score(self):
		''' Turn the score into a rendered image. '''
		rounded_score = int(round(self.stats.score, -1))
		# When precision is negative, round will round value to nearest 10, 100, etc., depends on the negative number you input.
		score_str = '{:,}'.format(rounded_score)
		# a string formatting directive tells Python to insert commas into numbers when converting a numerical value to a string
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
		
		# Display the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
	
	def prep_high_score(self):
		''' Turn the high score into a render image. '''
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = '{:,}'.format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
		
		# Center the high score at the top of the screen
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.screen_rect.top
		
	def prep_level(self):
		''' Turn the level into a rendered image. '''
		self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
		
		# Position the level below the score.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.screen_rect.right - 20
		self.level_rect.top = self.score_rect.height*2 + 20
		
	def prep_soumaos(self):
		''' Show how many soumao are left. '''
		self.soumaos = Group()
		for soumao_number in range(self.stats.soumao_left):
			soumao = Soumao(self.ai_settings, self.screen)
			soumao.rect.x = 10 + soumao_number * soumao.rect.width
			soumao.rect.y = 10
			self.soumaos.add(soumao)
		
	def show_score(self):
		''' Draw score and level to screen. '''
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		
		# Draw soumao
		self.soumaos.draw(self.screen)