# Game Asteroids

import pyglet
from pyglet import gl
from game_state import GameState
from space import Space

WINDOW_WIDTH = 800  # pixels
WINDOW_HEIGHT = 600  # pixels
FONT_SIZE = 40

pressed_keys = set()

def draw():
    window.clear()
        
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
    
    # score
    draw_text(str(game_state.score), 20, WINDOW_HEIGHT - FONT_SIZE - 20)

def draw_text(text, x, y):
    '''Draws text as label'''
    pyglet.text.Label(
        text,
        font_size=FONT_SIZE,
        x=x, y=y
    ).draw()


def key_press(key, modificators):
    '''Processes key press'''
    pressed_keys.add(key)


def key_release(key, modificators):
    '''Processes key release'''
    pressed_keys.discard(key)


# batch for loading sprites
batch = pyglet.graphics.Batch()

# game state
game_state = GameState()

# space
space = Space(WINDOW_WIDTH, WINDOW_HEIGHT, batch, game_state)
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
