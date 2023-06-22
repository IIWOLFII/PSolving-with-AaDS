import turtle
import random as rng

#blind playthrough
def triangle(t,degree,distance = 300):
    turn = 120
    if degree > 0:
        t.fillcolor((min(255,(40 * degree*2)), 0, int(40 * degree / 2)))
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

fred = turtle.Turtle()
fred.speed(0)
window = turtle.Screen()
window.colormode(255)

triangle(fred,5)

window.exitonclick()