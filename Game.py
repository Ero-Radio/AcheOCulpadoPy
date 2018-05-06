import arcade
import Settings
import Scene
import Player
import CollectableObject

class Game(arcade.Window):

    def __init__(self):
        super().__init__(800, 600, "Ache o Culpado")
        self.setWin = Settings.SettingsWindow()
        self.scene = Scene.Scene()
        self.player = Player.Player()
        self.inventory = []
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

    def on_draw(self):
        arcade.start_render()
        #self.setWin.draw()
        self.scene.draw()
        self.player.draw()
        self.walls.draw(self.player)
        self.collectables.draw(self.player)
        for i in range(len(self.inventory)):
            arcade.draw_text(self.inventory[i].name, 10, 100*i+1, arcade.color.GREEN, 20)

    def update(self, dt):
        self.setWin.update(self.keys)
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
