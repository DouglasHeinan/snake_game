"""
Questions/thoughts/goals for this code:
--The little red food balls could be made to appear NOT in a space that the snake body is also in.
--There is a lag between the pressing of the arrow button and snake response.
--Plan to add high score tracking.
"""

from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

SCREEN = Screen()


def main():
    """This program runs a game of Snake, as used to be common on old phones"""
    SCREEN.setup(width=600, height=600)
    SCREEN.bgcolor('black')
    SCREEN.title("Hungry Snake")
    SCREEN.tracer(0)
    SCREEN.update()
    username = "place_holder"

    # with open(".snake_scores", "r") as f:
    #     x = f.read()
    #     print("contents of the file", x)

    snake = Snake()
    food = Food()
    score = Score()

    """While the game is not over, the snake continues moving forward one space every tenth of a second"""
    game_over = False
    while not game_over:
        """A series of onkey events to move the snake"""
        SCREEN.listen()
        SCREEN.onkey(snake.up, 'Up')
        SCREEN.onkey(snake.left, 'Left')
        SCREEN.onkey(snake.right, 'Right')
        SCREEN.onkey(snake.down, 'Down')
        SCREEN.update()
        time.sleep(.1)

        snake.move()

        """If the snake eats any of the randomly distributed food, it grows by one segment 
        and the user's score increases"""
        if snake.head.distance(food) < 15:
            food.new_food()
            snake.grow_snake()
            score.increase()

        """After each move, the program checks to see if the game has ended and, if so, 
        it displays the user's final score"""
        if game_end(snake):
            game_over = play_again(score, SCREEN, snake)

    # user_score = [username, score.score]
    # with open(".snake_scores", "r") as f:
    #     the_score = f.read()
    #     real_score = json.loads(the_score)
    #     real_score.append(user_score)
    # with open(".snake_scores", "w+") as f:
    #     f.write(json.dumps(real_score))

    SCREEN.exitonclick()


"""This function runs after each move to check for game-end conditions"""


def game_end(snake):
    game_over = False
    if snake.head.xcor() > 299 or snake.head.xcor() < -299:
        game_over = True
    if snake.head.ycor() > 299 or snake.head.ycor() < -299:
        game_over = True
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over = True
    return game_over


def play_again(score, screen, snake):
    play = screen.textinput("Play again?", "(Y or N )").upper()
    while play != "Y" and play != "N":
        play = screen.textinput("Y or N only, please.", "(Y or N)").upper()
    if play == "N":
        score.reset(play)
        score.final()
        return True
    else:
        score.reset(play)
        score.update()
        snake.reset()
        return False


if __name__ == '__main__':
    main()
