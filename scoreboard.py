from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score :{self.score}", False, "center", ("Comic Sans", 20, "normal"))
        self.highscore = 0

    def increase_score(self):
        self.clear()
        self.score = self.score+1
        self.write(f"Score :{self.score}", False, "center", ("Comic Sans", 20, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color("teal")
        self.write(f"Game Over! Your Score :{self.score}", False, "center", ("Comic Sans", 30, "normal"))
