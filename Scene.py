import arcade
import CollectableObject
import KeysState
import Npc

scenesBackgrounds = ["img/backgrounds/CETAF.png",
                     "img/backgrounds/Estacao.png",
                     "img/backgrounds/Parque.png",
                     "img/backgrounds/Shopping.png",
                        ]

def new(sceneNo):
    return Scene(sceneNo)

class Scene:

    def __init__(self, sceneNo):
        self.bg = arcade.load_texture(scenesBackgrounds[sceneNo])
        self.collectableList = CollectableObject.newList()
        self.npcList = Npc.newNPCList()
        self.colisionsList = []
        self.loadSceneObjects(sceneNo)

    def draw(self, player):
        arcade.draw_texture_rectangle(self.bg.width/2, self.bg.height/2, self.bg.width, self.bg.height, self.bg, 0)
        self.collectableList.draw(player)
        self.npcList.draw(player)

    def update(self, player):

        '''
        '' Para cara item verifique se está em intereação
        '''
        for co in self.collectableList:
            if(co.isInteracting(player) and KeysState.keys["interaction"]):
                player.inventory.append(co)
                self.collectableList.remove(co)



    def loadSceneObjects(self, sceneNo):

        if(sceneNo == 0):
            for x in range(1,10):
                self.collectableList.append(CollectableObject.newObject())
                self.npcList.append(Npc.newNPC())

        pass