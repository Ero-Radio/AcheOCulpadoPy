import arcade
import CollectableObject
import InteractiveObject
import KeysState
import Npc
import json
import hud

scenesBackgrounds = ["img/backgrounds/CETAF.png",
                     "img/backgrounds/Estacao.png",
                     "img/backgrounds/Parque.png",
                     "img/backgrounds/Shopping.png",
                        ]

policeCarPosition = (
                     (79, 402),
                     (654, 31),
                     (12, 143),
                     (1096, 425)
                     )

def new(sceneNo):
    return Scene(sceneNo)

class Scene:

    def __init__(self, sceneNo):
        self.bg = arcade.load_texture(scenesBackgrounds[sceneNo])
        self.collectableList = CollectableObject.newList()
        self.npcList = Npc.newNPCList()
        self.colisionsList = []
        self.policeCar = InteractiveObject.InteractiveObject()
        self.policeCar.center_x = policeCarPosition[sceneNo][0]
        self.policeCar.center_y = policeCarPosition[sceneNo][1]
        self.loadSceneObjects(sceneNo)
        self.showLine = False
        self.lastLine = None

    def draw(self, player):
        arcade.draw_texture_rectangle(self.bg.width/2, self.bg.height/2, self.bg.width, self.bg.height, self.bg, 0)
        self.collectableList.draw(player)
        self.npcList.draw(player)
        self.policeCar.draw(player)
        if(self.showLine):
            hud.dialogBox(self.lastLine, True)

    def update(self, player):

        '''
        '' Para cada item verifique se está em interação
        '''

        for co in self.collectableList:
            if(co.isInteracting(player) and KeysState.keys["interaction"]):
                player.inventory.append(co)
                self.collectableList.remove(co)

        for npc in self.npcList:
            if(npc.isInteracting(player) and KeysState.keys["interaction"]):
                player.notebook[npc.name] = npc.lines[0]
                self.lastLine = npc.lines[0]
                self.showLine = not self.showLine
            if(npc.isInteracting(player) and KeysState.keys["acuse"]):
                self.lastLine = npc.lines[2]
                self.showLine = not self.showLine



    def loadSceneObjects(self, sceneNo):
        with open('json/scenes.json', 'r', encoding="utf-8") as file:
            scenes = json.load(file)

        _npcs = scenes[sceneNo]["npcs"]
        _objs = scenes[sceneNo]["objects"]
        for npc in _npcs:
            nome = npc["nome"]
            lines = npc["lines"]
            spritePath = npc["sprite_small"]
            newNPC = Npc.newNPC(nome, lines, spritePath)
            if "pos" in npc:
                newNPC.center_x = npc["pos"][0]
                newNPC.center_y = npc["pos"][1]
            self.npcList.append(newNPC)


        for obj in _objs:
            newObj = CollectableObject.newObject(obj["desc"], obj["path"])
            newObj.center_x = obj["pos"][0]
            newObj.center_y = obj["pos"][1]
            self.collectableList.append(newObj)
