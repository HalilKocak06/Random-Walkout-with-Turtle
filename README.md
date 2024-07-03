Random Walk with Turtle Module


This Python project utilizes the Turtle graphics module to create a random walk pattern. The turtle moves randomly in different directions and changes color from a predefined list, resulting in a visually dynamic pattern.

Features


Generates a random walk pattern using the Turtle module.
Randomly selects colors from a predefined list.
Turtle changes direction randomly during the walk.
Adjustments can be made to customize the number of steps and pen size.
Installation
To run this project, ensure you have Python installed on your system. The Turtle module is part of the standard library and does not require additional installation.

Usage


Clone the repository:

bash
Copy code
git clone <your-repo-url>
cd <your-repo-directory>
Run the Python script:

bash
Copy code
python random_walk.py
The script will open a Turtle graphics window and display a random walk pattern. The window will close when you click on it.

Code Explanation


python
Copy code
from turtle import Turtle, Screen
import random

halo = Turtle()
halo.color("green")
colours = ["green", "red", "blue", "purple", "brown"]
directions = [0, 90, 180, 270]
halo.pensize(15)
halo.speed("fastest")

for _ in range(200):
    halo.color(random.choice(colours))
    halo.forward(30)
    halo.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()



Contributing


Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or pull request in the repository.
