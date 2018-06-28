import arcade
import Menu
import Settings
import Scene
import Player
import KeysState
import sys
import hud
import time
import WorldMap

class Game(arcade.Window):

    def __init__(self):
        super().__init__(1280, 720, "Ache o Culpado")
        self.menuWin = None
        self.scenes = None
        self.player = None
        self.activeScene = None
        self.physicsEngine = None
        self.mx=0
        self.my=0

    def setup(self):
        print("Setup")
        self.menuWin = Menu.Window()
        KeysState.keymap = Settings.load_settings()
        self.wm = WorldMap.New(1280, 720)

    def on_draw(self):
        arcade.start_render()

        if(self.menuWin):
            self.menuWin.draw()

        if(self.scenes):
            self.scenes[self.activeScene].draw(self.player)
            self.player.draw()
            hud.clock()
            # hud.dialogBox("{},{}".format(self.mx, self.my), False)

            if(self.wm.active):
                self.wm.draw()




    def update(self, dt):
        if(self.menuWin):
            self.menuWin.update()

        if(self.scenes):

            if(not self.wm.active):
                self.player.update()
            aScene  = self.scenes[self.activeScene]
            aScene.update(self.player)
            if(aScene.policeCar.isInteracting(self.player) and KeysState.keys["interaction"]):
                self.wm.active = True

            if(self.wm.active):
                self.wm.update()
                if(KeysState.keys["interaction"]):
                    self.activeScene = self.wm.item
                    if self.scenes[self.activeScene] is None:
                        self.scenes[self.activeScene] = Scene.new(self.activeScene)
                        self.wm.active = False

        KeysState.keys["interaction"] = False
        KeysState.keys["notebook"] = False
        KeysState.keys["inventory"] = False
        KeysState.keys["acuse"] = False
        KeysState.keys["esc"] = False


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """ Override this function to add mouse button functionality. """
        self.mx = x
        self.my = y



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

        if key == arcade.key.R:
            KeysState.keys["acuse"] = True

        if key == arcade.key.I:
            KeysState.keys["inventory"] = True

        if key == arcade.key.N:
            KeysState.keys["notebook"] = True

        if key == arcade.key.ESCAPE:
            KeysState.keys["esc"] = True
            self.wm.active = False

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
