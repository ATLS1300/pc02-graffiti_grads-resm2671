#!/usr/bin/env python
# coding: utf-8

'''
Author: Bekah Smith
Sep 4, 2021
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("coral")
panel.bgpic(image)

#=======Add your code here======

#Set up turtle and coordinates
turtle.hideturtle()
turtle.up()
turtle.speed(10)
forehead = (-105, 175)
bezoschin = (15,15)
cloudone = (-323,72)
cloudtwo = (-190,130)
cloudthree = (243,60)
cloudfour = (350,150)
cloudfive = (170,160)
cloudsix = (-268,30)
cloudseven = (146,99)
lightningstart = (130,180)
fingertip = (111, -90)

#draw hat
turtle.goto(forehead)
turtle.left(90)
turtle.down()
turtle.pensize(6)
turtle.pencolor("green")
turtle.fillcolor("cadetblue")
turtle.begin_fill()
turtle.forward(80)
turtle.right(90)
turtle.forward(180)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(180)
turtle.right(90)
turtle.end_fill()
turtle.up()

#draw bezos surprised mouth
turtle.goto(bezoschin)
turtle.right(90)
turtle.down()
turtle.pensize(1)
turtle.speed(5)
turtle.pencolor("black")
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()
turtle.up()

#draw gathering storm clouds
turtle.color("DarkGrey")
turtle.speed(10)

turtle.goto(cloudone)
turtle.down()
turtle.pencolor(102,95,95)
turtle.dot(190)
turtle.up()

turtle.goto(cloudtwo)
turtle.down()
turtle.pencolor(120,99,89)
turtle.dot(170)
turtle.up()

turtle.goto(cloudthree)
turtle.down()
turtle.pencolor(89,87,82)
turtle.dot(140)
turtle.up()

turtle.goto(cloudfour)
turtle.down()
turtle.pencolor(82,81,79)
turtle.dot(165)
turtle.up()

turtle.goto(cloudfive)
turtle.down()
turtle.pencolor(66,71,63)
turtle.dot(190)
turtle.up()

turtle.goto(cloudsix)
turtle.down()
turtle.pencolor(77,80,79)
turtle.dot(165)
turtle.up()

turtle.goto(cloudseven)
turtle.down()
turtle.pencolor(69,70,82)
turtle.dot(90)
turtle.up()

#draw lightning to strike fingertip
turtle.pensize(10)
turtle.goto(lightningstart)
turtle.pencolor("yellow1")
turtle.down()

frog = turtle.clone()  #clone turtle to make lightning load better

turtle.forward(75)
turtle.right(120)
turtle.forward(140)
turtle.left(120)
frog.right(103)
frog.forward(150)
turtle.forward(50)
turtle.right(128)
frog.left(103)
frog.forward(30)
turtle.forward(140/1.618)
turtle.left(128)
turtle.forward(25)
frog.left(112)
frog.goto(fingertip)
turtle.goto(fingertip)

#draw three lazers shooting from finger
turtle.up()
turtle.goto(fingertip) 
turtle.right(11)
turtle.pencolor("red")
turtle.pensize(5)
turtle.down()
turtle.forward(30)
turtle.up()
turtle.forward(50)
turtle.down()
turtle.forward(30)
turtle.up()
turtle.forward(50)
turtle.down()
turtle.forward(30)
turtle.up()

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
