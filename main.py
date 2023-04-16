from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
#step 1: creat screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong game')
screen.tracer(0)
screen.listen()
# initialize paddle
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))


screen.onkey(key='Up',fun= r_paddle.go_up)

screen.onkey(key='Down',fun= r_paddle.go_down)

screen.onkey(key='w',fun= l_paddle.go_up)

screen.onkey(key='s',fun= l_paddle.go_down)



ball= Ball()
scoreboard= Scoreboard()



game_is_on = True
while game_is_on:

    ball.move()
    screen.update()
    time.sleep(ball.move_speed)
 
    #detect colison with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with paddle

    if ball.distance(r_paddle)<46 and ball.xcor()>320 or ball.distance(l_paddle)<46 and ball.xcor()<-320  :
        ball.bounce_x()
    
    #detect if the ball is out of edge

    # if right paddle misses it
    if ball.xcor()>380  :
        
       
       
        ball.reset_position()
        scoreboard.l_point()

    #if left paddle misses it:

    if ball.xcor() <-380:
       
        
        ball.reset_position()
        scoreboard.r_point()


  

    


   


screen.exitonclick()