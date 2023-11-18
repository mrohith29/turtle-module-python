import turtle
import colorsys
turtle.bgcolor("black")
turtle.tracer(100)
turtle.speed(100000)
def draw():
    h = 0
    n = 78
    turtle.up()
    turtle.goto(0, 60)
    turtle.down()
    turtle.pensize(5)
    for i in range(80):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        h+=1/n
        turtle.color(c)
        turtle.fd(33)
        turtle.circle(i, 10, 3)
        for k in range(i):
            turtle.fd(25)
            turtle.rt(36)
            turtle.bk(9)
            turtle.circle(k, 5,11)
            turtle.rt(90.2)

draw()
for p in range(17):
    draw()
turtle.done()