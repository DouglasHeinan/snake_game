from turtle import Turtle

MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POS = ((0, 0), (-20, 0), (-40, 0))

class Snake:

    '''
    This creates a list of the starting three segments that make up the snake and identifies the first segment in 
    that list as the snake's 'head'
    '''
    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]


    '''Creates a new snake at the start of the game'''
    def make_snake(self):
        for position in STARTING_POS:
            self.new_segment(position)


    '''Makes the snake bigger each time it eats a food'''
    def grow_snake(self):
        self.new_segment(self.segments[-1].position())


    '''Makes a snake segment'''
    def new_segment(self, position):
        segment = Turtle()
        segment.shape('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.make_snake()
        self.head = self.segments[0]

    '''Moves a snake forward'''
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)


    '''These four functions to control snake movement'''
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            









