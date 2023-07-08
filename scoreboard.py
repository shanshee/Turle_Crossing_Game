from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-215, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def add_score(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER! Be more careful next time :( ", align="center", font=("Courier", 15, "normal"))
