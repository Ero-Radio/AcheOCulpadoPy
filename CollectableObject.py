import arcade
import Util
import CommonObject

class CollectableObject(CommonObject.CommonObject):

    def __init__(self):
        super().__init__()
        self.interactionRadius = 100
        self.name = "Wololo {}".format(self)

    def draw(self, player):
        super().draw()
        if(self.isInteracting(player)):
            arcade.draw_text("Ai carai que interação delicia!!!", self.center_x, self.center_y+50, arcade.color.PINK, 30)

    def isInteracting(self, player):
        return Util.dist(player, self) < self.interactionRadius


class CollectableList(list):

#    def __init__(self):

#    def append(self, object):
#        self..append(object)

    def draw(self, player):
        for o in self:
            o.draw(player)
