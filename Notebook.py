import arcade

class Notebook(dict):

    def __init__(self):
        super().__init__()
        self.active = False

    def draw(self):
        if self.active:
            arcade.draw_rectangle_filled(400, 300, 750, 550, (255, 0, 255))
            arcade.draw_text("O NOTEBOOK SEU FUDIDO", 400, 500, (255, 255, 255), 40, align="center",
                                             anchor_x="center", anchor_y="center")
