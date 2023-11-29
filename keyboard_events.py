import pygame as pg
import sys


class Keyboard:
	''' Handle keyboard inputs'''

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