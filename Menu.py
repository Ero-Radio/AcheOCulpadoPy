import arcade
import KeysState

def Window():
    return MenuWindow()

class MenuWindow:
    def __init__(self):
        self.menu = [
                ("Iniciar", 100, 200),
                ("Pontuação", 100, 300),
                ("Opções", 100, 400),
                ("Sair", 100, 500)
                    ]
        self.item = 0
        self.hasChanged = False
        self.active = True

    def draw(self):
        if not self.active:
            return

        for item in self.menu:
            arcade.draw_text(item[0], item[1], item[2], arcade.color.WHITE, 50)

        selected = self.menu[self.item]
        arcade.draw_text(selected[0], selected[1], selected[2], arcade.color.RED, 55)

    def update(self):
        if(KeysState.keys["right"] or KeysState.keys["up"]):
            if not self.hasChanged:
                self.item += 1
                self.hasChanged = True
        elif(KeysState.keys["left"] or KeysState.keys["down"]):
            if not self.hasChanged:
                self.item -= 1
                self.hasChanged = True
        else:
            self.hasChanged = False


        if self.item > len(self.menu)-1:
            self.item = 0

        if self.item < 0:
            self.item = len(self.menu)-1
