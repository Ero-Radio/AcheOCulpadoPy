import arcade
import hud
import KeysState
import time
# import CollectableObject

def New(sW, sH):
    return WorldMap(sW, sH)

dialogFillColor = (155, 155, 155, 240)
dialogOutlineColor = (0, 0, 0)
selectedColor = (255, 0, 255, 100)

class WorldMap:

    def __init__(self, sW, sH):
        super().__init__()
        self.bg = arcade.load_texture( "img/backgrounds/Worldmap.png")
        self.active = False
        self.lastActivation = time.time()
        self.item = 0
        self.locations = [
          ("CETAF", 167, 388, 572, 450),
          ("Estação Cão Saetano", 684, 846, 255, 145),
          ("Parque", 492, 624, 571, 448),
          ("Shopping Cão Saetano", 949, 1097, 475, 351)
          ]
        self.sW = sW
        self.sH = sH

    def draw(self):
        if self.active:
            self.backdraw()
            self.drawLocations()
            hud.dialogBox(self.locations[self.item][0], False)

    def backdraw(self):
      arcade.draw_texture_rectangle(self.bg.width/2, self.bg.height/2, self.bg.width-100, self.bg.height-100, self.bg, 0)

    def drawLocations(self):
        for i, item in enumerate(self.locations):
            arcade.draw_lrtb_rectangle_outline(
              item[1],
              item[2],
              item[3],
              item[4],
              dialogOutlineColor if self.item != i else selectedColor,
              5
              )
            arcade.draw_lrtb_rectangle_filled(
              item[1],
              item[2],
              item[3],
              item[4],
              (255, 255, 255, 0) if self.item != i else selectedColor,
              )

    def update(self):
        if KeysState.keys["left"]:
          self.item -= 1
          self.lastActivation = time.time()

          if self.item < 0:
              self.item = len(self.locations)-1

        if KeysState.keys["right"]:
            self.item += 1
            self.lastActivation = time.time()

            if self.item > len(self.locations)-1:
                self.item = 0

        KeysState.keys["left"] = False
        KeysState.keys["right"] = False

