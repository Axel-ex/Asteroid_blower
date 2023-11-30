class settings:
	'''Stores important settings for the game'''

	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (30, 31, 51)
		self.score_color = (234, 203, 71)
		self.caption = "Asteroid blower"
		self.prompt = "ASTEROID BLOWER"

		#ships setting
		self.nb_ships = 3
		self.lifelost_delay = 3
		self.ship_speed = 10.5
		self.ship_sprite = "../assets/spaceship.bmp"

		#bullet setting
		self.bullet_radius = 6
		self.bullet_speed = 10
		self.bullet_color = (235, 116, 199)
		self.nb_bullets = 5

		#Thruster
		self.thruster_sprites = [
			"../assets/thruster/thruster0.bmp",
			"../assets/thruster/thruster1.bmp",
			"../assets/thruster/thruster2.bmp",
			"../assets/thruster/thruster3.bmp",
			"../assets/thruster/thruster4.bmp",
		]

		#Asteroid settings
		self.nb_asteroids = 5
		self.animation_speed = 2
		self.asteroid_speed = 4
		self.hitbox_expension = 20
		self.size_max = 80
		self.boundary_pad = 20
		self.asteroid_sprites = [
			"../assets/asteroids/asteroid0.bmp",
			"../assets/asteroids/asteroid1.bmp",
			"../assets/asteroids/asteroid2.bmp",
			"../assets/asteroids/asteroid3.bmp",
			"../assets/asteroids/asteroid4.bmp",
			"../assets/asteroids/asteroid5.bmp",
			"../assets/asteroids/asteroid6.bmp",
			"../assets/asteroids/asteroid7.bmp",
			"../assets/asteroids/asteroid8.bmp",
			"../assets/asteroids/asteroid9.bmp",
			"../assets/asteroids/asteroid10.bmp",
			"../assets/asteroids/asteroid11.bmp",
			"../assets/asteroids/asteroid12.bmp",
			"../assets/asteroids/asteroid13.bmp",
			"../assets/asteroids/asteroid14.bmp",
			"../assets/asteroids/asteroid15.bmp",
			"../assets/asteroids/asteroid16.bmp",
			"../assets/asteroids/asteroid17.bmp",
		]

		#explosion settings
		self.explosion_size = 250
		self.explosion_sprites = [
            "../assets/explosion/explosion1/1.bmp",
            "../assets/explosion/explosion1/2.bmp",
            "../assets/explosion/explosion1/3.bmp",
            "../assets/explosion/explosion1/4.bmp",
            "../assets/explosion/explosion1/5.bmp",
            "../assets/explosion/explosion1/6.bmp",
            "../assets/explosion/explosion1/7.bmp",
            "../assets/explosion/explosion1/8.bmp",
            "../assets/explosion/explosion1/9.bmp",
            "../assets/explosion/explosion1/10.bmp",
            "../assets/explosion/explosion1/11.bmp",
            "../assets/explosion/explosion1/12.bmp",
            "../assets/explosion/explosion1/13.bmp",
            "../assets/explosion/explosion1/14.bmp",
            "../assets/explosion/explosion1/15.bmp",
            "../assets/explosion/explosion1/16.bmp",
            "../assets/explosion/explosion1/17.bmp",
            "../assets/explosion/explosion1/18.bmp",
            "../assets/explosion/explosion1/19.bmp",
            "../assets/explosion/explosion1/20.bmp",
            "../assets/explosion/explosion1/21.bmp",
            "../assets/explosion/explosion1/22.bmp",
            "../assets/explosion/explosion1/23.bmp",
            "../assets/explosion/explosion1/24.bmp",
            "../assets/explosion/explosion1/25.bmp",
            "../assets/explosion/explosion1/26.bmp",
            "../assets/explosion/explosion1/27.bmp",
            "../assets/explosion/explosion1/28.bmp",
            "../assets/explosion/explosion1/29.bmp",
            "../assets/explosion/explosion1/30.bmp",
            "../assets/explosion/explosion1/31.bmp",
            "../assets/explosion/explosion1/32.bmp",
            "../assets/explosion/explosion1/33.bmp",
            "../assets/explosion/explosion1/34.bmp",
            "../assets/explosion/explosion1/35.bmp",
            "../assets/explosion/explosion1/36.bmp",
            "../assets/explosion/explosion1/37.bmp",
            "../assets/explosion/explosion1/38.bmp",
            "../assets/explosion/explosion1/39.bmp",
            "../assets/explosion/explosion1/40.bmp",
            "../assets/explosion/explosion1/41.bmp",
            "../assets/explosion/explosion1/42.bmp",
            "../assets/explosion/explosion1/43.bmp",
            "../assets/explosion/explosion1/44.bmp",
            "../assets/explosion/explosion1/45.bmp",
            "../assets/explosion/explosion1/46.bmp",
            "../assets/explosion/explosion1/47.bmp",
            "../assets/explosion/explosion1/48.bmp",
            "../assets/explosion/explosion1/49.bmp",
            "../assets/explosion/explosion1/50.bmp",
            "../assets/explosion/explosion1/51.bmp",
            "../assets/explosion/explosion1/52.bmp",
            "../assets/explosion/explosion1/53.bmp",
            "../assets/explosion/explosion1/54.bmp",
            "../assets/explosion/explosion1/55.bmp",
			"../assets/explosion/explosion1/56.bmp",
			"../assets/explosion/explosion1/57.bmp",
			"../assets/explosion/explosion1/58.bmp",
			"../assets/explosion/explosion1/59.bmp",
			"../assets/explosion/explosion1/60.bmp",
			"../assets/explosion/explosion1/61.bmp",
			"../assets/explosion/explosion1/62.bmp",
			"../assets/explosion/explosion1/63.bmp",
		]
		#Ship's explosion
		self.explosion_ship = [
		    "../assets/explosion/explosion2/1.bmp",
            "../assets/explosion/explosion2/2.bmp",
            "../assets/explosion/explosion2/3.bmp",
            "../assets/explosion/explosion2/4.bmp",
            "../assets/explosion/explosion2/5.bmp",
            "../assets/explosion/explosion2/6.bmp",
            "../assets/explosion/explosion2/7.bmp",
            "../assets/explosion/explosion2/8.bmp",
            "../assets/explosion/explosion2/9.bmp",
            "../assets/explosion/explosion2/10.bmp",
            "../assets/explosion/explosion2/11.bmp",
            "../assets/explosion/explosion2/12.bmp",
            "../assets/explosion/explosion2/13.bmp",
            "../assets/explosion/explosion2/14.bmp",
            "../assets/explosion/explosion2/15.bmp",
            "../assets/explosion/explosion2/16.bmp",
            "../assets/explosion/explosion2/17.bmp",
            "../assets/explosion/explosion2/18.bmp",
            "../assets/explosion/explosion2/19.bmp",
            "../assets/explosion/explosion2/20.bmp",
            "../assets/explosion/explosion2/21.bmp",
            "../assets/explosion/explosion2/22.bmp",
            "../assets/explosion/explosion2/23.bmp",
            "../assets/explosion/explosion2/24.bmp",
            "../assets/explosion/explosion2/25.bmp",
            "../assets/explosion/explosion2/26.bmp",
            "../assets/explosion/explosion2/27.bmp",
            "../assets/explosion/explosion2/28.bmp",
            "../assets/explosion/explosion2/29.bmp",
            "../assets/explosion/explosion2/30.bmp",
            "../assets/explosion/explosion2/31.bmp",
            "../assets/explosion/explosion2/32.bmp",
            "../assets/explosion/explosion2/33.bmp",
            "../assets/explosion/explosion2/34.bmp",
            "../assets/explosion/explosion2/35.bmp",
            "../assets/explosion/explosion2/36.bmp",
            "../assets/explosion/explosion2/37.bmp",
            "../assets/explosion/explosion2/38.bmp",
            "../assets/explosion/explosion2/39.bmp",
            "../assets/explosion/explosion2/40.bmp",
            "../assets/explosion/explosion2/41.bmp",
            "../assets/explosion/explosion2/42.bmp",
            "../assets/explosion/explosion2/43.bmp",
            "../assets/explosion/explosion2/44.bmp",
            "../assets/explosion/explosion2/45.bmp",
            "../assets/explosion/explosion2/46.bmp",
            "../assets/explosion/explosion2/47.bmp",
            "../assets/explosion/explosion2/48.bmp",
            "../assets/explosion/explosion2/49.bmp",
            "../assets/explosion/explosion2/50.bmp",
            "../assets/explosion/explosion2/51.bmp",
            "../assets/explosion/explosion2/52.bmp",
            "../assets/explosion/explosion2/53.bmp",
            "../assets/explosion/explosion2/54.bmp",
            "../assets/explosion/explosion2/55.bmp",
			"../assets/explosion/explosion2/56.bmp",
			"../assets/explosion/explosion2/57.bmp",
			"../assets/explosion/explosion2/58.bmp",
			"../assets/explosion/explosion2/59.bmp",
			"../assets/explosion/explosion2/60.bmp",
			"../assets/explosion/explosion2/61.bmp",
			"../assets/explosion/explosion2/62.bmp",
			"../assets/explosion/explosion2/63.bmp",	
		]