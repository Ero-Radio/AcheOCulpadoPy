import arcade
import CollectableObject

def new(sceneNo):
    return Scene(sceneNo)

class Scene:

    def __init__(self, sceneNo):
        self.bg = arcade.load_texture("wololo.png")
        self.collectableList = CollectableObject.newList()
        self.colisionsList = []
        self.loadSceneObjects(sceneNo)

    def draw(self, player):
        arcade.draw_texture_rectangle(self.bg.width/2, self.bg.height/2, self.bg.width, self.bg.height, self.bg, 0)
        self.collectableList.draw(player)

    def loadSceneObjects(self, sceneNo):

        if(sceneNo == 0):
            for x in range(1,10):
                self.collectableList.append(CollectableObject.newObject())

        pass