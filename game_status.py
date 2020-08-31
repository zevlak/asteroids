# Class for game status

import pyglet

FONT_SIZE = 15
IMAGES_SHIP = [
    'images/playerShip1_blue.png',
    'images/playerShip2_blue.png',
    'images/playerShip3_blue.png'
]


def draw_text(text, x, y, font_size, bold=False):
    '''Draws text as label'''
    pyglet.text.Label(
        text,
        font_size=font_size,
        x=x, y=y,
        bold=bold
    ).draw()
    
def draw_text_batch(text, x, y, font_size, batch, bold=False):
    pyglet.text.Label(
        text,
        font_size=font_size,
        x=x, y=y,
        bold=bold,
        batch=batch
    ).draw()
   


class GameStatus:
    
    def __init__(self, batch, ship_img_idx, window_width, window_height):
        self.score = 0
        self.lifes = 3
        self.level = 1
        self.lasers_fired = 0
        self.asteroids_destroyed = 0
        self.batch = batch
        self.ship_img_idx = ship_img_idx
        self.window_width = window_width
        self.window_height = window_height
        self.sprites = []
    
    def draw_lifes(self):
        image = pyglet.image.load(IMAGES_SHIP[self.ship_img_idx])
        for i in range(0, self.lifes):
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

        if self.lifes < 1:
            self.game_over()
    
    def draw(self):
        draw_text('Level: ' + str(self.level), 10, self.window_height - FONT_SIZE - 10, FONT_SIZE)
        draw_text('Score: ' + str(self.score), 10, self.window_height - 2 * FONT_SIZE - 5 - 10, FONT_SIZE)
        
    def game_over(self):
        draw_text_batch('GAME OVER!', self.window_width // 2 - 190, self.window_height // 2, 40, self.batch, True)
        font_size = 25
        draw_text_batch(
            'Level: ' + str(self.level),
            self.window_width // 2 - 190,
            self.window_height // 2 - 60,
            font_size,
            self.batch,
            True
        )
        draw_text_batch(
            'Score: ' + str(self.score),
            self.window_width // 2 - 190,
            self.window_height // 2 - 100,
            font_size,
            self.batch,
            True
        )
        draw_text_batch(
            'Lasers fired: ' + str(self.lasers_fired),
            self.window_width // 2 - 190,
            self.window_height // 2 - 140,
            font_size,
            self.batch,
            True
        )
        draw_text_batch(
            'Asteroids destroyed: ' + str(self.asteroids_destroyed),
            self.window_width // 2 - 190,
            self.window_height // 2 - 180,
            font_size,
            self.batch,
            True
        )
        draw_text_batch(
            'Fire accuracy: {:.2f} %'.format(self.asteroids_destroyed / self.lasers_fired * 100),
            self.window_width // 2 - 190,
            self.window_height // 2 - 220,
            font_size,
            self.batch,
            True
        )

