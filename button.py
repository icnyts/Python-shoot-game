import pygame.font

class Button():

	def __init__(self, ai_settings, screen, msg):
		''' Initialize button attributes. '''
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		# Set the dimensions and properties of the button
		self.width, self.height = 200, 50
		self.button_color = (0, 200, 0)
		#self.test_color = (100, 100, 100)
		self.text_color = (255, 255, 255)
		# None for default font, 48 for the size of text
		self.font = pygame.font.SysFont(None, 48)
		
		# Build the button's rect object
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		# what does the 0, 0 represent?
		self.rect.center = self.screen_rect.center
		#self.screen_rect.center
		
		# The button message needs to be prepped only once.
		self.prep_msg(msg)
		
	def prep_msg(self, msg):
		''' Turn msg into a rendered image and center the text on the button. '''
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		# msg represent the message delivered, True means turn on antialiasing, 3rd is for text color, 4nd is for button color
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
	
	def draw_button(self):
		# Draw blank button and then draw message.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)