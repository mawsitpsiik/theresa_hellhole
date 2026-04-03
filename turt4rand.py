import turtle
import time
import random

turtle.color("RED") #color of the line
turtle.Screen().bgcolor("black") #background color
turtle.width(3)
colorval = ["ORANGE", "YELLOW", "GREEN", "CYAN", "PURPLE", "WHITE"]

for x in range(6):
	for i in range(6): #hexagon now
		turtle.forward(50)
		turtle.right(60)
	turtle.color(colorval[x])
	xval = random.randint(0, 100)
	yval = random.randint(0, 100)
	turtle.goto(xval, yval)  #none of this works


'''
import random

xval = random.randint(30, 50)
yval = random.randint(30, 50)
'''

time.sleep(3)