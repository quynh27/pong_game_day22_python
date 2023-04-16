from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.l_score= 0
        self.r_score= 0
        self.update_scoreboard()
        
    
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-200,260)
        self.write(f'left_player {self.l_score}',False, 'center',('Courier',15,'normal'))
        self.goto(200,260)
        self.write(f'right_player {self.r_score}',False, 'center',('Courier',15,'normal'))
        

        
    def r_point(self):
        self.r_score +=1
        self.update_scoreboard()
        
    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()
        


    
        