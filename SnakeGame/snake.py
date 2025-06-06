from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        x_cor = 0
        for _ in range(3):
            snake_part = Turtle('square')
            snake_part.penup()
            snake_part.color('white')
            snake_part.goto(x=x_cor, y=0)
            x_cor -= 20
            self.snake_segments.append(snake_part)

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            proceed_seg_x = self.snake_segments[seg_num - 1].xcor()
            proceed_seg_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(x=proceed_seg_x, y=proceed_seg_y)

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self):
        snake_part = Turtle('square')
        snake_part.penup()
        snake_part.color('white')
        self.snake_segments.append(snake_part)
        if self.head.heading() == UP:
            new_x = self.snake_segments[-1].xcor()
            new_y = self.snake_segments[-1].ycor() - 20
        elif self.head.heading() == DOWN:
            new_x = self.snake_segments[-1].xcor()
            new_y = self.snake_segments[-1].ycor() + 20
        elif self.head.heading() == LEFT:
            new_x = self.snake_segments[-1].xcor() - 20
            new_y = self.snake_segments[-1].ycor()
        else:
            new_x = self.snake_segments[-1].xcor()   + 20
            new_y = self.snake_segments[-1].ycor()
        snake_part.goto(new_x, new_y)

