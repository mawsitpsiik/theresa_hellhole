import turtle
import time
import random

turtle.color("red")
turtle.Screen().bgcolor("black") #background color
turtle.width(3)
turtle.speed(0)
colorval = ["ORANGE", "YELLOW", "GREEN", "CYAN", "PURPLE", "RED"]

turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
for x in range(36):
	for x in range(6):
		for i in range(6): #hexagon now
			turtle.forward(10)
			turtle.right(60)
		turtle.color(colorval[x])
		turtle.left(60)
	turtle.penup()
	turtle.goto(0,0)
	# turnval = random.randint(0,360)
	# turtle.right(turnval)
	xval = random.randint(-225, 225)
	yval = random.randint(-225, 225)
	turtle.goto(xval, yval)
	turtle.pendown()


time.sleep(3)