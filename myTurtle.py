# myTurtle.py

import turtle
import math


def drawSquare(L=90):
    for _ in range(4):  # make a box
        turtle.left(90)
        turtle.forward(L)

def drawHex(L=40):
    for _ in range(6):
        turtle.left(60)
        turtle.forward(L)

def drawRectangle(L=50):
    for _ in 1,2:
        turtle.color("red")
        turtle.forward(L)
        turtle.left(90)
        turtle.color("green")
        turtle.forward(L*2)
        turtle.left(90)

def makeHouse(L=200):
    turtle.color("red")
    drawSquare(L)
    turtle.left(90)     # move to top of house
    turtle.forward(L)

    turtle.color("blue")
    turtle.left(45)
    turtle.forward(L/math.sqrt(2))
    turtle.left(90)
    turtle.forward(L/math.sqrt(2))
    turtle.color("yellow")
    turtle.left(90)
    turtle.forward(L*math.sqrt(2))
    turtle.color("red")
    turtle.right(135)
    turtle.forward(L)
    turtle.right(135)
    turtle.color("yellow")
    turtle.forward(L*math.sqrt(2))

def makeDottedArrow():
    turtle.reset()
    turtle.penup()
    turtle.left(180)
    turtle.forward(200)
    turtle.right(180)
    turtle.pendown()
    for i in range(20):
        turtle.forward(10+i)
        turtle.penup()
        turtle.forward(2)
        turtle.pendown()
    turtle.forward(11+i)

def drawFlower(L=80,petalColor="red", centerColor="orange"):
    turtle.reset()

    turtle.penup()
    turtle.goto(40,-40)  # moves the position but does not change the direction?
    turtle.pendown()

    turtle.fillcolor(petalColor)
    for _ in range(6):
        turtle.begin_fill()
        turtle.right(120)
        drawHex(L)
        turtle.left(180)
        turtle.forward(L)
        turtle.end_fill()
    
    turtle.fillcolor(centerColor)
    turtle.begin_fill()
    drawHex(L)
    turtle.end_fill()

def drawShape(functionName,L):
    functionName(L)

def choice(L = 50):
    direction = input('left or right?')
    if direction.strip().lower() == "left":
        turtle.left(60)
        turtle.forward(L)
    elif direction.strip().lower() == "right":
        turtle.right(60)
        turtle.forward(L)
    else:
        print("I don't understand.")

def forwardInPrison(d): # doesn't let the turtle go more than 100 units from the center
    while d > 0:
        if turtle.distance(0,0) > 100:
            angle = turtle.towards(0,0)
            turtle.setheading(angle)
        turtle.forward(1)
        d = d -1

def forwardInBox(d):  # like forward in prison but keeps the turtle in a box rather than a circle
    while d > 0:
        if math.fabs(turtle.xcor()) > 100 or math.fabs(turtle.ycor()) > 100:
            angle = turtle.towards(0,0)
            turtle.setheading(angle)
        turtle.forward(1)
        d = d-1
        

def drawSpiral(d):  # d is how far you can go from the center
    x = turtle.xcor()
    y = turtle.ycor()
    i=0
    while turtle.distance(x,y) <= d:
        turtle.forward(i/20)
        turtle.left(5)
        i=i+1

def forwardIfUp(d):
    if not turtle.isdown():
        turtle.forward(d)



# make a rectangle
turtle.reset()
#drawRectangle()

# make a house
turtle.reset()
#makeHouse()

# make a dotted line
turtle.reset()
#makeDottedArrow()

#turtle.reset()
#drawFlower(80, "purple", "yellow")

# passing a function
#drawShape(drawFlower,20)
""" turtle.reset()
drawShape(drawHex,5)
turtle.reset()
drawShape(drawSquare,300)
turtle.reset()
drawShape(drawRectangle(175)) """


""" for i in 20,40,60,80,100,120,140:
    turtle.left(20)
    forwardInPrison(i)
 """

 

#drawSpiral(200)

for i in 50, 80, 120, 140, 160:
    forwardInBox(i)
    turtle.left(20)

turtle.exitonclick()

