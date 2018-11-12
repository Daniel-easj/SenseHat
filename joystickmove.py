from sense_hat import SenseHat
from  time import sleep
import random
sense = SenseHat()

r = 255
g = 255
b = 255

blue = (0,0,255)
red = (255,0,0)

playerX = 4
playerY = 0

enemyX = random.randint(0,7)
enemyY = random.randint(5,7)

enemyAlive = None
iterations = 0
if iterations == 0:
	enemyAlive = True

sense.clear(0,0,0)
sense.set_pixel(enemyX,enemyY,red)
sense.set_pixel(playerX,playerY,blue)

def checkCollision(pX,pY,eX,eY):
	++iterations
	if pX == eX and pY == eY:
		sense.set_pixel(random.ranint(0,7),random.randomint(5,7),(0,0,0))
		enemyAlive = false
		return true

def shoot(event):
	++iterations
	global playerY
	global playerY
	shotX = playerX 
	shotY = playerY + 1
	if event.action == 'pressed':
		while shotX <= 7 and shotY < 8 and shotX >= 0 and shotY >= 0:
			if checkCollision(playerX,playerY,enemyX,enemyY):
				break;
			sense.set_pixel(shotX,shotY,(r,g,b))
			shotY = shotY + 1
			sleep(0.09)
			sense.set_pixel(shotX,shotY-1,(0,0,0))
			sense.set_pixel(playerX,playerY,blue)
		sense.set_pixel(shotX,shotY-1,(0,0,0))
		sense.set_pixel(playerX,playerY,blue)
def up(event):
	++iterations
	global playerY
	if  playerY > 0 and event.action == 'pressed':
		sense.clear(0,0,0)
		playerY = playerY -1
		sense.set_pixel(playerX,playerY,blue)
		if enemyAlive:
			sense.set_pixel(enemyX,enemyY,red)
def down(event):
	++iterations
	global playerY
	if playerY < 7 and event.action == 'pressed':
		sense.clear(0,0,0)
		playerY = playerY +1
		sense.set_pixel(playerX,playerY,blue)
		if enemyAlive:
			sense.set_pixel(enemyX,enemyY,red)
def left(event):
	++iterations
	global playerX
	if playerX > 0 and event.action == 'pressed':
		sense.clear(0,0,0)
		playerX = playerX -1
		sense.set_pixel(playerX,playerY,blue)
		if enemyAlive:
			sense.set_pixel(enemyX,enemyY,red)
def right(event):
	++iterations
	global playerX
	if playerX < 7 and event.action == 'pressed':
		sense.clear(0,0,0)
		playerX = playerX +1
		sense.set_pixel(playerX,playerY,blue)
		if enemyAlive:
			sense.set_pixel(enemyX,enemyY,red)

sense.stick.direction_up = up
sense.stick.direction_down = down
sense.stick.direction_left = left
sense.stick.direction_right = right
sense.stick.direction_middle = shoot


while True:
	pass #Keeps program running
