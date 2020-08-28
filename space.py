# Space for asteroids game

import pyglet
from random import choice, randrange
from laser import Laser
from spaceship import Spaceship
from asteroid import Asteroid

IMAGES_SHIP = [
    'images/playerShip1_blue.png',
    'images/playerShip2_blue.png',
    'images/playerShip3_blue.png'
]
IMAGES_ASTEROID = []
IMAGES_ASTEROID.append(['images/meteorGrey_tiny1.png', 'images/meteorGrey_tiny2.png'])
IMAGES_ASTEROID.append(['images/meteorGrey_small1.png', 'images/meteorGrey_small2.png'])
IMAGES_ASTEROID.append(['images/meteorGrey_med1.png', 'images/meteorGrey_med2.png'])
IMAGES_ASTEROID.append([
    'images/meteorGrey_big1.png',
    'images/meteorGrey_big2.png',
    'images/meteorGrey_big3.png',
    'images/meteorGrey_big4.png'
])
IMAGES_LASER = ['images/laserGreen13.png']


class Space:

    def __init__(self, width, height, batch, game_status, ship_img_idx):
        self.width = width
        self.height = height
        self.ships = []
        self.asteroids = []
        self.lasers = []
        self.batch = batch
        self.game_status = game_status
        self.ship_img_idx = ship_img_idx
        # create first laser sprite and when fire is done then create new one
        self.laser_sprite = self.sprite(IMAGES_LASER)
    
    def create_objects(self):
        '''Create all objects in the space'''
        self.create_ship()
        self.create_asteroids()
            
    def create_ship(self):
        '''Create ship'''
        ship = Spaceship(self.width // 2, self.height // 2, self.sprite([IMAGES_SHIP[self.ship_img_idx]]), self.width, self.height)
        self.ships.append(ship)
        
    def create_asteroids(self):
        '''Create asteroids'''
        for i in range(0, len(IMAGES_ASTEROID)):
            x = 0
            y = 0
            if randrange(0, 2) == 0:
                x = randrange(0, self.width)
            else:
                y = randrange(0, self.height)
            
            size = len(IMAGES_ASTEROID) - i - 1
            for j in range(0, self.game_status.level - i):
                asteroid = Asteroid(x, y, size, self.sprite(IMAGES_ASTEROID[size]), self.width, self.height)
                self.asteroids.append(asteroid)

    def sprite(self, image_list):
        '''Loads image and return sprite'''
        image = pyglet.image.load(choice(image_list))
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        
        return pyglet.sprite.Sprite(image, batch=self.batch)
        
    def tick(self, dt, pressed_keys):
        '''process space objects'''
        self.process_ships(dt, pressed_keys)
        self.process_asteroids(dt)
        self.process_lasers(dt)
        
        
    def process_ships(self, dt, pressed_keys):
        for ship in self.ships:
            ship.tick(dt, pressed_keys)
            if pyglet.window.key.SPACE in pressed_keys:
                laser = ship.fire(self.laser_sprite)
                if laser is not None:
                    self.lasers.append(laser)
                    # create new laser sprite
                    self.laser_sprite = self.sprite(IMAGES_LASER)

    def process_asteroids(self, dt):
        for asteroid in self.asteroids:
            asteroid.tick(dt)
            # check collisions
            # ships check from asteroids, because ships are less
            for ship in self.ships:
                if ship.overlaps(asteroid, self.width, self.height):
                    self.ships.remove(ship)
                    ship.delete()
            
            # next lifes
            if not self.ships and self.game_status.lifes > 1:
                self.game_status.remove_life()
                self.create_ship()
                
    
    def process_lasers(self, dt):
        for laser in self.lasers:
            laser.tick(dt)
            if not laser.live():
                laser.delete()
                self.lasers.remove(laser)
            #  destroy asteroids
            for asteroid in self.asteroids:
                if laser.overlaps(asteroid, self.width, self.height):
                    self.lasers.remove(laser)
                    self.asteroids.remove(asteroid)

                    if asteroid.size > 0:
                        new_size = asteroid.size - 1
                        for i in range(0, 2):
                            new_asteroid = Asteroid(
                                asteroid.x,
                                asteroid.y,
                                new_size,
                                self.sprite(IMAGES_ASTEROID[new_size]),
                                self.width,
                                self.height
                            )
                            self.asteroids.append(new_asteroid)
                    
                    score = 100
                    if asteroid.size == 1:
                        score = 50
                    elif asteroid.size == 2:
                        score = 20
                    elif asteroid.size == 3:
                        score = 10
                    self.game_status.score += score
                    
                    laser.delete()
                    asteroid.delete()
                    
                    # it has to break because neither asteroid nor laser exists
                    break
            
            # Create new asteroids if there are no
            if not self.asteroids:
                self.game_status.level += 1
                self.create_asteroids()
    