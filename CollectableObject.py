import arcade
import Util
import InteractiveObject

def newObject():
	return CollectableObject()

def newList():
	return CollectableList();

class CollectableObject(InteractiveObject.InteractiveObject):

    def __init__(self):
        super().__init__()
        self.interactionRadius = 100
        self.name = "Wololo {}".format(self)

class CollectableList(list):

#    def __init__(self):

#    def append(self, object):
#        self..append(object)

    def draw(self, player):
        for o in self:
            o.draw(player)
