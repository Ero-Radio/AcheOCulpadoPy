import arcade
import Settings
import Scene
import Player

class Game(arcade.Window):

    def __init__(self):
        super().__init__(800, 600, "Ache o Culpado")
        self.setWin = Settings.SettingsWindow()
        self.scene = Scene.Scene()
        self.player = Player.Player()
        self.keys = {
                "up":False,
                "right":False,
                "down":False,
                "left":False
                }

    def on_draw(self):
        arcade.start_render()
        #self.setWin.draw()
        self.scene.draw()
        self.player.draw()
    def update(self, dt):
        self.setWin.update(self.keys)
        self.player.update(self.keys)

    def on_key_press(self, key, mod):
        if key == arcade.key.UP or key == arcade.key.W:
            self.keys["up"] = True
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.keys["right"] = True
        if key == arcade.key.DOWN or key == arcade.key.S:
            self.keys["down"] = True
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.keys["left"] = True

    def on_key_release(self, key, mod):
        if key == arcade.key.UP or key == arcade.key.W:
            self.keys["up"] = False
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.keys["right"] = False
        if key == arcade.key.DOWN or key == arcade.key.S:
            self.keys["down"] = False
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.keys["left"] = False
