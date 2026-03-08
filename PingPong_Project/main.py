from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My first Pong Game")
screen.tracer(0)
r_paddle = Paddle(350,0 )
l_paddle = Paddle(-350, 0 )

screen.listen()



screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # Detect right paddle collision miss
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()

    # Detect left paddle collision miss
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()