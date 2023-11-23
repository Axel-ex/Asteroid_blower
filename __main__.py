import sys
import pygame as pg
from settings import *
from classes import Bullet
from classes import ship
from classes import thruster


class	spacewar():
	''' Clas to manage assets and behaviour'''

	def __init__(self):
		pg.init()
		self.settings = settings()
		self.screen = pg.display.set_mode((self.settings.screen_width,
										 	   self.settings.screen_length))
		pg.display.set_caption(self.settings.caption)
		self.clock = pg.time.Clock()
		self.ship = ship(self)
		self.thruster = thruster(self)
		self.bullets = pg.sprite.Group()

	def get_keydown_events(self, event):
				if event.key == pg.K_RIGHT:
					self.ship.move_right = True
				elif event.key == pg.K_LEFT:
					self.ship.move_left = True
				elif event.key == pg.K_UP:
					self.ship.move_up = True
				elif event.key == pg.K_DOWN:
					self.ship.move_down = True
				elif event.key == pg.K_z:
					self.fire_bullets()

	def get_keyup_events(self, event):
				if event.key == pg.K_RIGHT:
					self.ship.move_right = False
				elif event.key == pg.K_LEFT:
					self.ship.move_left = False
				elif event.key == pg.K_UP:
					self.ship.move_up = False
				elif event.key == pg.K_DOWN:
					self.ship.move_down = False
	
	def fire_bullets(self):
		new_bullet = Bullet(self)
		if (len(self.bullets) < self.settings.nb_bullets):
			self.bullets.add(new_bullet)

	def get_event(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
			elif event.type == pg.KEYDOWN:
				self.get_keydown_events(event)
			elif event.type == pg.KEYUP:
				self.get_keyup_events(event)
	
	def update_bullets(self):
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

	def	update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.update_bullets()
		self.ship.blitme()
		self.thruster.blit_thruster(self)
		pg.display.flip()
		
	def run_game(self):
		while True:
			self.get_event()
			self.ship.update()
			self.bullets.update()
			self.update_screen()
			self.clock.tick(30)

if __name__ == '__main__':
	sw = spacewar()
	sw.run_game()