from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup() # avoiding drawing lines
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1  # reverse the y(vertical) direction

    def bounce_x(self):
        self.x_move *= -1 # reverse the x(horizontal) direction

