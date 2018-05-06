import arcade
import Menu
import Settings
import Scene
import Player
import CollectableObject
import InteractiveObject
import Notebook
import Inventory

class Game(arcade.Window):

    def __init__(self):
        super().__init__(800, 600, "Ache o Culpado")
        self.menuWin = None
        self.scenes = None
        self.player = None
        self.collectableList = None
        self.colisionsList = None
        self.physicsEngine = None
        self.keys = None

    def setup(self):
        print("Setup")
        self.menuWin = Menu.Window()
        self.keys = {
                "up":False,
                "right":False,
                "down":False,
                "left":False,
                "interaction":False
                }
        self.keymap = Settings.load_settings()

    def on_draw(self):
        arcade.start_render()
        self.menuWin.draw()
        '''
        self.scene.draw()
        self.player.draw()
        self.walls.draw(self.player)
        self.collectables.draw(self.player)
        self.notebook.draw()
        self.inventory.draw()

        self.t2.interact(sairFatequia)
        '''

    def update(self, dt):
        '''
        self.t1.interact()
        self.setWin.update(self.keys)
        if not (self.notebook.active or self.inventory.active):
            self.player.update(self.keys)
        for c in self.collectables:
            if(c.isInteracting(self.player) and self.keys["interaction"]):
                self.inventory.append(c)
                self.collectables.remove(c)

        self.physicsEngine.update()
        '''
    def on_key_press(self, key, mod):
        print(key)
        if key == self.keymap["interaction"]:
            print("Interraco puto")
        '''
        if key == arcade.key.UP or key == arcade.key.W:
            self.keys["up"] = True
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.keys["right"] = True
        if key == arcade.key.DOWN or key == arcade.key.S:
            self.keys["down"] = True
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.keys["left"] = True
        if key == arcade.key.E:
            self.keys["interaction"] = True
        if key == arcade.key.N:
            self.menuWin.active = False
        if key == arcade.key.I:
            self.menuWin.active = True
        if key == arcade.key.ESCAPE:
            if(self.notebook.active):
                self.notebook.active = False
            if(self.inventory.active):
                self.inventory.active = False
        '''
    def on_key_release(self, key, mod):
        if key == arcade.key.UP or key == arcade.key.W:
            self.keys["up"] = False
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.keys["right"] = False
        if key == arcade.key.DOWN or key == arcade.key.S:
            self.keys["down"] = False
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.keys["left"] = False
        if key == arcade.key.E:
            self.keys["interaction"] = False
