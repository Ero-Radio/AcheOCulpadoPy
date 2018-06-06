import arcade
from random import randint

temp =  ["img/chars/zenic.png",
		"img/chars/vronic.png",
		"img/chars/shirley.png",
		"img/chars/pictor.png",
		"img/chars/mumilo.png",
		]

class CommonObject:

    def __init__(self):
        self.center_x = randint(0, 800)
        self.center_y = randint(0, 600)
        self.texture = arcade.load_texture(temp[randint(0, 4)])

    def draw(self):
        arcade.draw_texture_rectangle(self.center_x, self.center_y, self.texture.width*0.07, self.texture.height*0.07, self.texture, 0)
