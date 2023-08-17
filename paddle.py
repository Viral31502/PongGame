from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,cord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(cord)

    def movement(self, caller):
        present_pos = self.ycor()
        if caller == 1:
            direction = -20
        else:
            direction = 20
        self.sety(direction + present_pos)

    def upward(self):
        self.movement(0)


    def downward(self):
        self.movement(1)


