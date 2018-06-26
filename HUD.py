'''
	MODULO HUD
'''
import arcade
import time

'''
	Contantes da HUD
'''
textColor = (255, 255, 255)

<<<<<<< HEAD
dialogFillColor = (155, 155, 155)
dialogOutlineColor = (0, 0, 0)

'''
	Variaveis de inicialização
'''
sWidth = 500
sHeigh = 500
startTime = time.time()

def textAt(*, x, y, text):
	"""
	Texto Flutuante

	Insere um texto na posição específicada

	Parametros
	----------
	text: str
		Texto a ser inserido
	x: float
		posição x central do texto
	y: float
		posição y central do texto
	"""
	arcade.draw_text(text, x, y, textColor, 20, font_name=("Impact Regular"))


def dialogBox(text):
	"""
	Caixa de dialogo

	Desenha a caixa de diálogo, o comando para a próxima interação
	e o texo requerido

	Parametro
	---------
	text: str
		Texto a ser inserido na caixa de dialogo
	"""
	arcade.draw_rectangle_filled(sWidth/2, 50, sWidth, 100, dialogFillColor)
	arcade.draw_rectangle_outline(sWidth/2, 50, sWidth-10, 90, dialogOutlineColor, 2)
	arcade.draw_text(text, 20, 90, textColor, 16, font_name=("Impact Regular"), align="left", anchor_y="top")
	arcade.draw_text("e para continuar", sWidth-180, 15, textColor, 16, font_name=("Impact Regular"), align="left")


def clock():
	"""
	Desenha o relógio em seu estado atual

	A partir da inicialização od modulo hud, desenha e atualiza tanto o
	rológio digital no canto superior direito da tela, como a barra
	de tempo restante
	"""
	elapsedTime = int(time.time() - startTime)
	secs = elapsedTime%60
	mins = int(elapsedTime/60)
	timeWidth = sWidth - sWidth/1800 * elapsedTime
	arcade.draw_lrtb_rectangle_filled(0, timeWidth, sHeigh, sHeigh-10, dialogFillColor)
	textAt(x=sWidth-80, y=sHeigh-30, text="{:02}:{:02}".format(mins, secs))
