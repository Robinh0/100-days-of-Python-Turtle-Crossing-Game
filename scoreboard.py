from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-280, 250)
        self.hideturtle()
        self.color('black')
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align='left', font=FONT)

    def next_level(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.color('black')
        self.write('GAME OVER', align='center', font=FONT)

