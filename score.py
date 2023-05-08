from turtle import Turtle

ALIGNMENT = 'center'
FONT =('Arial', 16, 'normal')

class Score(Turtle):

    """This creates a turtle object that runs a scoreboard"""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 270)
        self.color('white')
        self.score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)


    """This function adds one point to the users score each time their snake eats a food"""
    def increase(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)


    """This function displays a 'Game Over' Message and the user's final score after the game ends"""
    def final(self):
        self.clear()
        self.goto(0, 20)
        self.write(arg="Game Over", move=False, align=ALIGNMENT, font=FONT)
        self.goto(0, -20)
        self.write(arg=f"Final Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(0, -60)
        self.write(arg=f"High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)


    def reset(self, play):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(str(self.high_score))
        if play == "Y":
            self.score = 0