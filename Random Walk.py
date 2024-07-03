from turtle import Turtle, Screen
import random

halo = Turtle()
halo.color("green")

colours = ["green","red","blue","purple","brown"]
directions = [0,90,180,270]
halo.pensize(15)
halo.speed("fastest")

for blank in range(200):
    halo.color(random.choice(colours))
    halo.forward(30)
    halo.setheading(random.choice(directions))
    

screen = Screen()
screen.exitonclick()
