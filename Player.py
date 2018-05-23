import arcade
import Notebook
import Inventory
import KeysState

PLAYER_SPEED = 10

def new():
    return Player()

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("wolele.png", 2)
        self.center_x = 100
        self.center_y = 100
        self.notebook = Notebook.New()
        self.inventory = Inventory.New()

    def draw(self):
        super().draw()
        self.notebook.draw()
        self.inventory.draw()

    def update(self):
        super().update()
        if(KeysState.keys["up"]):
            self.change_y = PLAYER_SPEED
        if(KeysState.keys["down"]):
            self.change_y = -PLAYER_SPEED
        if(KeysState.keys["left"]):
            self.change_x = -PLAYER_SPEED
        if(KeysState.keys["right"]):
            self.change_x = PLAYER_SPEED

        if(not KeysState.keys["up"] and not KeysState.keys["down"]):
            self.change_y = 0
        if(not KeysState.keys["left"] and not KeysState.keys["right"]):
            self.change_x = 0
