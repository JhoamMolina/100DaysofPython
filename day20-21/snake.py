from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        ts = Turtle("square")
        ts.color('white')
        ts.penup()
        ts.goto(position)
        self.segments.append(ts)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for snake_part_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_part_num - 1].xcor()
            new_y = self.segments[snake_part_num - 1].ycor()
            self.segments[snake_part_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)

    def move_right(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)
