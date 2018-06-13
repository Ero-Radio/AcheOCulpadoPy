import arcade
import time

startTime = 0
currentTime = 0

def draw():
	timeString = "{0:02}:{1:02}:{2:02}".format(int(currentTime/360),
	 int(currentTime/60), currentTime%60)
	print(currentTime)
	arcade.draw_text(timeString, 400, 500, (255, 255, 255), 40, align="center",anchor_x="center", anchor_y="center")

def update():
	currentTime = time.time()-startTime
