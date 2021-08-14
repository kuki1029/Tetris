import pyglet
from tetris_game import tetris

class Window(pyglet.window.Window):

    def __init__(self):
        super().__init__()
        self.set_size(700,600)
        self.tetris = tetris(700,600)

    def on_draw(self):
        self.clear()
        self.tetris.draw_background()


if __name__ == '__main__':
    window = Window()
    pyglet.app.run()