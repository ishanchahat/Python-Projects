#Testing Your Program is very very important

import turtle

win = turtle.Screen()
win.title("Pong by @ishanpandey_13")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

#paddle A
paddle_a = turtle.Turtle()#small t for our module name and capital T for our class name
paddle_a.speed(0)#speed of animation,sets speed to maximum possible speed otherwise things will get slow
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)#since the length and width are 20 pixels by default by increasing width by 5 we are actually increasing the pixels of width by 20*5 that is 100
paddle_a.penup()#turtles draw lines while moving since we do not need it in our game so we use the function penup to avoid drawing lines
paddle_a.goto(-350, 0)#This shows swhere our paddle will get started (-350, 0)are x and y coordinate respectively

#Paddle B
paddle_b = turtle.Turtle()#small t for our module name and capital T for our class name
paddle_b.speed(0)#speed of animation,sets speed to maximum possible speed otherwise things will get slow
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)#since the length and width are 20 pixels by default by increasing width by 5 we are actually increasing the pixels of width by 20*5 that is 100
paddle_b.penup()#turtles draw lines while moving since we do not need it in our game so we use the function penup to avoid drawing lines
paddle_b.goto(350, 0)#This shows swhere our paddle will get started (-350, 0)are x and y coordinate respectively

#Ball
ball = turtle.Turtle()#small t for our module name and capital T for our class name
ball.speed(2)#speed of animation,sets speed to maximum possible speed otherwise things will get slow
ball.shape("circle")
ball.color("white")
ball.penup()#turtles draw lines while moving since we do not need it in our game so we use the function penup to avoid drawing lines
ball.goto(0, 0)#This shows swhere our paddle will get started (-350, 0)are x and y coordinate respectively
ball.dx = 0.2#This indicates from how many pixels does tha ball will move in x-axis
ball.dy = -0.2#This indicates from how many pixels does tha ball will move in y-axis

# Pen -- Display default score on the screen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()# we dont want any line moving after the turtle completed writing score
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center",font=("Courier", 24, "normal"))

#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
       
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")    
        
#Main game loop
while True:
    win.update()
    
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border Checking
    
    #Top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  #For reversing the direction of the ball
        
    #Bottom border    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
   
    #Right corner    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a += 1 #adds one to player a score because the ball went to the writer side of the window
        pen.clear() #first clear what is on the screen then update the score
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier", 24, "normal"))

    #Left corner    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b += 1
        pen.clear() 
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier", 24, "normal"))
     
    # Paddle and Ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40): # for middle contact of the paddle and for only one touch contact 
        ball.setx(340)
        ball.dx *= -1
             
    # for the second paddle just reverse the statement    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40): # for middle contact of the paddle and for only one touch contact 
        ball.setx(-340)
        ball.dx *= -1
        
        

    
   
        

    
