from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("lightGreen")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def ball_move(self, x_dir, y_dir):
        x_cor = self.xcor() + self.x_move * x_dir
        y_cor = self.ycor() + self.y_move * y_dir
        self.goto(x_cor, y_cor)

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10