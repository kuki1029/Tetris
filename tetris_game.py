import pyglet


class tetris:

    def __init__(self, window_width, window_length):
        self.screen_width = window_width
        self.screen_length = window_length

    def draw_background(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', [225, 525,
                                      225, 75,
                                      475, 75,
                                      475, 525]))