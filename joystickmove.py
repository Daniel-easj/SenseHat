from sense_hat import SenseHat
from  time import sleep

sense = SenseHat()

r = 255
g = 255
b = 255

blue = (0,0,255)
playerX = 4
playerY = 3

sense.clear(0,0,0)
sense.set_pixel(playerX,playerY,blue)

def shoot():
	global playerY
	global playerY
	shotX = playerX 
	shotY = playerY + 1
	while shotX < 7 and shotY < 8 and shotX > 0 and shotY > 0:
		sense.set_pixel(shotX,shotY,(r,g,b))
		shotY = shotY + 1
		sleep(0.09)
	sense.clear(0,0,0)
	sense.set_pixel(playerX,playerY,blue)
def up():
	global playerY
	if  playerY > 0:
		sense.clear(0,0,0)
		playerY = playerY -1
		sense.set_pixel(playerX,playerY,blue)
def down():
	global playerY
	if playerY < 7:
		sense.clear(0,0,0)
		playerY = playerY +1
		sense.set_pixel(playerX,playerY,blue)
def left():
	global playerX
	if playerX > 0:
		sense.clear(0,0,0)
		playerX = playerX -1
		sense.set_pixel(playerX,playerY,blue)
def right():
	global playerX
	if playerX < 7:
		sense.clear(0,0,0)
		playerX = playerX +1
		sense.set_pixel(playerX,playerY,blue)

sense.stick.direction_up = up
sense.stick.direction_down = down
sense.stick.direction_left = left
sense.stick.direction_right = right
sense.stick.direction_middle = shoot
while True:
	pass #Keeps program running
