import json
import arcade
def load_settings():
    settings = open("settings.json", "r", encoding="utf8")
    settings = json.loads(settings.read())
    sKeyMap = settings["keymap"]
    return settings["keymap_options"][sKeyMap]


def save_settings():
    ...

class SettingsWindow:
    def __init__(self):
        self.menu = [
                ("Iniciar", 100, 200),
                ("Pontuação", 200, 300),
                ("Opções", 300, 400),
                ("Sair", 400, 500)
                    ]
        self.item = 0
        self.hasChanged = False

    def draw(self):
        for item in self.menu:
            arcade.draw_text(item[0], item[1], item[2], arcade.color.WHITE, 50)

        selected = self.menu[self.item]
        arcade.draw_text(selected[0], selected[1], selected[2], arcade.color.RED, 55)

    def update(self, keys):
        if(keys["right"] or keys["up"]):
            if not self.hasChanged:
                self.item += 1
                self.hasChanged = True
        elif(keys["left"] or keys["down"]):
            if not self.hasChanged:
                self.item -= 1
                self.hasChanged = True
        else:
            self.hasChanged = False


        if self.item > len(self.menu)-1:
            self.item = 0

        if self.item < 0:
            self.item = len(self.menu)-1
