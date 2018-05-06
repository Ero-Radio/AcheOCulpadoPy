import arcade
class Scene:

    def __init__(self):
        self.bg = arcade.load_texture("wololo.png")

    def draw(self):
        arcade.draw_texture_rectangle(self.bg.width/2, self.bg.height/2, self.bg.width, self.bg.height, self.bg, 0)
