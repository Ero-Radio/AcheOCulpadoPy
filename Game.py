import arcade
import Menu
import Settings
import Scene
import Player
import CollectableObject
import InteractiveObject

class Game(arcade.Window):

    def __init__(self):
        super().__init__(800, 600, "Ache o Culpado")
        self.menuWin = None
        self.scenes = None
        self.player = None
        self.collectableList = []
        self.colisionsList = []
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
        self.player = Player.New()
        self.colisionsList = arcade.SpriteList()
        self.collectableList = CollectableObject.CollectableList()
        self.physicsEngine = arcade.PhysicsEngineSimple(self.player, self.colisionsList)

    def on_draw(self):
        arcade.start_render()
        #self.menuWin.draw()
        #self.scene.draw()
        self.colisionsList.draw(self.player)
        self.collectableList.draw(self.player)
        self.player.draw()

    def update(self, dt):
        #self.setWin.update(self.keys)
        if not (self.player.notebook.active or self.player.inventory.active):
            self.player.update(self.keys)
        for c in self.collectableList:
            if(c.isInteracting(self.player) and self.keys["interaction"]):
                self.player.inventory.append(c)
                self.collectableList.remove(c)

        self.physicsEngine.update()

    def on_key_press(self, key, mod):
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
