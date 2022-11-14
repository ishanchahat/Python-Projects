#Testing Your Program is very very important

import turtle

win = turtle.Screen()
win.title("Pong by @ishanpandey_13")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


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
ball.speed(0)#speed of animation,sets speed to maximum possible speed otherwise things will get slow
ball.shape("circle")
ball.color("white")
ball.penup()#turtles draw lines while moving since we do not need it in our game so we use the function penup to avoid drawing lines
ball.goto(0, 0)#This shows swhere our paddle will get started (-350, 0)are x and y coordinate respectively

#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")

    
    
    
#Main game loop
while True:
    win.update()
    
