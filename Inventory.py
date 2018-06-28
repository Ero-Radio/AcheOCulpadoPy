import arcade
import hud
import KeysState
# import CollectableObject

def New(sW, sH):
    return Inventory(sW, sH)

dialogFillColor = (155, 155, 155, 240)
dialogOutlineColor = (0, 0, 0)
selectedColor = (255, 0, 255)

class Inventory(list):

    def __init__(self, sW, sH):
        super().__init__()
        self.active = False
        self.item = 0
        self.sW = sW
        self.sH = sH
        self.texture = arcade.load_texture("wolala.png")

    def draw(self):
        if self.active:
            self.backdraw()
            self.drawItems()
            if(len(self)>0):
                hud.textAt(text=self[self.item].name, x=100, y=200)

    def backdraw(self):
        arcade.draw_rectangle_filled(self.sW/2,
         self.sH/2,
         self.sW-50,
         self.sH-50,
         dialogFillColor)

        arcade.draw_rectangle_outline(self.sW/2,
         self.sH/2,
         self.sW-60,
         self.sH-60,
         dialogOutlineColor,
         2)

        arcade.draw_text("INVENTARIO",
                self.sW/2, self.sH-70, (255, 255, 255), 40,
                align="center", anchor_x="center",anchor_y="center")

    def drawItems(self):
        for i, item in enumerate(self):
            arcade.draw_rectangle_outline(
              100 + 120*(i%10),
              self.sH-150 - 120*int(i/10),
              100,
              100,
              dialogOutlineColor if self.item != i else selectedColor,
              3
              )

            arcade.draw_texture_rectangle(
              100 + 120*(i%10),
              self.sH-150 - 120*int(i/10),
              90,
              90,
              item.texture,
              0
              )

    def update(self):
        if KeysState.keys["left"]:
            self.item += 1

        if self.item > len(self)-1:
            self.item = 0