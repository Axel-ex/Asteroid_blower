from pygame.sprite import Sprite
import pygame as pg
import random as rd
import time
import sys
from pathlib import Path
from events import *


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
			                                                    


class Menu:
	def __init__(self, spacewar):
		self.screen = spacewar.screen
		self.settings = spacewar.settings
		self.stats = spacewar.stats
		self.prompt = self.settings.prompt
		self.score_board = ScoreBoard(spacewar)

		self.font = pg.font.Font('freesansbold.ttf', 40)
		self.color = (255, 255, 255)
		self.text = self.font.render(self.prompt, True, self.color)
		self.rect = self.text.get_rect()

		self.subfont = pg.font.Font('freesansbold.ttf', 20)
		self.subtext = self.subfont.render("press space to play, q to quit", True, self.color)
		self.subrect = self.subtext.get_rect()
		self.user_text = self.font.render("Enter your username in the terminal", True, self.color)
		self.user_text_rect = self.user_text.get_rect()

	def update_best_score(self):
		if not self.stats.score:
			return
		file = Path("../best_scores.txt")
		time_spent = time.time() - self.stats.start_time
		best_score = f"{self.stats.player_name}: {self.stats.score} in {time_spent/60:.2f} mins\n"
		file.write_text(file.read_text() + best_score)
	
	def game_over(self):
		self.text = self.font.render("GAME OVER", True, (255, 255, 255))
		self.rect = self.text.get_rect()
		if self.stats.game_on:
			self.update_best_score()
		self.stats.game_on = False
		self.get_key_event()

	def update_username(self):
		self.user_text_rect.midbottom = self.rect.midtop
		self.screen.blit(self.user_text, self.user_text_rect)
		self.user_text_rect.y -= 10
		pg.display.flip()
		self.stats.player_name = input("Enter a player name:\n")

	def get_key_event(self):
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					self.stats.reset()
					self.update_username()
				if event.key == pg.K_q or event.key == pg.QUIT:
					sys.exit()

	def display(self):
		if self.stats.game_on == True:
			return
		screen_rect = self.screen.get_rect()
		self.rect.center = screen_rect.center
		self.subrect.midtop = self.rect.midbottom
		self.screen.blit(self.text, self.rect)
		self.screen.blit(self.subtext, self.subrect)
		self.score_board.display()
		self.get_key_event()



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



class LifeBar(Sprite):
	def __init__(self, spacewar):
		super().__init__()
		self.screen = spacewar.screen
		self.settings = spacewar.settings
		self.stats = spacewar.stats
		self.sprites = []
		self.create()
	
	def create(self):
		self.sprites.clear()
		for i in range(self.settings.nb_ships):
			new_sprite = pg.image.load("../assets/heart_pix.bmp")
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



class ScoreBoard:
	def __init__(self, spacewar):
		self.screen = spacewar.screen
		self.settings = spacewar.settings
		self.stats = spacewar.stats
		self.font = pg.font.Font('freesansbold.ttf', 30)
		self.color = (255, 255, 255)
		self.scores = []
		self.text = []
		self.rects = []

	def get_scores(self):
		path = Path("../best_scores.txt")
		lines = path.read_text().splitlines()
		scores_data = []
		for line in lines[1:]:
			parts = line.split(': ')
			if len(parts) == 2:
				player_name, score_time = parts
				score, time_spent = score_time.split(' in ')
				scores_data.append({
					'player_name': player_name,
					'score': int(score),
					'time': time_spent.strip()
				})
		self.scores = sorted(scores_data, key=lambda x: x['score'], reverse=True)

	def update(self):
		self.get_scores()
		self.text.clear()
		self.rects.clear()
		for score in self.scores[:3]:
			text = self.font.render(
				f"{score['player_name']}: {score['score']} in {score['time']}",
                True,
                self.color
			)
			self.text.append(text)
			self.rects.append(text.get_rect())

	def display(self):
		self.update() 
		screen_rect = self.screen.get_rect()
		y_shift = 80
		for text, rect in zip(self.text, self.rects):
			rect.midtop = screen_rect.center
			rect.y += y_shift
			self.screen.blit(text, rect)
			y_shift += 40