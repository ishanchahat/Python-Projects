import turtle
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(0, -200)
t.pendown()
t.begin_fill()
t.fillcolor('red')
t.left(45)
t.forward(200)
t.circle(100, 180)
t.right(90)
t.circle(100, 180)
t.forward(200)
t.end_fill()
t.hideturtle()
turtle.done()
