#snake game
import turtle
import time
import random

#window 
win = turtle.Screen()
win.bgcolor("black")
win.window_height = 700
win.window_width = 700

#score
score = 0
high_score = 1
score_screen = turtle.Turtle()
score_screen.speed(0)
score_screen.color("white")
score_screen.penup()
score_screen.ht()
score_screen.goto(0, 300)
score_screen.write("SCORE: {} || High SCORE: {}".format(str(score), str(high_score)),move=False,align="left")
#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0,100)

#head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

delay = 0.15

#head movment
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)   

    if head.direction == "right":
        head.setx(head.xcor() + 20)

def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"

#assigning keys for movment
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

#movment updates
while True:
    win.update()
    if head.distance(food) < 20:
        food.goto(random.randint(-350, 350),random.randint(-350, 350))
    #Score increase
        score += 1
        score_screen.clear()
        score_screen.write("SCORE: {} || High SCORE: {}".format(score, high_score), move=False)
    #edges of the game
    if head.xcor() < -350 or head.xcor() > 350:
        score_screen.clear()
        score = 0
        score_screen.write("SCORE: {} || High SCORE: {}".format(score, high_score), move=False)
        head.goto(0,0)
        head.direction = "stop"
    if head.ycor() < -300 or head.ycor() > 300:
         score_screen.clear()
         score = 0
         score_screen.write("SCORE: {} || High SCORE: {}".format(score, high_score), move=False)
         head.goto(0,0)
         head.direction = "stop"
    #High score
    if score > high_score:
        high_score = score
        score_screen.clear()
        score_screen.write("Score: {} || High Score: {}".format(score,high_score), move=False,align="left")

    move()

    time.sleep(delay)
#holds the window open
win.mainloop()


