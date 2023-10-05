from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.current_score = 0
        self.write_score()

    def increase_score(self):
        self.clear()
        self.current_score += 1
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.current_score}", move=False,
                   align=ALIGNMENT, font=FONT)

    def write_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT,
                   font=FONT)
