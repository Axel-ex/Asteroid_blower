import pygame as pg 
from pygame.sprite import Sprite
from settings import *
from destructibles import *

class Ship():
	def __init__(self, spacewar):
		self.screen = spacewar.screen
		self.screen_rect = spacewar.screen_rect
		self.stats = spacewar.stats

		self.settings = spacewar.settings	
		self.image = pg.image.load(self.settings.ship_sprite)
		self.image = pg.transform.scale(self.image, (50, 50))
		self.rect = self.image.get_rect()
		self.rect.midbottom = self.screen_rect.midbottom
		self.explosion_sprites = pg.sprite.Group()

		self.move_right = False
		self.move_left = False
		self.move_up = False
		self.move_down = False

	def animate_death(self):
		if not self.stats.is_dead:
			return
		if not self.explosion_sprites.sprites():
			explosion = Explosion(self, self.rect.center, self.settings.explosion_ship)
			self.explosion_sprites.add(explosion)
		for explo in self.explosion_sprites.sprites():
			explo.blit()
		if len(self.explosion_sprites.sprites()) == 0:
			self.stats.stop = True

	def check_death(self):
		if self.stats.nb_lifes == 0:
			self.stats.is_dead = True

	def collision_update(self):
		screen_rect = self.screen.get_rect()
		if self.rect.y < screen_rect.bottom and self.rect.y + 50 < screen_rect.bottom:
			self.rect.y += 50

	def update(self):
		self.check_death()
		if self.move_right and self.rect.right < self.screen_rect.right:
			self.rect.x += self.settings.ship_speed
		elif self.move_left and self.rect.left > self.screen_rect.left:
			self.rect.x -= self.settings.ship_speed
		elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.y += self.settings.ship_speed - 5
		elif self.move_up and self.rect.top > self.screen_rect.top:
			self.rect.y -= self.settings.ship_speed

	def blit(self):
		'''send ship to screen buffer'''
		self.screen.blit(self.image, self.rect)



class Thruster(Sprite):
	def __init__(self, spacewar):
		super().__init__()
		self.screen = spacewar.screen
		self.settings = spacewar.settings
		self.curr_sprite = 0

		self.sprites = []
		for sprite in self.settings.thruster_sprites:
			self.sprites.append(pg.image.load(sprite))

		self.image = self.sprites[self.curr_sprite]
		self.image = pg.transform.scale(self.image, (15, 15))
		self.rect = self.image.get_rect()
		self.rect.midtop= spacewar.ship.rect.midbottom
	
	def update(self, spacewar):
		self.rect.midtop= spacewar.ship.rect.midbottom
		self.curr_sprite += 1
		if self.curr_sprite == len(self.sprites):
			self.curr_sprite = 0
		self.image = self.sprites[self.curr_sprite]
		self.image = pg.transform.scale(self.image, (15, 15))

	def blit(self):
		self.screen.blit(self.image, self.rect)



class Bullet(Sprite):
	def __init__(self, spacewar):
		super().__init__()
		self.screen = spacewar.screen
		self.settings = spacewar.settings
		self.color = self.settings.bullet_color

		self.rect = pg.Rect(0, 0, self.settings.bullet_radius * 2, self.settings.bullet_radius * 2)
		self.rect.midbottom = spacewar.ship.rect.midtop
	
	def update(self):
		self.rect.y -= self.settings.bullet_speed
	
	def draw_bullet(self):
		pg.draw.circle(self.screen, self.color, self.rect.center, self.settings.bullet_radius)


	