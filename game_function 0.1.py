import sys

import pygame

def check_events(soumao):
	# Take action fot the mouse&keyboard event
	for event in pygame.event.get():
		# Quit action
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				soumao.moving_right = True
				# Move the LS to the right by single press
				#soumao.rect.centerx += 10
			elif event.key == pygame.K_LEFT:
				soumao.moving_left = True
				# Move the LS to the left by single press
				#soumao.rect.centerx -= 10

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				soumao.moving_right = False
			elif event.key == pygame.K_LEFT:
				soumao.moving_left = False

def update_screen(ai_settings, screen, soumao):
	# Redraw the screen during each time pass the loop
	screen.fill(ai_settings.bg_color)
	soumao.blitme()