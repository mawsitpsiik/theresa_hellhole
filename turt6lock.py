import turtle
import time
import random

turtle.color("red") #default, should be replaced
turtle.Screen().bgcolor("black") #background color
turtle.width(3)
turtle.speed(0)
turtle.hideturtle()
locdict = {1:(-300,0), 2:(-150,0), 3:(0,0), 4:(150,0), 5:(300,0)}

def whatshape(ws1, usrloc):
	if ws1 == 1:
		dotd(usrloc)
	elif ws1 == 2:
		lined(usrloc)
	elif ws1 == 3:
		triangled(usrloc)
	elif ws1 == 4:
		squared(usrloc)
	elif ws1 == 5:
		pentagond(usrloc)
	elif ws1 == 6:
		hexagond(usrloc)
	else:
		dotd(usrloc)
	'''
	I didn't know about dicts when i made this, but
	i'm a little scared of doing this with a dict
	'''

def dotd(dlocation):
	turtle.color("#ffffff")
	turtle.penup()
	turtle.goto(locdict[dlocation])
	turtle.seth(0) #east
	turtle.pendown()
	turtle.dot()

def lined(llocation):
	turtle.color("#0000ff")
	turtle.penup()
	turtle.goto(locdict[llocation])
	turtle.seth(135) #northwest
	turtle.forward(21.2)
	turtle.seth(0) #east
	turtle.pendown()
	for i in range(1): #line
		turtle.right(45)
		turtle.forward(42.4)

def triangled(tlocation):
	turtle.color("#ffff00")
	turtle.penup()
	turtle.goto(locdict[tlocation])
	turtle.seth(180) #west. placing the turtle so it draws from the right spot
	turtle.forward(0)
	turtle.seth(90) #north
	turtle.forward(30)
	turtle.seth(300) #downright
	turtle.pendown()
	for i in range(3): #triangle
		turtle.forward(60)
		turtle.right(120)

def squared(slocation):
	turtle.color("#00ff00")
	turtle.penup()
	turtle.goto(locdict[slocation])
	turtle.seth(135) #northwest
	turtle.forward(21.2)
	turtle.seth(0) #east
	turtle.pendown()
	for i in range(4): #square
		turtle.forward(30)
		turtle.right(90)

def pentagond(plocation):
	turtle.color("#ff0000")
	turtle.penup()
	turtle.goto(locdict[plocation])
	turtle.seth(162) #upleft
	turtle.forward(25.5)
	turtle.seth(36) #upright
	turtle.pendown()
	for i in range(5): #pentagon
		turtle.forward(30)
		turtle.right(72)


def hexagond(hlocation):
	turtle.color("#ff00ff")
	turtle.penup()
	turtle.goto(locdict[hlocation])
	turtle.seth(180) #west
	turtle.forward(15)
	turtle.seth(90) #north
	turtle.forward(25)
	turtle.seth(0) #east
	turtle.pendown()
	for i in range(6): #hexagon
		turtle.forward(30)
		turtle.right(60)

def main():
	usrinp = input("Put in five numbers, with values 6 OR LESS -> ")
	if len(usrinp) == 5:
		try:
			shp1 = int(usrinp[0])
			shp2 = int(usrinp[1])
			shp3 = int(usrinp[2])
			shp4 = int(usrinp[3])
			shp5 = int(usrinp[4]) 
			'''
			converts all the numbers to integers, so it goes
			from '33564' to ints reading 3, 3, 5, 6, 4
			'''
			print("success!")
		except:
			print("TRY AGAIN (int)")
			main()
	else:
		print("TRY AGAIN (length)")
		main()
	whatshape(shp1, 1)
	whatshape(shp2, 2)
	whatshape(shp3, 3)
	whatshape(shp4, 4)
	whatshape(shp5, 5)
	'''
	takes the 3, 3, 5, 6, 4 ints and runs 
	the "what shape is this number" function
	'''
main()

time.sleep(7)