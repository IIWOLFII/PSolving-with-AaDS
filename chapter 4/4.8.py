import math
import turtle
from math import cos,sin,tan
import random as rng

################### \/ \/ \/
#blind playthrough
def triangle(t,degree,distance = 300):
    turn = 120
    if degree > 0:
        t.fillcolor((min(255,(40 * degree*2)), 0, min(255,int(40 * degree / 2))))
        t.begin_fill()
        for _ in range(3):
            t.right(120)
            t.forward(distance/2)
            t.right(turn)
            triangle(t,degree-1,int(distance/2))
            t.left(turn)
            t.forward(distance / 2)
        t.end_fill()
#different approach, oops
################### /\ /\ /\

################### \/ \/ \/
# got it right, nice
def draw_a_triangle(t,distance):
    t.begin_fill()
    pos = []
    for _ in range(3):
        pos.append(t.pos())
        t.left(120)
        t.forward(distance)
    t.end_fill()
    return pos

def triangle_filled(t,degree,distance = 300, pos = None):
    if degree > 0:
        t.fillcolor((
            max(0, 40+ int(cos(degree*0.4)*100)),
            max(0, 50+ int(tan(degree)*50) ),
            max(0, 120+ int(sin(degree)*130))
        ))

        # #red = int(t.ycor()*70)
        # red = 50
        # green = int(5*t.xcor())
        # blue = int(255-t.ycor())
        #
        # color = (red%255,green%255,blue%255)
        #
        # colorclipped = (
        #     max(0,min(255,red)),
        #     max(0, min(255, green)),
        #     max(0, min(255, blue))
        # )
        #
        # t.fillcolor(color)
        # t.begin_fill()

        # avg = int(((red + green + blue)/3)-30)%255
        # t.pencolor(avg,avg,avg)


        pos = draw_a_triangle(t,distance)
        posmiddles = list()

        for i in [1,2]:
            x = (pos[0][0] + pos[i][0])/2
            y = (pos[0][1] + pos[i][1])/2
            posmiddles.append((x,y))
        posmiddles.append(pos[0])

        for i in posmiddles:
            t.goto(i)
            triangle_filled(t,degree-1,int(distance/2),pos)


fred = turtle.Turtle()
fred.speed(0)
window = turtle.Screen()
window.colormode(255)
fred.forward(300)
fred.right(90)
fred.forward(480)
fred.left(90)
fred.pensize(2)

triangle_filled(fred,7,1000)

# fred.left(90)
# fred.forward(480)
# fred.right(90)
# fred.forward(300)
#
# triangle(fred,4,200)

window.exitonclick()




