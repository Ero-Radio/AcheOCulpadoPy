import arcade
import Settings
import Scene
import Player
import CollectableObject
import InteractiveObject
import Notebook
import Inventory

### funcoes de Interacao
def sairFatequia():
    arcade.draw_rectangle_filled(400, 300 ,800, 600, (200, 200, 200))

class Game(arcade.Window):

    def __init__(self):
        super().__init__(800, 600, "Ache o Culpado")
        self.setWin = Settings.SettingsWindow()
        self.scene = Scene.Scene()
        self.player = Player.Player()
        self.notebook = Notebook.Notebook()
        self.inventory = Inventory.Inventory()
        self.collectables = CollectableObject.CollectableList()
        self.collectables.append(CollectableObject.CollectableObject())
        self.collectables.append(CollectableObject.CollectableObject())
        self.collectables.append(CollectableObject.CollectableObject())
        self.collectables.append(CollectableObject.CollectableObject())
        self.collectables.append(CollectableObject.CollectableObject())
        self.collectables.append(CollectableObject.CollectableObject())
        self.walls = arcade.SpriteList()
        self.walls.append(arcade.Sprite("wolala.png", 1, center_x=100, center_y=200))
        self.walls.append(arcade.Sprite("wolala.png", 1, center_x=400, center_y=200))
        self.walls.append(arcade.Sprite("wolala.png", 1, center_x=300, center_y=200))
        self.physicsEngine = arcade.PhysicsEngineSimple(self.player, self.walls)
        self.keys = {
                "up":False,
                "right":False,
                "down":False,
                "left":False,
                "interaction":False
                }
        self.t1 = InteractiveObject.InteractiveObject()
        self.t2 = InteractiveObject.InteractiveObject()

    def on_draw(self):
        arcade.start_render()
        #self.setWin.draw()
        self.scene.draw()
        self.player.draw()
        self.walls.draw(self.player)
        self.collectables.draw(self.player)
        self.notebook.draw()
        self.inventory.draw()

        self.t2.interact(sairFatequia)

    def update(self, dt):
        self.t1.interact()
        self.setWin.update(self.keys)
        if not (self.notebook.active or self.inventory.active):
            self.player.update(self.keys)
        for c in self.collectables:
            if(c.isInteracting(self.player) and self.keys["interaction"]):
                self.inventory.append(c)
                self.collectables.remove(c)

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
            self.notebook.active = True
        if key == arcade.key.I:
            self.inventory.active = True
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
