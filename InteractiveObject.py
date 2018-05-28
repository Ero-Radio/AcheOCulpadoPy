import arcade
import Util
import CommonObject

class InteractiveObject(CommonObject.CommonObject):

    def __init__(self):
        super().__init__()
        self.interactionText = "Wololo"
        self.state = False

    def draw(self, player):
        super().draw()
        if(self.isInteracting(player)):
            arcade.draw_text("Interação", self.center_x, self.center_y+50, arcade.color.PINK, 30)

    def isInteracting(self, player):
        return Util.dist(player, self) < self.interactionRadius

    def interact(self,function = None):
        if function == None:
            self.state = not self.state
            print(self.state)
        else:
            function()
