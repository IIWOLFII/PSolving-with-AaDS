#hilbert curve
import turtle as tut

# i dont get it

def drawcurve(which,distance,t):
    if which == "A":
        t.forward(distance)
        t.left(90)
        t.forward(distance)
        t.left(90)
        t.forward(distance)
    if which == "B":
        pass
    if which == "C":
        pass
    if which == "D":
        pass


def hcurve(t,depth):
    distance = 30

    if depth < 0:
        return
    elif depth % 4 == 0:
        drawcurve('A',distance,t)
        t.right(90)
        t.forward(distance)
    elif depth % 3 == 0:
        drawcurve('B',distance,t)
        t.left(90)
        t.forward(distance)
    elif depth % 2 == 0:
        drawcurve('B',distance,t)
        t.left(90)
        t.forward(distance)
    else:
        drawcurve('B',distance,t)
        t.left(90)
        t.forward(distance)

    hcurve(t, depth - 1)


    pass



fred = tut.Turtle()
fred.right(90)
window = tut.Screen()

hcurve(fred, 1)

window.exitonclick()
