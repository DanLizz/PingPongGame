from turtle import *

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.paddle1_score = 0
        self.paddle2_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-50, 220)
        self.write(self.paddle1_score, align=ALIGNMENT, font=FONT)
        self.goto(50, 220)
        self.write(self.paddle2_score, align=ALIGNMENT, font=FONT)

    def paddle1_point(self):
        self.paddle1_score += 1
        self.update_score()

    def paddle2_point(self):
        self.paddle2_score += 1
        self.update_score()
