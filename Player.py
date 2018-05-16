import arcade
import Notebook
import Inventory

PLAYER_SPEED = 10

def New():
    return Player()
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("wolala.png", 1)
        self.center_x = 100
        self.center_i = 100
        self.notebook = Notebook.New()
        self.inventory = Inventory.New()

    def draw(self):
        super().draw()
        self.notebook.draw()
        self.inventory.draw()

    def update(self,keys):
        if(keys["up"]):
            self.change_y = PLAYER_SPEED
        if(keys["down"]):
            self.change_y = -PLAYER_SPEED
        if(keys["left"]):
            self.change_x = -PLAYER_SPEED
        if(keys["right"]):
            self.change_x = PLAYER_SPEED

        if(not keys["up"] and not keys["down"]):
            self.change_y = 0
        if(not keys["left"] and not keys["right"]):
            self.change_x = 0
