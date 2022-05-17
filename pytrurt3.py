import turtle
s = turtle.getscreen()
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(25)
while True:
    for i in range(6):
        for colors in ["red","yellow","green","magenta","white","orange"]:
            turtle.color(colors)
            turtle.circle(100)
            turtle.left(10)
turtle.hideturtle()
turtle.mainloop()