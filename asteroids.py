# Game Asteroids

import pyglet
from pyglet import gl
from game_status import GameStatus
from space import Space

WINDOW_WIDTH = 800  # pixels
WINDOW_HEIGHT = 600  # pixels
SHIP_IMAGE_INDEX = 0

pressed_keys = set()

def draw():
    window.clear()
        
    batch_status.draw()
    game_status.draw()
    
    # draw neightbour windows for fluent ship flight over end of window
    for x_offset in (-window.width, 0, window.width):
        for y_offset in (-window.height, 0, window.height):
            # Remember the current state
            gl.glPushMatrix()
            # Move everything drawn from now on by (x_offset, y_offset, 0)
            gl.glTranslatef(x_offset, y_offset, 0)

            # Draw
            batch.draw()

            # Restore remembered state (this cancels the glTranslatef)
            gl.glPopMatrix()
    

def key_press(key, modificators):
    '''Processes key press'''
    pressed_keys.add(key)


def key_release(key, modificators):
    '''Processes key release'''
    pressed_keys.discard(key)


# batch for graphics
batch = pyglet.graphics.Batch()
batch_status = pyglet.graphics.Batch()

# game state
game_status = GameStatus(batch_status, SHIP_IMAGE_INDEX, WINDOW_WIDTH, WINDOW_HEIGHT)
game_status.draw_lifes()
#game_status.draw()

# space
space = Space(WINDOW_WIDTH, WINDOW_HEIGHT, batch, game_status, SHIP_IMAGE_INDEX)
space.create_objects()

# window
window = pyglet.window.Window(space.width, space.height, caption='ASTEROIDS')
window.push_handlers(
    on_draw=draw,
    on_key_press=key_press,
    on_key_release=key_release
)

pyglet.clock.schedule(space.tick, pressed_keys)
pyglet.app.run()
