import turtle

#Set the turtle screen
window = turtle.Screen()
tur=turtle.Turtle()
scr=tur.getscreen()
#title of the screen
scr.title("Merry Christmas")
#backgroundcolor of screen
scr.bgcolor("Light Blue")

tur.color("green")
tur.pensize(5)
tur.begin_fill()


# Creating Right half of the tree
tur.forward(100)
tur.left(150)
tur.forward(90)
tur.right(150)
tur.forward(60)
tur.left(150)
tur.forward(60)
tur.right(150)
tur.forward(40)
tur.left(150)
tur.forward(100)
tur.end_fill()

    #left half of the tree
tur.begin_fill()
tur.left(60)
tur.forward(100)
tur.left(150)
tur.forward(40)
tur.right(150)
tur.forward(60)
tur.left(150)
tur.forward(60)
tur.right(150)
tur.forward(90)
tur.left(150)
tur.forward(133)
tur.end_fill()

#Creating the trunck of the tree
tur.color("red")
tur.pensize(1)
tur.begin_fill()
tur.right(90)
tur.forward(80)
tur.right(90)
tur.forward(40)
tur.right(90)
tur.forward(80)
tur.end_fill()

#Creating the balls on the Christmas Tree
tur.penup()
tur.color("red")
tur.goto(110,-10)
tur.begin_fill()
tur.circle(10)
tur.end_fill()

tur.penup()
tur.color("red")
tur.goto(-120,-10)
tur.begin_fill()
tur.circle(10)
tur.end_fill()

tur.penup()
tur.color("yellow")
tur.goto(100,40)
tur.begin_fill()
tur.circle(10)
tur.end_fill()



tur.penup()
tur.color("yellow")
tur.goto(-105,38)
tur.begin_fill()
tur.circle(10)
tur.end_fill()

tur.penup()
tur.color("red")
tur.goto(85,70)
tur.begin_fill()
tur.circle(7)
tur.end_fill()

tur.penup()
tur.color("red")
tur.goto(-95,70)
tur.begin_fill()
tur.circle(7)
tur.end_fill()

#Drawing the bells using turtle.
tur.shape("triangle")
tur.fillcolor("yellow")
tur.goto(-20,30)
tur.setheading(90)
tur.stamp()
tur.fillcolor("red")
tur.goto(20,60)
tur.setheading(90)
tur.stamp()
tur.goto(-40,75)
tur.setheading(90)
tur.stamp()

# Printing the star using for loop
tur.speed(1)
tur.penup()
tur.color("yellow")
tur.goto(-20,110)
tur.begin_fill()
tur.pendown()

for i in range(5):
    tur.forward(40)
    tur.right(144)

tur.end_fill()

# Display the message on the screen
tur.penup()
message="Merry Christmas!!!"
tur.goto(-10,-180)
tur.color("Orange")
tur.pendown()
tur.write(message,move=False,align="center",font=("Arial",15,"bold"))
tur.hideturtle()
turtle.d