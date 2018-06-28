import arcade
import Util
import InteractiveObject

def newObject(nome="nada", path="wolala.png"):
	return CollectableObject(nome, path)

def newList():
	return CollectableList();

class CollectableObject(InteractiveObject.InteractiveObject):

    def __init__(self, nome, path):
        super().__init__()
        self.name = "{}".format(nome)
        self.texture = arcade.load_texture(path)

    def draw(self, player):
        arcade.draw_texture_rectangle(self.center_x, self.center_y, self.texture.width, self.texture.height, self.texture, 0)
        if(self.isInteracting(player)):
            arcade.draw_text("!", self.center_x, self.center_y+50, arcade.color.PINK, 30)

class CollectableList(list):

    # def __init__(self):

#    def append(self, object):
#        self..append(object)

    def draw(self, player):
        for o in self:
            o.draw(player)
