import turtle
import time
import random
 
delay = 0.05
score = 0
high_score = 0

delay2 = 0.1
score2 = 0

 
 
 
# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Xenzia Multiplayerz")
wn.bgcolor("black")

# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)
 


# head of the snake
head = turtle.Turtle()
head.shape("circle")
head.color("white")
head.penup()
head.goto(0, -100)
head.direction = "Stop"
 
# creating the second head of the snake
head2 = turtle.Turtle()
head2.shape("circle")
head2.color("gold")
head2.penup()
head2.goto(0, 100)
head2.direction = "Stop"


# food in the game
food = turtle.Turtle()
colors = random.choice([ 'green'])
shapes = random.choice([ 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 0)
 
# The scores in the game
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player I : 0 Player II : 0 High Score : 0", align="center",
          font=("candara", 24, "bold"))
 
 
 
# assigning key directions for player 1:
def group():
    if head.direction != "down":
        head.direction = "up"
 
 
def godown():
    if head.direction != "up":
        head.direction = "down"
 
 
def goleft():
    if head.direction != "right":
        head.direction = "left"
 
 
def goright():
    if head.direction != "left":
        head.direction = "right"
 
 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

# assigning key directions for player 2:
def group2():
    if head2.direction != "down":
        head2.direction = "up"
 
 
def godown2():
    if head2.direction != "up":
        head2.direction = "down"
 
 
def goleft2():
    if head2.direction != "right":
        head2.direction = "left"
 
 
def goright2():
    if head2.direction != "left":
        head2.direction = "right"
 
 
def move2():
    if head2.direction == "up":
        y = head2.ycor()
        head2.sety(y+20)
    if head2.direction == "down":
        y = head2.ycor()
        head2.sety(y-20)
    if head2.direction == "left":
        x = head2.xcor()
        head2.setx(x-20)
    if head2.direction == "right":
        x = head2.xcor()
        head2.setx(x+20)
         
wn.listen()
wn.onkeypress(group, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")
wn.onkeypress(group2, "w")
wn.onkeypress(godown2, "s")
wn.onkeypress(goleft2, "a")
wn.onkeypress(goright2, "d")

 
segments = []
segments2 = []
 

 
# Main Gameplay
while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, -100)
        head.direction = "Stop"
        colors = random.choice(['red', 'yellow', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.05
        pen.clear()
        pen.write("Player I : {} Player II : {} High Score : {} ".format(
            score, score2,  high_score), align="center", font=("candara", 24, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
 
        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(10)
        new_segment.shape("circle")
        new_segment.color("white")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("PLayer I : {}  Player II : {} High Score : {} ".format(
            score, score2, high_score), align="center", font=("candara", 24, "bold"))
    # Checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
 
            score = 0
            delay = 0.05
            pen.clear()
            pen.write("Player I : {} Player II : {}  High Score : {} ".format(
               score, score2, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)

    wn.update()
    if head2.xcor() > 290 or head2.xcor() < -290 or head2.ycor() > 290 or head2.ycor() < -290:
        time.sleep(1)
        head2.goto(0, 0)
        head2.direction = "Stop"
        colors = random.choice(['red', 'yellow', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment2 in segments2:
            segment2.goto(1000, 1000)
        segments2.clear()
        score2 = 0
        delay2 = 0.05
        pen.clear()
        pen.write("Player I  : {} Player II : {} High Score : {} ".format(
            score, score2, high_score), align="center", font=("candara", 24, "bold"))
    if head2.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
 
        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(10)
        new_segment.shape("circle")
        new_segment.color("gold")  # tail colour
        new_segment.penup()
        segments2.append(new_segment)
        delay2 -= 0.001
        score2 += 1
        if score2 > high_score:
           high_score = score2
        pen.clear()
        pen.write("Player I : {} Player II : {} High Score : {} ".format(
            score, score2, high_score), align="center", font=("candara", 24, "bold"))
    # Checking for head collisions with body segments
    for index2 in range(len(segments2)-1, 0, -1):
        a = segments2[index2-1].xcor()
        b = segments2[index2-1].ycor()
        segments2[index2].goto(a, b)
    if len(segments2) > 0:
        a = head2.xcor()
        b = head2.ycor()
        segments2[0].goto(a, b)
    move2()
    for segment2 in segments2:
        if segment2.distance(head2) < 20:
            time.sleep(1)
            head2.goto(0, 100)
            head2.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment2 in segments2:
                segment2.goto(1000, 1000)
            segments2.clear()
 
            score2 = 0
            delay2 = 0.1
            pen.clear()
            pen.write(" Player I : {} Player II : {} High Score : {} ".format(
                score, score2, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay2)