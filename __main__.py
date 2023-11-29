import pygame as pg
import time
from settings import *
from sprite_classes import *
from keyboard_events import *
from game_stats import *

class	spacewar():
	''' Clas to manage assets and behaviour'''

	def __init__(self):
		pg.init()
		self.settings = settings()
		self.screen = pg.display.set_mode((self.settings.screen_width,
										 	   self.settings.screen_height))
		self.screen_rect = self.screen.get_rect()
		pg.display.set_caption(self.settings.caption)
		self.clock = pg.time.Clock()
		self.keyboard = Keyboard()
		self.stats = GameStats(self)
		self.menu = Menu(self)
		self.score_counter = Score(self)
		self.life_bar = LifeBar(self)

		self.background = Background(self)
		self.ship = Ship(self)
		self.thruster = Thruster(self)
		self.bullets = pg.sprite.Group()
		self.asteroids = pg.sprite.Group()
		self.explosions = pg.sprite.Group()
		self.ship_explosion = pg.sprite.Group()
		self.create_asteroids()

	# def display_menu(self):

	def create_asteroids(self):
		for i in range(self.settings.nb_asteroids):
			asteroid = Asteroid(self)
			self.asteroids.add(asteroid)

	def fire_bullets(self):
		new_bullet = Bullet(self)
		if (len(self.bullets) < self.settings.nb_bullets):
			self.bullets.add(new_bullet)
	
	def handle_collisions(self):
		collision = pg.sprite.groupcollide(self.bullets, self.asteroids, True, True)	
		for bullets, asteroids in collision.items():
			for asteroid in asteroids:
				explosion = Explosion(self, asteroid.rect.center, self.settings.explosion_sprites)
				self.explosions.add(explosion)
				self.stats.score += 10
		if pg.sprite.spritecollideany(self.ship, self.asteroids):
			self.ship.collision_update()
			self.stats.got_hit = True

	def animate_explosion(self):
		if self.stats.is_dead == False:
			return
		explosion = Explosion(self, self.ship.rect.center, self.settings.explosion_ship)
		self.ship_explosion.add(explosion)

	def update_bullets(self):
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

	def actualize_asteroids(self):
		if len(self.asteroids) == 0:
			self.settings.nb_asteroids += 5
			self.create_asteroids()

	def	update_screen(self):
		self.background.update()
		if self.stats.game_on == False:
			return
		self.life_bar.update()
		self.handle_collisions()
		self.ship.update()
		self.ship_explosion.update()
		self.actualize_asteroids()
		for asteroid in self.asteroids.sprites():
			asteroid.update()
		for explosion in self.explosions.sprites():
			explosion.update()
		self.bullets.update()
		self.thruster.update(self)
	
	def blit_next_frame(self):
		self.background.blit()
		if self.stats.game_on == True:
			self.animate_explosion()
			if (self.ship_explosion and self.stats.stop == False):
				for explo in self.ship_explosion.sprites():
					explo.blit()
			self.ship.blit()
			self.thruster.blit()
			for asteroid in self.asteroids.sprites():
				asteroid.blit()
			for explosion in self.explosions.sprites():
				explosion.blit()
			self.life_bar.blit()
			self.update_bullets()
			self.score_counter.blit()
		pg.display.flip()
		
	def run_game(self):
		while True:
			self.menu.display()
			self.keyboard.get_event(self)
			self.update_screen()
			self.blit_next_frame()
			self.clock.tick(30)

if __name__ == '__main__':
	sw = spacewar()
	sw.run_game()