#Pong Game based on this tutorial -https://youtu.be/LH8WgrUWG_I
#Added graphics and sound
#Add a game start countdown
# I played around with the Ai made it somtimes go in the wrong direction !!
#Created on IDLE on Mac sound would need to be changed for Windows or Linux

#Need to do this to get the keys to repeat

#defaults write -g ApplePressAndHoldEnabled -bool false



import turtle
import os
import time
import random


wn = turtle.Screen()
wn.title ("Pong Game")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.bgpic("Stars_800_600.gif")
#Score
score_a = 0
score_b = 0


#Paddle A
paddle_a = turtle.Turtle()
turtle.register_shape("paddle_a.gif")
paddle_a.speed(0)
paddle_a.shape("paddle_a.gif")
#paddle_a.color("cyan")
#paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
turtle.register_shape("paddle_b.gif")
paddle_b.speed(0)
paddle_b.shape("paddle_b.gif")
#paddle_b.color("magenta")
#paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("square")
ball1.color("yellow")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 3
ball1.dy = 3

#Ball 2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("square")
ball2.color("yellow")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -2
ball2.dy = 2
ball2.ht()

#Ball 3
ball3 = turtle.Turtle()
ball3.speed(0)
ball3.shape("square")
ball3.color("yellow")
ball3.penup()
ball3.goto(0, 0)
ball3.dx = 1
ball3.dy = -1
ball3.ht()

#ball 2
ball4 = turtle.Turtle()
ball4.speed(0)
ball4.shape("square")
ball4.color("yellow")
ball4.penup()
ball4.goto(0, 0)
ball4.dx = -1
ball4.dy = 1
ball4.ht()

#balls = [ball1, ball2, ball3, ball4]
balls = [ball1]

ballcount =1

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Pen
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 0)

#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

    #AI function

def paddle_bai_up():
    y = paddle_b.ycor()
    y += (random.randint(-4,10))
    paddle_b.sety(y)

def paddle_bai_down():
    y = paddle_b.ycor()
    y -= (random.randint(-4,10))
    paddle_b.sety(y)

def time_delay():
    time_stamp = time.time()
    while time.time() < time_stamp + 20:
            print()    
def count_down():

    for count in range(3,0,-1):
        os.system("afplay sfx_menu_move4.wav&")
        pen2.write((count), align="center", font=("Courier", 30, "normal"))
        
        time.sleep(1)
        pen2.clear()
    
    
    

#Keyboard binding onkey or onkeypress
wn.listen()
wn.onkey(paddle_a_up, "w")
wn.onkey(paddle_a_down, "s")
wn.onkey(paddle_b_up, "Up")
wn.onkey(paddle_b_down, "Down")

count_down()

# Main Game Loop
while True:
    wn.update()
    for ball in balls:
        
        #Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

    

    #Border Checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            os.system("afplay bounce.wav&")

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            os.system("afplay bounce.wav&")
            
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            os.system("afplay sfx_sounds_falling3.wav&")
            #Pause countdown
            count_down()

            
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b +=1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            os.system("afplay sfx_sounds_falling3.wav&")
            #Pause countdown
            count_down()

  
#Paddle and Ball collisions

        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +50 and ball.ycor() > paddle_b.ycor() -50):
            ball.setx(340)
            ball.dx *= -1
            ball.color("magenta")
            
            os.system("afplay bounce.wav&")
            
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +50 and ball.ycor() > paddle_a.ycor() -50):
            ball.setx(-340)
            ball.dx *= -1
            ball.color("cyan")
            os.system("afplay bounce.wav&")




    # AI Player
    closest_ball = balls[0]
    for ball in balls:
        if ball.xcor() > closest_ball.xcor():
            closest_ball = ball

    #if ball.xcor() > ball2.xcor():
    if paddle_b.ycor() < closest_ball.ycor() and abs(paddle_b.ycor() -closest_ball.ycor()) > 10:        
        paddle_bai_up()

    elif paddle_b.ycor() > closest_ball.ycor()and abs(paddle_b.ycor() -closest_ball.ycor()) > 10:           
        paddle_bai_down()

  
    if score_a >4 or score_b>4:
       if ballcount == 1:
           balls.append(ball2)
           ball2.st()
           ballcount = 2
           
      
        
        
        
        
    
