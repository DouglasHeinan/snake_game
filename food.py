from turtle import Turtle
import random

class Food(Turtle):

    """This function creates an object that will serve as food for the snake and places it in a random location"""
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 265)
        self.goto(random_x, random_y)


    """
    After the snake head 'eats' (makes contact with) the food, 
    this function moves the food to a new random location.
    """
    def new_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 265)
        self.goto(random_x, random_y)
        