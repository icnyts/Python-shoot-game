import sys

import pygame

from bullet import Bullet

from marisa import Marisa

from random import randint

from time import sleep

# Optional mission: create a bullets type which destroy marisa and continue fly through the whole screen

def update_bullets(bullets, marisas, ai_settings, screen, soumao, stats, sb):
	'''Update position of the bullets and delete bullets out of screen '''
	# Update bullets position
	bullets.update()
	
	# Delete the bullets go outside the screen
	for bullet in bullets:
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
				#print (len(bullets))
		
	check_bullet_marisa_collisions(bullets, marisas, ai_settings, screen, soumao, stats, sb)
	
def check_bullet_marisa_collisions(bullets, marisas, ai_settings, screen, soumao, stats, sb):
	''' Respond to bullet-marisa collisions. '''
	# Record rects of overlap bullets and marisas. 
	# Delete overlap bullets and marisas
	collisions = pygame.sprite.groupcollide(bullets, marisas, True, True)
	# Create two type of bullets, one disappear when hit marisa, second continue fly untill goes out of screen.
	
	# Scoring when a marisa is collided with bullet
	if collisions:
		for marisas in collisions.values():
			stats.score += ai_settings.marisa_points * len(marisas)
			#print (stats.score)
			sb.prep_score()
		check_high_score(stats, sb)
		
	
	marisa = Marisa(ai_settings, screen)
	marisa_number_x = get_marisa_line(ai_settings, marisa.rect.width)
	number_rows = get_marisa_row(ai_settings, soumao.rect.height, marisa.rect.height)
	
	if len(marisas) == 0:
		# Destroy all existing bullets and create new fleet
		bullets.empty()
		ai_settings.increase_speed()
		
		# If the entire fleet is destroyed, increase a game level
		stats.level += 1
		sb.prep_level()
		# Call prep_level() to make sure the new level is displayed correctly
		
		create_fleet(ai_settings, screen, marisas, soumao)
	
	'''
	# Attampt to randomly create marisa when one is removed
	all_marisa = (number_rows * marisa_number_x)
	print(all_marisa)
	print(len(marisas))
	if len(marisas) < all_marisa:
		marisa_random = Marisa(ai_settings, screen)
		marisa_random.rect.x = randint(-800, 800)
		marisa_random.rect.y = randint(0,1000)
		marisas.add(marisa_random)
	主要疑问：为什么随机产生的marisa只在极小范围内的x轴内？
	originally attribute to problem of the range of x, while appears to wrong. Since randon number of x-axist is between -800 to 800, but new-created marisa still limit to small range of x-axis.
	'''
	
def fire_bullet(ai_settings, screen, soumao, bullets):
	''' fire a bullets if the limit is not reached '''
	# Create a new bullets and add it to the group
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(ai_settings, screen, soumao)
		bullets.add(new_bullet)
	
	

def get_marisa_line(ai_settings, marisa_width):
	''' Get the number of marisa in a row '''
	available_space_x = ai_settings.screen_width - 2 * marisa_width
	marisa_number_x = int(available_space_x / (2 * marisa_width))
	return marisa_number_x

def get_marisa_row(ai_settings, soumao_height, marisa_height):
	''' Determine the number of rows of marisa that fit the screen '''
	available_space_y = (ai_settings.screen_height - (3 * marisa_height) - soumao_height)
	number_rows = int(available_space_y / (2 * marisa_height))
	#print(number_rows)
	#print(soumao_height)
	#print (marisa_height)
	return number_rows
	
def create_marisa(ai_settings, screen, marisas, marisa_number, row_number):
	''' Create a marisa and put her in the row. '''
	marisa = Marisa(ai_settings, screen)
	marisa_width = marisa.rect.width
	marisa.x = marisa_width + 2 * marisa_width * marisa_number
	marisa.rect.x = marisa.x
	marisa.y = marisa.rect.height + 2 * marisa.rect.height * row_number
	marisa.rect.y = marisa.y
	#经验：the reason why only a single row of marisa will be drawn is when call 'marisas.draw(screen)', python will draw every sprite under marisas by their different coordinator, which comes from the attribute of rect. so marisa.y is only a attribute for instance marisa, but won't recorded into the rect as their spatial coordinator.
	marisas.add(marisa)
	
def create_fleet(ai_settings, screen, marisas, soumao):
	''' Create a fleet of marisa to destroy whole chewan. '''
	# Create a marisa and find number of marisa in a row.
	# One width/height of marisa between each of them.
	marisa = Marisa(ai_settings, screen)
	
	marisa_number_x = get_marisa_line(ai_settings, marisa.rect.width)
	number_rows = get_marisa_row(ai_settings, soumao.rect.height, marisa.rect.height)
	
	# Create a fleet of marisa
	#print (number_rows)
	#print (marisa_number_x)
	for row_number in range(number_rows):
		for marisa_number in range(marisa_number_x):
			create_marisa(ai_settings, screen, marisas, marisa_number, row_number)
	# These two loop first decide the y-coordinate of first row by outter loop and then draw a line of marisa by the inner loop. Repeat this process by the definition given in 'create_marisa' .
	
def change_fleet_direction(ai_settings, marisas):
	''' Drop the entire fleet and change fleet's direction. '''
	for marisa in marisas.sprites():
		marisa.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, marisas):
	''' Respond appropriately when any marisa has hit the edges. '''
	for marisa in marisas.sprites():
		if marisa.check_edges() == True:
			change_fleet_direction(ai_settings, marisas)
			break

def soumao_hit(ai_settings, screen, stats, marisas, bullets, soumao, sb):
	'''Respond to soumao being hit by the marisa and refresh the whole screen. '''
	if stats.soumao_left > 0:
		# Decrement soumao_left
		stats.soumao_left -= 1
		#stats.soumao_left = stats.soumao_left - 1/8
		print (stats.soumao_left)
		
		# Update scoreboard
		sb.prep_soumaos()
		
		'''
		1: Code will execute this command 8 times, hence cause the left number be deducted 8, rather than 1. Therefore I wrote 1/8 as a temporary measurement, but the reason need to be found.
		
		2: Seems like problem of soumao_hit, for when this code executed before there comes a long gip, much longer than 0.5... wait, it stop 4 seconds each time there coems a hit or out of bottom, which means this code chunk has been executed 8 times.
		
		3: I guess it should be the problem of the 'while' main loop in the AI.py.
		
		4: Second attemp turns problem is caused by missing break command of the loop of 157. since one line contains 8 marisas, so when a line of marisas hit the bottom, the loop will count 8 marisas hit the bottom the same time, therefore execute line 127 8 times. when with break, when codes are executed and try to loop, it will be 'break' by break command.
		
		5: problem solved, logs keep.
		'''
	
		# Empty the list of marisas and bullets
		marisas.empty()
		bullets.empty()
		
		# Refresh the whole screen, include create a new fleet and recenter the soumao.
		create_fleet(ai_settings, screen, marisas, soumao)
		soumao.center_soumao()
	
		# Pause to give player time to react
		sleep(0.5)
	
	else:
		stats.game_active = False
		pygame.mouse.set_visible (True)
	
def check_aliens_bottom(ai_settings, stats, screen, soumao, marisas, bullets, sb):
	''' Check if any marisa has hit the bottom of the screen. '''
	screen_rect = screen.get_rect()
	for marisa in marisas.sprites():
		if marisa.rect.bottom >= screen_rect.bottom:
			# Treat as the same as the soumao get hit
			soumao_hit(ai_settings, screen, stats, marisas, bullets, soumao, sb)
			print ('a marisa escaped, mission failed')
			break
	
def update_marisas(ai_settings, screen, stats, soumao, marisas, bullets, sb):
	''' Update the position of all marisa under the group of marisas. '''
	'''
	this code chunk has the problem that codes in response to detect soumao-marisa collision never executed. this problem is caused by order between codes. the codes in response of checking marisas who reach bottom come first, and I make the drop speed very high(200), so it will pass through soumao and directly reach the bottom, therefore restart the whole game. 
	'''
	check_fleet_edges(ai_settings, marisas)
	#print(len(marisas))
	marisas.update()
	
	# Look for marisa-soumao collision
	if pygame.sprite.spritecollideany(soumao, marisas):
		# when marisa hit soumao, these codes are not executed, but which one do the job of this code?
		# since these codes come after the code of check_aliens_bottom, so marisas pass through soumao and reach the bottom, restart the game. Hence cause the illusion of marisa-soumao collision cause the game restart. 
		soumao_hit(ai_settings, screen, stats, marisas, bullets, soumao, sb)
		print ('my my my... pity soumao is hit')
	
	
	check_aliens_bottom(ai_settings, stats, screen, soumao, marisas, bullets, sb)

		

def check_keydown_event(event, ai_settings, screen, soumao, bullets):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			soumao.moving_right = True
			# Move the LS to the right by single press
			#soumao.rect.centerx += 10
		elif event.key == pygame.K_LEFT:
			soumao.moving_left = True
			# Move the LS to the left by single press
			#soumao.rect.centerx -= 10
		elif event.key == pygame.K_SPACE:
			fire_bullet(ai_settings, screen, soumao, bullets)
		elif event.key == pygame.K_q:
			sys.exit()

def check_keyup_event(event, soumao):
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_RIGHT:
			soumao.moving_right = False
		elif event.key == pygame.K_LEFT:
			soumao.moving_left = False

def check_events(ai_settings, screen, stats, play_button, soumao, marisas, bullets, sb):
	# Take action fot the mouse&keyboard event
	for event in pygame.event.get():
		# Quit action
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event, ai_settings, screen, soumao, bullets)
			# The code below will make CP print the relative codes according to what you input
			#print (event.key)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event, soumao)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, play_button, soumao, marisas, bullets, mouse_x, mouse_y, sb)
			
def check_play_button(ai_settings, screen, stats, play_button, soumao, marisas, bullets, mouse_x, mouse_y, sb):
	''' Start a new game when click the play button. '''
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		# Reset the game statistics
		stats.reset_stats()
		ai_settings.initialize_dynamic_settings()
		stats.game_active = True
	
		# Reset the scoreboard and level images
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_soumaos()
		
		# Hide the mouse cursor.
		pygame.mouse.set_visible(False)
	
		# Empty the list of marisas and bullets
		marisas.empty()
		bullets.empty()
	
		# Create a new fllet of marisa and recenter the soumao
		create_fleet(ai_settings, screen, marisas, soumao)
		soumao.center_soumao()
		
def check_high_score(stats, sb):
	''' Check if there is a new higher score. '''
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
		
def update_screen(ai_settings, screen, stats, sb, soumao, marisas, bullets, play_button):
	# Redraw the screen during each time pass the loop
	screen.fill(ai_settings.bg_color)
	
	# Redraw all bullets between LS and MS
	for bullet in bullets.sprites():
		bullet.draw_bullets()
	
	# Draw the score information
	sb.show_score()
	
	soumao.blitme()
	marisas.draw(screen)
	
	# Draw the play button is the game is inactive
	if not stats.game_active:
		play_button.draw_button()
	
	# Display the most recently drawn screen object
	pygame.display.flip()
	
	
	