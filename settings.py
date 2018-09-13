class Settings():
	''' the class to store all settings for the game alien invasion(though I like Kapari garden better)'''
	
	def __init__(self):
		''' Initialize the game's static setting '''
		# the screen settings:
		self.screen_width = 1200
		self.screen_height = 1000
		#self.bg_color = (230, 232, 200), moka color
		self.bg_color = (255, 250, 250)
		
		# Soumao settings
		self.soumao_limit = 3
		
		# Bullet settings
		self.bullet_width = 1200
		self.bullet_height = 10
		self.bullet_color = 60, 60, 60
		self.bullet_allowed = 8
		
		# Marisa settings
		self.fleet_drop_speed = 120
		
		# How quick the game speeds up
		self.speedup_scale = 1.1
		
		# How quick the score increase
		self.score_scale = 2
		
		self.initialize_dynamic_settings()
		# Finally, we call initialize_dynamic_settings() to initialize the values for attributes that need to change throughout the course of a game
	
	def increase_speed(self):
		''' Increase speed settings and marisa point values. '''
		self.soumao_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.marisa_speed_factor *= self.speedup_scale
		
		self.marisa_points = int(self.marisa_points * self.score_scale)

		
	
	def initialize_dynamic_settings(self):
		''' initialize the settings that change through time. '''
		self.soumao_speed_factor = 6
		self.bullet_speed_factor = 4
		self.marisa_speed_factor = 1
		
		# Fleet direction of 1 represents right; -1 represents left
		self.fleet_direction = 1
		
		# Scoring
		self.marisa_points = 1
	