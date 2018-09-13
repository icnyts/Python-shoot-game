class GameStats():
	''' Track statistics for JP. '''
	def __init__(self, ai_settings):
		''' Initialize statistics. '''
		self.ai_settings = ai_settings
		self.reset_stats()
		# Pay attention to this usage, this will help to reset the score each time a new game starts and GameStats(Or its subclass/instance) is executed. Since reset_stats() is an attribute of this class, so reset_stats() will reset stats value.
		
		# Start JP in an active status
		self.game_active = False
		
		# High score should never be reset
		self.high_score = 0
		
	def reset_stats(self):
		''' Initialize statistics which can change during the gmae. '''
		self.soumao_left = self.ai_settings.soumao_limit
		self.score = 0
		self.level = 1