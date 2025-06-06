from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"SCORE: {self.score}", align='center',font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def end_game(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align='center',font=('Arial', 24, 'normal'))
