import arcade
import Util
import InteractiveObject
import random

temp =  ["img/chars/small/zenic.png",
		"img/chars/small/vronic.png",
		"img/chars/small/shirley.png",
		"img/chars/small/pictor.png",
		"img/chars/small/mumilo.png",
		]

def newNPC(name, lines, spritePath):
	return NPC(name, lines, spritePath)

def newNPCList():
	return NPCList();

class NPC(InteractiveObject.InteractiveObject):

    def __init__(self, name, lines, spritePath):
        super().__init__()
        self.texture = arcade.load_texture(spritePath)
        self.interactionRadius = 100
        self.name = name
        self.lines = lines

    def draw(self, player):
        super().draw(player)
        arcade.draw_texture_rectangle(self.center_x, self.center_y, self.texture.width, self.texture.height, self.texture, 0)

class NPCList(list):

#    def __init__(self):

#    def append(self, object):
#        self..append(object)

    def draw(self, player):
        for npc in self:
            npc.draw(player)

    def update(self):

        pass
