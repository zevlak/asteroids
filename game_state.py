# Class for game state

import pyglet

IMAGES_SHIP = [
    'images/playerShip1_blue.png',
    'images/playerShip2_blue.png',
    'images/playerShip3_blue.png'
]


class GameState:
    
    def __init__(self, batch, ship_img_idx):
        self.score = 0
        self.lifes = 3
        self.level = 1
        self.batch = batch
        self.ship_img_idx = ship_img_idx
        self.sprites = []
    
    def draw_lifes(self):
        image = pyglet.image.load(IMAGES_SHIP[self.ship_img_idx])
        for i in range(0, self.lifes):
            print(i)
            sprite = pyglet.sprite.Sprite(image, batch=self.batch)
            sprite.scale = 1/3
            sprite.opacity = 100
            sprite.x = 10 + i * (5 + sprite.width)
            sprite.y = 10
            self.sprites.append(sprite)

    def remove_life(self):
        self.lifes -= 1
        sprite = self.sprites.pop()
        sprite.delete()
        del(sprite)
