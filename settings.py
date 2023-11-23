class settings:
	'''Stores important settings for the game'''

	def __init__(self):
		self.screen_width = 1200
		self.screen_length = 800
		self.bg_color = (30, 31, 51)
		self.caption = "Space War"

		#ships setting
		self.ship_speed = 10.5

		#bullet setting
		self.bullet_speed = 5
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color = (235, 116, 199)
		self.nb_bullets = 5
