import pyglet
from pyglet.window import key

class Window(pyglet.window.Window):
    def __init__(self):
        super(Window, self).__init__()
        #self.window = pyglet.window.Window()
        #self.window.on_draw = self.on_draw
        #self.window.on_key_press = self.on_key_press
        pyglet.app.run()

    def on_draw(self):
        self.clear()
        self.render()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.RETURN:
            self.close()
            print('closes')


    def render(self):
        print('render;')

