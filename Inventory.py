import arcade
import CollectableObject

def New():
    return Inventory()

class Inventory(CollectableObject.CollectableList):

    def __init__(self):
        super().__init__()
        self.active = False

    def draw(self):
        if self.active:
            arcade.draw_rectangle_filled(400, 300, 750, 550, (255, 0, 255))
            arcade.draw_text("O INVENTORY", 400, 500, (255, 255, 255), 40, align="center",
                                             anchor_x="center", anchor_y="center")
            for i in range(len(self)):
                arcade.draw_text(self[i].name, 400, 450-10*i,(255, 255, 255), 20, align="center",
                                             anchor_x="center", anchor_y="center")

