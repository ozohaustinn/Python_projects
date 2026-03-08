from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"final scores: left player {self.l_score}, right player {self.r_score} ", align=ALIGNMENT, font=("Courier", 20, "normal"))
