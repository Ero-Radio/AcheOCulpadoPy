import arcade

PLAYER_SPEED = 10
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("wolala.png", 1)
        self.center_x = 100
        self.center_i = 100

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
