from turtle import *
bgcolor("black")
speed(100)

penup()
goto(0,0)
pendown()

def start():
    goto(0,-200)
    fillcolor("light yellow")
    begin_fill()
    color("yellow")
    pensize(2)
    penup()
    pendown()
    circle(200)
    end_fill()


def layer1():
    penup()
    goto(0,0)
    pendown()
    pensize(2)
    for i in range(6):
        for colors in ["Red", "pink", "light green", "green", "yellow", "white"]:
            color(colors)
            circle(90)
            left(10)
layer1()

def layer2():
    pencolor("black")
    fillcolor('#c4f5d5')
    begin_fill()
    penup()
    goto(0, -160)
    pendown()
    circle(160)
    end_fill()

layer2()

def layer2_2():
    fillcolor("red")
    begin_fill()
    pensize(2)
    color("black")
    penup()
    goto(0, -130)
    pendown()
    circle(130)
    end_fill()
layer2_2()

def layer2_3():
    pensize(2)
    color("white")
    penup()
    goto(0, -120)
    pendown()
    circle(120)
layer2_3()


def layer3():
    pensize(2)
    pencolor("green")
    left(90)
    for i in range(51):
        penup()
        goto(0, 0)
        right(20 + 1)
        forward(120)
        pendown()
        circle(15)

layer3()

def layer4():
    penup()
    goto(0,0)
    right(10)
    pendown()
    pensize(2)

    pencolor("green")
    fillcolor("light green")
    begin_fill()
    for i in range(4):
        forward(50)
        left(90)
for i in range (1,45):
    layer4()
    left(18)
    end_fill()

def layer5():
    pensize(1)
    pencolor("magenta")
    fillcolor("red")
    begin_fill()
    for i in range(23):
        circle(20)
        left(216+3)
    end_fill()
layer5()
exitonclick()
