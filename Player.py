import arcade
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("wolala.png", 1)
        self.center_x = 100
        self.center_i = 100

    def update(self,keys):
        if(keys["up"]):
            self.center_y +=1
        if(keys["down"]):
            self.center_y -=1
        if(keys["left"]):
            self.center_x -=1
        if(keys["right"]):
            self.center_x +=1
