import pygame as pg 
from pygame.sprite import Sprite
from settings import *

class ship():
	'''Manage user's ship'''

	def __init__(self, spacewar):
		self.screen = spacewar.screen
		self.screen_rect = spacewar.screen.get_rect()

		self.settings = spacewar.settings	
		self.image = pg.image.load("assets/spaceship.bmp").convert_alpha()
		self.image = pg.transform.scale(self.image, (50, 50))
		self.rect = self.image.get_rect()
		self.rect.midbottom = self.screen_rect.midbottom

		self.move_right = False
		self.move_left = False
		self.move_up = False
		self.move_down = False

	def update(self):
		if self.move_right and self.rect.right < self.screen_rect.right:
			self.rect.x += self.settings.ship_speed
		elif self.move_left and self.rect.left > self.screen_rect.left:
			self.rect.x -= self.settings.ship_speed
		elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.y += self.settings.ship_speed
		elif self.move_up and self.rect.top > self.screen_rect.top:
			self.rect.y -= self.settings.ship_speed

	def blitme(self):
		'''send ship to screen buffer'''
		self.screen.blit(self.image, self.rect)



class Bullet(Sprite):
	'''Manage bullets of the ship'''

	def __init__(self, spacewar):
		'''bullet object spawning at ship position'''
		super().__init__()
		self.screen = spacewar.screen
		self.settings = spacewar.settings
		self.color = self.settings.bullet_color

		self.rect = pg.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = spacewar.ship.rect.midtop
	
	def update(self):
		self.rect.y -= self.settings.bullet_speed
	
	def draw_bullet(self):
		pg.draw.rect(self.screen, self.color, self.rect)

class thruster(Sprite):
	'''thruster animation'''

	def __init__(self, spacewar):
		super().__init__()
		self.screen = spacewar.screen
		self.settings = spacewar.settings
		self.sprites = []
		self.sprites.append(pg.image.load("assets/thruster/thruster0.bmp"))
		self.sprites.append(pg.image.load("assets/thruster/thruster1.bmp"))
		self.sprites.append(pg.image.load("assets/thruster/thruster2.bmp"))
		self.sprites.append(pg.image.load("assets/thruster/thruster3.bmp"))
		self.sprites.append(pg.image.load("assets/thruster/thruster4.bmp"))
		self.curr_sprite = 0
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

	def blit_thruster(self, spacewar):
		self.update(spacewar)
		self.screen.blit(self.image, self.rect)
	
		
