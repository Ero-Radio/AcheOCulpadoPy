import arcade
import Menu
import Settings
import Scene
import Player
import KeysState

class Game(arcade.Window):

    def __init__(self):
        super().__init__(1280, 720, "Ache o Culpado")
        self.menuWin = None
        self.scenes = None
        self.player = None

        self.physicsEngine = None

    def setup(self):
        print("Setup")
        self.menuWin = Menu.Window()
        KeysState.keymap = Settings.load_settings()

    def on_draw(self):
        arcade.start_render()
        if(self.menuWin):
            self.menuWin.draw()

        if(self.scenes):
            self.scenes.draw(self.player)
            self.player.draw()


    def update(self, dt):
        if(self.menuWin):
            self.menuWin.update()

        if(self.scenes):
            self.player.update()
            self.scenes.update(self.player)



    def on_key_press(self, key, mod):
        if key == arcade.key.UP or key == arcade.key.W:
            KeysState.keys["up"] = True
        if key == arcade.key.RIGHT or key == arcade.key.D:
            KeysState.keys["right"] = True
        if key == arcade.key.DOWN or key == arcade.key.S:
            KeysState.keys["down"] = True
        if key == arcade.key.LEFT or key == arcade.key.A:
            KeysState.keys["left"] = True
        if key == arcade.key.E:
            KeysState.keys["interaction"] = True
        if key == arcade.key.I:
            KeysState.keys["inventory"] = True
        if key == arcade.key.N:
            KeysState.keys["notebook"] = True
        if key == arcade.key.ESCAPE:
            KeysState.keys["esc"] = True

        if key == arcade.key.ENTER:
            if(self.menuWin):
                if(self.menuWin.item == 0):
                    self.player = Player.new()
                    self.scenes = Scene.new(0)
                    self.menuWin = None



    def on_key_release(self, key, mod):
        if key == arcade.key.UP or key == arcade.key.W:
            KeysState.keys["up"] = False
        if key == arcade.key.RIGHT or key == arcade.key.D:
            KeysState.keys["right"] = False
        if key == arcade.key.DOWN or key == arcade.key.S:
            KeysState.keys["down"] = False
        if key == arcade.key.LEFT or key == arcade.key.A:
            KeysState.keys["left"] = False
        if key == arcade.key.E:
            KeysState.keys["interaction"] = False
        if key == arcade.key.I:
            KeysState.keys["inventory"] = False
        if key == arcade.key.N:
            KeysState.keys["notebook"] = False
        if key == arcade.key.ESCAPE:
            KeysState.keys["esc"] = False
