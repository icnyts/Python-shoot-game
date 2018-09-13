import sys

from PIL import Image

import pygame

def run_game():
	# Initial the game and create the game screen
	pygame.init()
	screen = pygame.display.set_mode((600, 600))
	pygame.display.set_caption('kapari gardenpi')
	
	# Set the background color
	bg_color = (230, 232, 200)
	# Attempt to fill picture in_temp cold, for the fill command only accept pure color fillin
	#im = Image.open('pic.jpg')
	
	# Strat the main loop
	while True:
		# Take action fot the mouse&keyboard event
		for event in pygame.event.get():
			# Quit action
			if event.type == pygame.QUIT:
				sys.exit()
		
		# Redraw the screen during each time pass the loop
		screen.fill(bg_color)
		# Attempt to fillin pic next code
		#screen.fill(im)
		# Attempt fail, for screen.fill func only accept pure color rather than picture
		
		# Display the most recently drawn screen object
		pygame.display.flip()
		
run_game()

