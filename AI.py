'''
when write codes, it is important to write down map&analysis of the logic chain and spatial&temporal relationship between different code chunk. Plan and adjust your plan throughout the whole coding.
在写代码之前，先做好时间空间复杂度分析，让自己心中有数

The theoretical highest score should near 1640 (if you always count one marisa as 1 point), or 31885837205464 (if the score_scale is 2)
'''

import pygame

import game_function as gf

from settings import Settings

from usm import Soumao

from marisa import Marisa

from pygame.sprite import Group

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard

def run_game():
	# Initial the game and create the game screen
	pygame.init()
	# 经验：it creates an instance in order to use the functions contains in Settings class
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption('Japari Park')
	
	# Make the Play button
	play_button = Button(ai_settings, screen, 'Play')
	
	# create the LS
	soumao = Soumao(ai_settings, screen)
	marisa = Marisa (ai_settings, screen)
	
	# Make a group to store bullets
	bullets = Group()
	
	# Make a group of marisa
	marisas = Group()
	
	# Create a fleet of marisas
	gf.create_fleet(ai_settings, screen, marisas, soumao)
	
	# Create an instance to store game statistics and create a scoreboard
	stats = GameStats(ai_settings)
	sb = Scoreboard(screen, ai_settings, stats)
	
	# Strat the main loop
	while True:
		# Take action fot the mouse&keyboard event
		gf.check_events(ai_settings, screen, stats, play_button, soumao, marisas, bullets, sb)
		
		# Redraw the screen during each time pass the loop
		gf.update_screen(ai_settings, screen, stats, sb, soumao, marisas, bullets, play_button)
		
		# Keep the game inactive when soumao_limit is lower than 0 and therefore game_active is False 
		if stats.game_active == True:
			soumao.update()
			marisa.update()
			bullets.update()
		
		# Update the position of bullets and 	delete unnecessary bullets
			gf.update_bullets(bullets, marisas, ai_settings, screen, soumao, stats, sb)
		
		# Update the position of marisas, include the drop, single-direction movement, direction change when hit edges, etc.
			gf.update_marisas(ai_settings, screen, stats, soumao, marisas, bullets, sb)
		
run_game()

