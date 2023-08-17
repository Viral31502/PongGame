from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from score_board import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")

player = Paddle(cord=(350, 0))
player_score = ScoreBoard(color="green", pos=(20, 240))

pc = Paddle(cord=(-350, 0))
pc_score = ScoreBoard(color="Red", pos=(-20, 240))
ball = Ball()
x = 1
y = 1

screen.listen()

screen.onkey(player.upward, "Up")
screen.onkey(player.downward, "Down")
screen.onkey(pc.upward, "w")
screen.onkey(pc.downward, "s")
is_running = True

while is_running:
    screen.update()
    time.sleep(0.1)
    ball.ball_move(x, y)

    # change direction on contact with vertical wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        y *= -1

    # change direction on contact with any player
    if (player.distance(ball) < 50 and ball.xcor() > 335) or (pc.distance(ball) < 50 and ball.xcor() < -335):
        x *= -1
        ball.x_move += 2
        ball.y_move += 2
        # print("pc SCores")
    if ball.xcor() > 351:
        x *= -1
        ball.reset_ball()
        print("pc scores")
        pc_score.add_score()
    elif ball.xcor() < -351:
        x *= -1
        ball.reset_ball()
        print("Player score")
        player_score.add_score()

print(f"{max(player_score.score, pc_score.score)}")

screen.exitonclick()
