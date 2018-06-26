import arcade
import Menu
import Settings
import Scene
import Player
import KeysState
import sys
import hud
import time

class Game(arcade.Window):

    def __init__(self):
        super().__init__(1280, 720, "Ache o Culpado")
        self.menuWin = None
        self.scenes = None
        self.player = None
        self.activeScene = None
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
            self.scenes[self.activeScene].draw(self.player)
            self.player.draw()
            hud.clock()


    def update(self, dt):
        if(self.menuWin):
            self.menuWin.update()

        if(self.scenes):
            self.player.update()
            self.scenes[self.activeScene].update(self.player)



    def on_key_press(self, key, mod):
        '''
        '' Directional keys
        '''
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


        '''
        '' Switch Between scenes
        '''
        if key == arcade.key.KEY_1:
            self.activeScene = 0
        if key == arcade.key.KEY_2:
            self.activeScene = 1
            if self.scenes[1] is None:
                self.scenes[1] = Scene.new(1)
        if key == arcade.key.KEY_3:
            self.activeScene = 2
            if self.scenes[2] is None:
                self.scenes[2] = Scene.new(2)
        if key == arcade.key.KEY_4:
            self.activeScene = 3
            if self.scenes[3] is None:
                self.scenes[3] = Scene.new(3)

        '''
        '' On menu if enter load the game
        '''
        if key == arcade.key.ENTER:
            if(self.menuWin):
                if(self.menuWin.item == 0):
                    self.player = Player.new()
                    self.scenes = []
                    hud.startTime = time.time()
                    self.scenes.append(Scene.new(0))
                    self.scenes.append(None)
                    self.scenes.append(None)
                    self.scenes.append(None)
                    self.activeScene = 0
                    self.menuWin = None

                elif(self.menuWin.item == 3):
                    sys.exit(0)




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
