import turtle
import time
import random

class SnakeGame:
    def __init__(self):
        # Window setup
        self.win = turtle.Screen()
        self.win.title("Snake Game")
        self.win.bgcolor("black")
        self.win.setup(width=700, height=700)
        self.win.tracer(0)

        # Game state
        self.score = 0
        self.high_score = 0
        self.delay = 0.1
        self.game_on = True

        # Initialize game objects
        self.create_snake()
        self.create_food()
        self.create_score_display()
        self.create_instruction_display()

        # Key bindings
        self.setup_controls()

    def create_snake(self):
        # Create snake head
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("red")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "stop"

        # Snake body segments
        self.segments = []

    def create_food(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("green")
        self.food.penup()
        self.food.goto(0, 100)

    def create_score_display(self):
        self.score_display = turtle.Turtle()
        self.score_display.speed(0)
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(0, 300)
        self.update_score_display()

    def create_instruction_display(self):
        instructions = turtle.Turtle()
        instructions.speed(0)
        instructions.color("white")
        instructions.penup()
        instructions.hideturtle()
        instructions.goto(0, -320)
        instructions.write("Controls: W/A/S/D to move | R to restart", align="center", font=("Arial", 14, "normal"))

    def setup_controls(self):
        self.win.listen()
        self.win.onkeypress(self.go_up, "w")
        self.win.onkeypress(self.go_down, "s")
        self.win.onkeypress(self.go_left, "a")
        self.win.onkeypress(self.go_right, "d")
        self.win.onkeypress(self.restart_game, "r")

    def move(self):
        # Move snake body
        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)

        # Move first segment to head
        if len(self.segments) > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.segments[0].goto(x, y)

        # Move head
        if self.head.direction == "up":
            self.head.sety(self.head.ycor() + 20)
        elif self.head.direction == "down":
            self.head.sety(self.head.ycor() - 20)
        elif self.head.direction == "left":
            self.head.setx(self.head.xcor() - 20)
        elif self.head.direction == "right":
            self.head.setx(self.head.xcor() + 20)

    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def add_segment(self):
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("grey")
        segment.penup()
        self.segments.append(segment)

    def update_score_display(self):
        self.score_display.clear()
        self.score_display.write(f"Score: {self.score} | High Score: {self.high_score}", 
                                align="center", font=("Arial", 24, "normal"))

    def check_collision(self):
        # Check for wall collision
        if (self.head.xcor() > 330 or self.head.xcor() < -330 or 
            self.head.ycor() > 330 or self.head.ycor() < -330):
            return True

        # Check for body collision
        for segment in self.segments:
            if self.head.distance(segment) < 20:
                return True
        return False

    def reset_game(self):
        # Update high score
        if self.score > self.high_score:
            self.high_score = self.score

        # Reset score and snake
        self.score = 0
        self.head.goto(0, 0)
        self.head.direction = "stop"

        # Hide segments
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()

        self.update_score_display()
        self.game_on = True

    def restart_game(self):
        if not self.game_on:
            self.reset_game()

    def run(self):
        while True:
            self.win.update()

            if self.game_on:
                if self.check_collision():
                    self.game_on = False
                else:
                    # Check for food collision
                    if self.head.distance(self.food) < 20:
                        self.food.goto(random.randint(-330, 330), random.randint(-330, 330))
                        self.add_segment()
                        self.score += 1
                        self.update_score_display()
                        self.delay *= 0.95  # Increase speed

                    self.move()

            time.sleep(self.delay)

# Create and run the game
if __name__ == "__main__":
    game = SnakeGame()
    game.run()


