# Space for asteroids game

import pyglet
from random import choice, randrange
from laser import Laser
from effect import Effect
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
IMAGES_SMOKE = [
    'images/whitePuff00.png',
    'images/whitePuff01.png',
    'images/whitePuff02.png',
    'images/whitePuff03.png',
    'images/whitePuff04.png',
    'images/whitePuff05.png',
    'images/whitePuff06.png',
    'images/whitePuff07.png',
    'images/whitePuff08.png'
]
IMAGES_FIRE = [
    'images/explosion08.png',
    'images/explosion01.png',
    'images/explosion02.png',
    'images/explosion03.png',
    'images/explosion04.png',
    'images/explosion05.png',
    'images/explosion06.png',
    'images/explosion07.png',
    'images/explosion08.png'
]

class Space:

    def __init__(self, width, height, batch, batch_effects, game_status, ship_img_idx):
        self.width = width
        self.height = height
        self.ships = []
        self.asteroids = []
        self.lasers = []
        self.effects = []
        self.batch = batch
        self.batch_effects = batch_effects
        self.game_status = game_status
        self.ship_img_idx = ship_img_idx
    
    def create_objects(self):
        '''Create all objects in the space'''
        self.create_ship()
        self.create_asteroids()
            
    def create_ship(self):
        '''Create ship'''
        ship = Spaceship(self.width // 2, self.height // 2, self.sprite([IMAGES_SHIP[self.ship_img_idx]], self.batch), self.width, self.height)
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
                asteroid = Asteroid(x, y, size, self.sprite(IMAGES_ASTEROID[size], self.batch), self.width, self.height)
                self.asteroids.append(asteroid)

    def create_smoke(self, x, y, asteroid_size):
        '''Creates random count of smoke'''
        for i in range(0, randrange(3, 7)):
            effect = Effect(
                x + randrange(10, 30),
                y + randrange(10, 30),
                self.sprite(IMAGES_SMOKE, self.batch_effects),
                20 // (asteroid_size + 1),
                self.width,
                self.height
            )
            self.effects.append(effect)

    def create_fire(self, x, y):
        '''Creates random count of fire'''
        for i in range(0, randrange(3, 7)):
            effect = Effect(
                x + randrange(10, 30),
                y + randrange(10, 30),
                self.sprite(IMAGES_FIRE, self.batch_effects),
                4,
                self.width,
                self.height
            )
            self.effects.append(effect)

    def sprite(self, image_list, batch):
        '''Loads image and return sprite'''
        image = pyglet.image.load(choice(image_list))
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        
        return pyglet.sprite.Sprite(image, batch=batch)
        
    def tick(self, dt, pressed_keys):
        '''process space objects'''
        self.process_ships(dt, pressed_keys)
        self.process_asteroids(dt)
        self.process_lasers(dt)
        self.process_effect(dt)
        
        
    def process_ships(self, dt, pressed_keys):
        for ship in self.ships:
            ship.tick(dt, pressed_keys)
            if pyglet.window.key.SPACE in pressed_keys:
                laser = ship.fire(self.sprite(IMAGES_LASER, self.batch))
                if laser is not None:
                    self.lasers.append(laser)

    def process_asteroids(self, dt):
        for asteroid in self.asteroids:
            asteroid.tick(dt)
            # check collisions
            # ships check from asteroids, because ships are less
            for ship in self.ships:
                if ship.overlaps(asteroid, self.width, self.height):
                    self.ships.remove(ship)
                    ship.delete()
                    self.create_fire(ship.x, ship.y)
            
            # next lifes
            if not self.ships:
                if self.game_status.lifes > 1:
                    self.game_status.remove_life()
                    self.create_ship()
                elif self.game_status.lifes == 1:
                    self.game_status.remove_life()
                    pyglet.clock.unschedule(self.tick)
            
                
    
    def process_lasers(self, dt):
        for laser in self.lasers:
            laser.tick(dt)
            
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
                                self.sprite(IMAGES_ASTEROID[new_size], self.batch),
                                self.width,
                                self.height
                            )
                            self.asteroids.append(new_asteroid)
                    
                    self.create_smoke(asteroid.x, asteroid.y, asteroid.size)
                    
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
            
            # destroy dead laser
            if not laser.live():
                laser.delete()
                self.lasers.remove(laser)

            # Create new asteroids if there are no
            if not self.asteroids:
                self.game_status.level += 1
                self.create_asteroids()

 
    def process_effect(self, dt):
        for effect in self.effects:
            effect.tick(dt)
            
            if effect.life_time < 0:
                self.effects.remove(effect)
                effect.delete()
