import turtle
import time

turtle.color("RED") #color of the line
turtle.Screen().bgcolor("black") #background color
turtle.width(3)
colorval = ["ORANGE", "YELLOW", "GREEN", "CYAN", "PURPLE", "WHITE"]

for x in range(6):
	for i in range(6): #hexagon now
		turtle.forward(50)
		turtle.right(60)
	turtle.color(colorval[x])
	turtle.left(60)


time.sleep(3)