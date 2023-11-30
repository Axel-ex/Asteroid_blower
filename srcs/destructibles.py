import random as rd 
import pygame as pg
from player import *

class Asteroid(Sprite):
	def __init__(self, spacewar):
		super().__init__()
		self.screen = spacewar.screen
		self.settings = spacewar.settings
		self.curr_sprite = 0
		self.frame_count = 0
		self.size = rd.randint(40, self.settings.size_max)
		self.speed = rd.randint(1, self.settings.asteroid_speed)

		self.sprites = []
		for sprite in self.settings.asteroid_sprites:
			self.sprites.append(pg.image.load(sprite))

		self.image = self.sprites[self.curr_sprite]
		self.rect = self.image.get_rect()
		self.rect.x = rd.uniform(0, self.settings.screen_width)
		self.rect.y = rd.uniform(-500, -100)
		self.rect.inflate_ip(self.settings.hitbox_expension, self.settings.hitbox_expension)

		#Store the initial position to determine how asteroid will move
		self.x_initial = self.rect.x
		self.y_initial = self.rect.y

	def is_out_bounds(self):
		screen_rect = self.screen.get_rect()
		return (self.rect.y >= screen_rect.bottom + self.settings.boundary_pad
		  or self.rect.x >= screen_rect.right + self.settings.boundary_pad
		  or self.rect.x < screen_rect.left - self.settings.boundary_pad)

	def resize_image(self):
		old_center = self.rect.center
		self.image = pg.transform.scale(self.sprites[self.curr_sprite], (self.size, self.size))
		self.rect = self.image.get_rect()
		self.rect.center = old_center

	def animate(self):
		self.frame_count += 1
		if self.frame_count % self.settings.animation_speed == 0:
			self.curr_sprite += 1
		if self.curr_sprite == len(self.sprites):
			self.curr_sprite = 0
		self.resize_image()

	def update(self):
		#give a direction to the atseroid depending on where it is on screen
		#if it goes out of the screen, it appears on the other side
		if self.x_initial >= self.settings.screen_width / 2:
			self.rect.x -= 1
			if self.is_out_bounds():
				self.rect.x = self.settings.screen_width + self.settings.boundary_pad - 1

		if self.x_initial < self.settings.screen_width / 2:
			self.rect.x += 1
			if self.is_out_bounds():
				self.rect.x = - self.settings.boundary_pad + 1

		self.rect.y += self.speed
		if self.is_out_bounds():
			self.rect.y = -15
		self.animate()
	
	def blit(self):
		self.screen.blit(self.image, self.rect)



class Explosion(Sprite):
	def __init__(self, spacewar, position, sprites):
		super().__init__()
		self.screen = spacewar.screen
		self.settings = spacewar.settings
		self.size = self.settings.explosion_size
		self.curr_sprite = 0
		self.frame_count = 0
		
		self.sprites = []
		for sprite in sprites:
			self.sprites.append(pg.image.load(sprite))

		self.image = self.sprites[self.curr_sprite]
		self.image = pg.transform.scale(self.image, (self.size, self.size))
		self.rect = self.image.get_rect()
		self.rect.center = position

	def resize_image(self):
		old_center = self.rect.center
		self.image = pg.transform.scale(self.sprites[self.curr_sprite], (self.size, self.size))
		self.rect = self.image.get_rect()
		self.rect.center = old_center

	def animate(self):
		self.frame_count += 1
		if self.frame_count % self.settings.animation_speed == 0:
			self.curr_sprite += 1
			if self.curr_sprite == len(self.sprites):
				self.kill()
			else:
				self.resize_image()
		
	def blit(self):
		self.animate()
		self.screen.blit(self.image, self.rect)


