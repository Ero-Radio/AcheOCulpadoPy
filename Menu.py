import arcade
import KeysState

def Window():
    return MenuWindow()

class MenuWindow:
    def __init__(self):
        self.menu = [
                ("Iniciar", 100, 200),
                ("Pontuação", 200, 300),
                ("Opções", 300, 400),
                ("Sair", 400, 500)
                    ]
        self.item = 0
        self.hasChanged = False
        self.active = True
        self.bandeira = arcade.load_texture("img/assets/bandeira.jpg")

    def draw(self):
        if not self.active:
            return

        arcade.draw_texture_rectangle(1280/2,
            720/2,
            1280,
            720,
            self.bandeira,
            0)
        for item in self.menu:
            arcade.draw_text(item[0], item[1], item[2], arcade.color.GRAY, 50)

        selected = self.menu[self.item]
        arcade.draw_text(selected[0], selected[1], selected[2], arcade.color.RED, 50)

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
