import arcade
import time

startTime = 0
currentTime = 0

def new():
	return HUD()

class HUD:
	def __init__(self):
		self.currentTime = 0
		self.startTime = 0

	def draw(self):
		self.timeString = "{0:02}:{1:02}:{2:02}".format(int(self.currentTime/360),
		int(self.currentTime/60), self.currentTime%60)
		print(self.currentTime)
		arcade.draw_text(self.timeString, 400, 500, (255, 255, 255), 40, align="center",anchor_x="center", anchor_y="center")

	def update(self):
		self.currentTime += 1
		# currentTime = time.time()-startTime
