import pygame as pg
from settings import *
from player import *
from destructibles import *
from events import *
from interface import *


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


	def create_asteroids(self):
		self.asteroids.empty()
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
				explosion = Explosion(self, asteroid.rect.center, self.settings.explosion_ship)
				self.explosions.add(explosion)
				self.stats.score += 10
		if pg.sprite.spritecollideany(self.ship, self.asteroids):
			self.ship.collision_update()
			self.stats.got_hit = True

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
	
	def reset(self):
		if not self.stats.reset_flag:
			return
		self.life_bar.create()
		self.create_asteroids()
		self.stats.reset_flag = False

	def	update_screen(self):
		if self.stats.reset_flag:
			self.reset()
		self.background.update()
		for asteroid in self.asteroids.sprites():
			asteroid.update()
		if self.stats.game_on == False:
			return
		self.life_bar.update()
		self.handle_collisions()
		self.ship.update()
		self.ship_explosion.update()
		self.actualize_asteroids()
		for explosion in self.explosions.sprites():
			explosion.update()
		self.bullets.update()
		self.thruster.update(self)
	
	def blit_next_frame(self):
		self.background.blit()
		self.menu.display()
		if self.stats.game_on and not self.stats.is_dead:
			self.ship.blit()
			self.thruster.blit()
			self.update_bullets()
			self.life_bar.blit()
			self.score_counter.blit()
			for explosion in self.explosions.sprites():
				explosion.blit()
		for asteroid in self.asteroids.sprites():
			asteroid.blit()
		if self.stats.is_dead and not self.stats.stop:
			self.ship.animate_death()
		elif self.stats.stop:
			self.menu.game_over()
			self.reset()
		pg.display.flip()
		
	def run_game(self):
		while True:
			if self.stats.game_on:
				self.keyboard.get_event(self)
			self.update_screen()
			self.blit_next_frame()
			self.clock.tick(30)

if __name__ == '__main__':
	sw = spacewar()
	sw.run_game()