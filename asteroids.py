# Game Asteroids

import pyglet
from pyglet import gl
from spaceship import Spaceship

WINDOW_WIDTH = 800  # pixels
WINDOW_HEIGHT = 600  # pixels
PRESSED_KEYS = set()

def draw():
    window.clear()

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
    PRESSED_KEYS.add(key)


def key_release(key, modificators):
    '''Processes key release'''
    PRESSED_KEYS.discard(key)


# batch for loading sprites
batch = pyglet.graphics.Batch()

#objects
objects = []
ship = Spaceship(WINDOW_WIDTH, WINDOW_HEIGHT, batch)
objects.append(ship)

# window
window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, caption='ASTEROIDS')
window.push_handlers(
    on_draw=draw,
    on_key_press=key_press,
    on_key_release=key_release
)

pyglet.clock.schedule(ship.tick, PRESSED_KEYS)
pyglet.app.run()
