import arcade

def New(sW=1280, sH=720):
    return Notebook(sW, sH)

dialogFillColor = (155, 155, 155, 100)
dialogOutlineColor = (0, 0, 0)

class Notebook(dict):

    def __init__(self, sW, sH):
        super().__init__()
        self.active = False
        self.activeDetails = 2
        self.activeRegistry = 2
        self.activePage = 0
        self.sW = sW
        self.sH = sH

    def draw(self):
        if self.active:
            self.backdraw()
            self.drawTextLines()
            self.drawActiveRegistry()


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

        arcade.draw_line(self.sW/2,
         self.sH-130,
         self.sW/2,
         40,
         dialogOutlineColor,
         2)

        for i in range(1, int(self.sH/50)):
            arcade.draw_line(100, self.sH-130-50*i,
             self.sW-100,
             self.sH-130-50*i,
             dialogOutlineColor,
             2)

        arcade.draw_text("NOTEBOOK",
                self.sW/2, self.sH-70, (255, 255, 255), 40,
                align="center", anchor_x="center",anchor_y="center")

    def drawActiveRegistry(self):
        left = 100 if self.activeRegistry <11 else self.sW/2+2
        right = self.sW/2-2 if self.activeRegistry < 11 else self.sW-100
        top = self.sH-130-50*(self.activeRegistry%11)
        bottom = self.sH-130-48-50*(self.activeRegistry%11)

        arcade.draw_lrtb_rectangle_outline(left,
         right,
         top,
         bottom,
         arcade.color.RED,
         2)

    def drawTextLines(self):
        i = 0
        for k, v in self.items():
            xPos = 110 if i <11 else self.sW/2+12
            yPos= self.sH-130-50*(i%11)
            arcade.draw_text("{}:\n{}".format(k, v),
                xPos, yPos, (255, 255, 255), 14,
                align="left", anchor_x="left",anchor_y="top")
            i+=1