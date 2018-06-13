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

def newNPC():
	return NPC()

def newNPCList():
	return NPCList();

class NPC(InteractiveObject.InteractiveObject):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(temp[random.randint(0, 4)])
        self.interactionRadius = 100
        self.name = "Wolala {}".format(self)

class NPCList(list):

#    def __init__(self):

#    def append(self, object):
#        self..append(object)

    def draw(self, player):
        for npc in self:
            npc.draw(player)
