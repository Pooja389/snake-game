from turtle import *
import time,random
score_val = 0
with open("/Users/YC/Desktop/my_file.txt") as file:
    highest_score = int(file.read())
screen = Screen()
screen.setup(width=500,height=500)
screen.bgcolor("black")
screen.title("SNAKE GAME")

# snake head
betty = Turtle()
betty.shape("square")
betty.color("white")
betty.penup()

# snake food
food = Turtle()
food.shape("circle")
food.color("red")
food.shapesize(0.6)
food.penup()
food.goto(0,100)

# score
score = Turtle()
score.penup()
score.goto(-150,220)
score.pencolor("white")
score.write(f"score : 0 || highest score : {highest_score}",font=("Lucida Handwriting",16,"bold"))
score.hideturtle()

direction = "stop"
# functions
def move_up():
    global direction
    if direction != "down":
        direction = "up"

def move_left():
    global direction
    if direction != "right":
        direction = "left"

def move_down():
    global direction
    if direction != "up":
        direction = "down"

def move_right():
    global direction
    if direction != "left":
        direction = "right"

def move():
    if direction == "up":
        betty.setheading(90)
        betty.forward(20)
    if direction == "down":
        betty.setheading(270)
        betty.forward(20)
    if direction == "left":
        betty.setheading(180)
        betty.forward(20)
    if direction == "right":
        betty.setheading(0)
        betty.forward(20)

def update_score():
    score.clear()
    score.write(f"score : {score_val} || highest score : {highest_score}",font=("Aria",16,"normal"))
    with open("/Users/YC/Desktop/my_file.txt",mode = "w") as file:
        file.write(str(highest_score))

def reset_game():
    global score_val
    score_val = 0
    for body in bodies:
        body.goto(600,600)
    bodies.clear()    

    food.goto(0,200)
    betty.goto(0,0)
    betty.direction = "stop"
    update_score()
    screen.listen()
    screen.onkey(move_up,"Up")
    screen.onkey(move_left,"Left")
    screen.onkey(move_down,"Down")
    screen.onkey(move_right,"Right")
    screen.tracer(0)
    loop()

screen.listen()
screen.onkey(move_up,"Up")
screen.onkey(move_left,"Left")
screen.onkey(move_down,"Down")
screen.onkey(move_right,"Right")
screen.tracer(0)

bodies = []
def loop():
    global move_down,move_left,move_right,move_up
    global score_val,food,highest_score
    while True:
        
        screen.update()
        betty.speed(20)
        move()
        if betty.xcor() > 245 or betty.ycor() > 245 or betty.xcor() < -245 or betty.ycor() < -245:
            ask = screen.textinput(prompt= f"do you want to play again\nyour score is {score_val}",title="game over")
            if ask == "yes":
                reset_game()
            else:
                screen.bye()

        x = random.randint(-240,240)
        y = random.randint(-240,220)

        if betty.distance(food) < 13:
            food.goto(x,y)
        
    # snake body
        
            body = Turtle()
            body.shape("square")
            body.color("white")
            body.penup()
        
            bodies.append(body)

            score_val += 1  

            if score_val > highest_score:
                highest_score = score_val
            update_score()

        for body in range(len(bodies)-1,0,-1):
            x = bodies[body-1].xcor()
            y = bodies[body-1].ycor()
            bodies[body].goto(x,y)
        
        if len(bodies) > 0:
            x = betty.xcor()
            y = betty.ycor()
            bodies[0].goto(x, y)

        for body in bodies:
            if body.distance(betty)<20:
                break
        time.sleep(0.12)

loop()
screen.exitonclick()