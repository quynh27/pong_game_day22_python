from turtle import Turtle
#step 2 : create paddle  with width = 20, height=100, x_pos= 350 and y_pos=0


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
       
        self.goto(position)

        
    def go_up(self):
        new_y = self.ycor()+20
        
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor()-20
        
        self.goto(self.xcor(),new_y)


