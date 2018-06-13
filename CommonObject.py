import arcade
from random import randint

class CommonObject:

    def __init__(self):
        self.center_x = randint(0, 800)
        self.center_y = randint(0, 600)
        self.texture = arcade.load_texture("wolala.png")

    def draw(self):
        arcade.draw_texture_rectangle(self.center_x, self.center_y, self.texture.width, self.texture.height, self.texture, 0)
