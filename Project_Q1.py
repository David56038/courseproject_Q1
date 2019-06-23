import turtle as turtle
from sys import argv

color = argv
prompt = '> '
print("Hi, I'd like to ask you a few questions about triangles.")
print("What color do you like for the first triange?")
color1 = input(prompt)

#Arguments for the X and Ycoordinates of the first trangle's vertices.
#def Q1.1(x,y)

#pen color or outline color is here
#turtle.pencolor()
#'black'

#triange 1
turtle.color(color1)
turtle.begin_fill()
turtle.position()
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(157.5)
turtle.forward(184.776)
tutle.end_fill()



#print("What color do you like for the second triange?")
#color2 = input(prompt)

#print("What color do you like for the third triange?")
#color3 = input(prompt)
