import turtle
import time
import random
'''
this code is written to be executed in Sublime Text, since that is capable
of opening its own windows to do the turtle drawing. I have no idea if it's
functional on other python/turtle instances, and I don't rather care
'''

turtle.color("red")
turtle.Screen().bgcolor("black") #background color
turtle.width(3)
turtle.speed(5)
screen = turtle.Screen()

seglist = [(-80,0), (-60, 0), (-40, 0), (-20, 0), (0,0)]

def movewest():
	abtCheck = seglist[4]
	abtAdd = ((abtCheck[0] - 20), abtCheck[1])
	turtle.penup()
	turtle.goto(seglist[0])
	turtle.color("black")
	turtle.pendown()
	turtle.dot()
	seglist.append(abtAdd)
	seglist.pop(0)

def moveeast():
	abtCheck = seglist[4]
	abtAdd = ((abtCheck[0] + 20), abtCheck[1])
	turtle.penup()
	turtle.goto(seglist[0])
	turtle.color("black")
	turtle.pendown()
	turtle.dot()
	seglist.append(abtAdd)
	seglist.pop(0)

def movesouth():
	abtCheck = seglist[4]
	abtAdd = ((abtCheck[0], abtCheck[1] - 20))
	turtle.penup()
	turtle.goto(seglist[0])
	turtle.color("black")
	turtle.pendown()
	turtle.dot()
	seglist.append(abtAdd)
	seglist.pop(0)

def movenorth():
	abtCheck = seglist[4]
	abtAdd = ((abtCheck[0], abtCheck[1] + 20))
	turtle.penup()
	turtle.goto(seglist[0])
	turtle.color("black")
	turtle.pendown()
	turtle.dot()
	seglist.append(abtAdd)
	seglist.pop(0)

def gothrulist():
	whichon = 0
	turtle.speed(0)
	for d in range(5):
			turtle.penup()
			turtle.goto(seglist[whichon])
			turtle.pendown()
			turtle.color("green")
			turtle.dot()
			whichon = (whichon + 1)
	turtle.color("red")

screen.onkeypress(gothrulist, "q")
screen.onkeypress(movewest, "a")
screen.onkeypress(movesouth, "s")
screen.onkeypress(moveeast, "d")
screen.onkeypress(movenorth, "w")




# def drawapple():
# 	for l in range(5): 
# 		turtle.penup()
# 		xval = random.randint(-225, 225)
# 		yval = random.randint(-225, 225)
# 		turtle.goto(xval, yval)
# 		turtle.pendown()
# 		turtle.dot(33, "purple")
# 		turtle.penup()
# 	turtle.goto(0,0)
# 	turtle.pendown()


screen.onkeypress(gothrulist, "r")

screen.listen()

turtle.mainloop()