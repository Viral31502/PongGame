from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, color, pos):
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        self.score = -1
        self.goto(pos)
        self.add_score()

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align="center", font=("courier", 40, "normal"))