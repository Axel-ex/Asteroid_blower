import pygame as pg
import sys
import time
from pathlib import Path

class GameStats:
	def __init__(self, spacewar):
		self.settings = spacewar.settings
		self.player_name = ""
		self.nb_lifes = self.settings.nb_ships
		self.game_on = False
		self.can_lose_life = True
		self.last_hit = time.time()
		self.got_hit = False
		self.score = 0
		self.is_dead = False
		self.stop = False
		self.reset_flag = False
		self.start_time = time.time()

	def reset(self):
		self.settings.nb_asteroids = 5
		self.score = 0
		self.nb_lifes = self.settings.nb_ships
		self.game_on = True
		self.is_dead = False
		self.stop = False
		self.reset_flag = True


class Keyboard:
	def get_keydown_events(self, event, spacewar):
			if event.key == pg.K_RIGHT:
				spacewar.ship.move_right = True
			elif event.key == pg.K_LEFT:
				spacewar.ship.move_left = True
			elif event.key == pg.K_UP:
				spacewar.ship.move_up = True
			elif event.key == pg.K_DOWN:
				spacewar.ship.move_down = True
			elif event.key == pg.K_z:
				spacewar.fire_bullets()

	def get_keyup_events(self, event, spacewar):
				if event.key == pg.K_RIGHT:
					spacewar.ship.move_right = False
				elif event.key == pg.K_LEFT:
					spacewar.ship.move_left = False
				elif event.key == pg.K_UP:
					spacewar.ship.move_up = False
				elif event.key == pg.K_DOWN:
					spacewar.ship.move_down = False

	def get_event(self, spacewar):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
			elif event.type == pg.KEYDOWN:
				self.get_keydown_events(event, spacewar)
			elif event.type == pg.KEYUP:
				self.get_keyup_events(event, spacewar)

