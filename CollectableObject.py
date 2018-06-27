import arcade
import Util
import InteractiveObject

def newObject(nome="nada"):
	return CollectableObject(nome)

def newList():
	return CollectableList();

class CollectableObject(InteractiveObject.InteractiveObject):

    def __init__(self, nome):
        super().__init__()
        self.name = "{}".format(nome)

class CollectableList(list):

    # def __init__(self):

#    def append(self, object):
#        self..append(object)

    def draw(self, player):
        for o in self:
            o.draw(player)
