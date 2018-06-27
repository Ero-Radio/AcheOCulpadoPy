import arcade
import Notebook
import Inventory
import KeysState

PLAYER_SPEED = 10

def new():
    return Player()

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("img/chars/small/prot_masc.png")
        self.center_x = 100
        self.center_y = 100
        self.notebook = Notebook.New()
        self.inventory = Inventory.New(1280, 720)

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


        if(KeysState.keys["inventory"]):
            self.inventory.active = True

        if(KeysState.keys["notebook"]):
            self.notebook.active = True


        if(KeysState.keys["esc"]):
            self.inventory.active = False
            self.notebook.active = False

        if(self.inventory.active):
            self.inventory.update()


