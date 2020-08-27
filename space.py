# Space for asteroids game

import pyglet
from random import choice, randrange
from spaceship import Spaceship
from asteroid import Asteroid

IMAGES_SHIP = [
    'images/playerShip1_blue.png',
    'images/playerShip2_blue.png',
    'images/playerShip3_blue.png'
]
IMAGES_ASTEROID = [
    'images/meteorGrey_big1.png',
    'images/meteorGrey_big2.png',
    'images/meteorGrey_big3.png',
    'images/meteorGrey_big4.png',
    'images/meteorGrey_med1.png',
    'images/meteorGrey_med2.png',
    'images/meteorGrey_small1.png',
    'images/meteorGrey_small2.png',
    'images/meteorGrey_tiny1.png',
    'images/meteorGrey_tiny2.png',
]


class Space:

    def __init__(self, width, height, batch):
        self.width = width
        self.height = height
        self.ships = []
        self.asteroids = []
        self.batch = batch
    
    def create_objects(self):
        '''Create all objects in the space'''
        ship = Spaceship(self.width // 2, self.height // 2, self.sprite(IMAGES_SHIP), self.width, self.height)
        self.ships.append(ship)
        
        for i in range(0, 10):
            x = 0
            y = 0
            if randrange(0, 2) == 0:
                x = randrange(0, self.width)
            else:
                y = randrange(0, self.height)
            asteroid = Asteroid(x, y, self.sprite(IMAGES_ASTEROID), self.width, self.height)
            self.asteroids.append(asteroid)
            
    
    def sprite(self, image_list):
        '''Loads image and return sprite'''
        image = pyglet.image.load(choice(image_list))
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        
        return pyglet.sprite.Sprite(image, batch=self.batch)
        
    def tick(self, dt, pressed_keys):
        '''Moves space objects'''
        for ship in self.ships:
            ship.tick(dt, pressed_keys)
        for asteroid in self.asteroids:
            asteroid.tick(dt)
            # check collisions
            for ship in self.ships:
                if ship.overlaps(asteroid, self.width, self.height):
                    self.ships.remove(ship)
                    ship.delete()
            
                

