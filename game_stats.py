from pygame.sprite import Sprite
import pygame as pg
import random as rd
import time

class GameStats:
	'''Manage all game statistics'''

	def __init__(self, spacewar):
		self.settings = spacewar.settings
		self.nb_lifes = self.settings.nb_ships
		self.game_on = False
		self.can_lose_life = True
		self.last_hit = time.time()
		self.got_hit = False
		self.score = 0
		self.is_dead = False
		self.stop = False



class Background(Sprite):
	def __init__(self, spacewar):
		super().__init__()
		self.screen = spacewar.screen
		self.settings = spacewar.settings
		self.stats = spacewar.stats

		self.color = (255, 255, 255)
		self.nb_sprites = 150
		self.sprites = []
		for i in range(self.nb_sprites):
			size = 1
			position = (
				rd.randint(0, self.settings.screen_width),
			    rd.randint(0, self.settings.screen_height))
			rect = pg.Rect(0, 0, size, size)
			rect.x = position[0]
			rect.y = position[1]
			self.sprites.append(rect)

	def update(self):
		for sprite in self.sprites:
			sprite.y += 2
			if sprite.y > self.settings.screen_height:
				sprite.y = 0
	
	def blit(self):
		self.screen.fill(self.settings.bg_color)
		for sprite in self.sprites:
			radius = rd.randint(1, 2)
			pg.draw.circle(self.screen, self.color, sprite.center, radius)
			                                                    



class LifeBar(Sprite):
	''' Dis'''
	def __init__(self, spacewar):
		super().__init__()
		self.screen = spacewar.screen
		self.settings = spacewar.settings
		self.stats = spacewar.stats

		self.sprites = []
		for i in range(self.settings.nb_ships):
			new_sprite = pg.image.load("assets/heart_pix.bmp")
			new_sprite = pg.transform.scale(new_sprite, (20, 20))
			self.sprites.append(new_sprite)
	
	def update(self):
		if self.stats.nb_lifes > 0 and self.stats.can_lose_life:
			if self.stats.got_hit == False:  # Check if the player got hit recently
				return
			if time.time() - self.stats.last_hit > self.settings.lifelost_delay:
				self.stats.last_hit = time.time()
				if self.sprites:
					self.sprites.pop()
				self.stats.nb_lifes -= 1
				self.stats.got_hit = False  # Reset got_hit flag

	def blit(self):
		x = -30
		screen_rect = self.screen.get_rect()
		for item in self.sprites:
			rect = item.get_rect()
			rect.center = screen_rect.midtop
			rect.y += 60
			rect.x += x
			self.screen.blit(item, rect)
			x += 30



class Score:
	def __init__(self, spacewar):
		self.screen = spacewar.screen
		self.settings = spacewar.settings
		self.stats = spacewar.stats
		
		self.font = pg.font.Font('freesansbold.ttf', 32)
		self.color = self.settings.score_color
		
	def blit(self):
		screen_rect = self.screen.get_rect()
		score_text = f"{self.stats.score}"
		text_surface = self.font.render(score_text, True, self.color)
		text_rect = text_surface.get_rect()
		text_rect.center = screen_rect.midtop
		text_rect.y += 30
		self.screen.blit(text_surface, text_rect)



class Menu:
	def __init__(self, spacewar):
		self.screen = spacewar.screen
		self.settings = spacewar.settings
		self.stats = spacewar.stats
		self.prompt = self.settings.prompt

		self.font = pg.font.Font('freesansbold.ttf', 20)
		self.color = (255, 255, 255)
		self.text = self.font.render(self.prompt, True, self.color)
		self.rect = self.text.get_rect()

	def get_key_event(self):
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				self.stats.game_on = True

	def display(self):
		if self.stats.game_on == True:
			return
		screen_rect = self.screen.get_rect()
		self.rect.center = screen_rect.center
		self.screen.blit(self.text, self.rect)
		self.get_key_event()


