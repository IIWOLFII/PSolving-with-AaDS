import turtle as tut



# time wasted 2 hr
#
# actually seeing as it only does 1 'side' of the triangle per function, i may have gotten it but then ..
# .. tried to draw the entire triangle in 1 go, maybe thats much more complicated to do in recursion

def drawKochCurve (t,level,distance):  # copypaste because i can not figure this out
    if level == 0:
        t.forward(distance)
    else:
        drawKochCurve(t, level - 1, distance / 3)
        t.left(60)
        drawKochCurve(t, level - 1, distance / 3)
        t.right(120)
        drawKochCurve(t, level - 1, distance / 3)
        t.left(60)
        drawKochCurve(t, level-1, distance / 3)
        input()


def koch(t, depth, distance):  # im shit
    if depth <= 0:
        t.right(120)
        t.forward(distance)
        t.left(60)
        return

    # for depth of 3

    # forward
    # left 45
    # make recursion

    # forward
    # left 45
    # make recursion

    ####### n1
    t.forward(distance)
    t.left(60)
    koch(t,depth-1,distance/2)
    t.forward(distance)
    t.left(60)
    t.forward(distance)
    ####### n1

    # forward
    # left 45
    # make recursion
    # forward
    # left 45

    # no recursion return
    # rigth 90 + 45
    # forward
    # left 45


    # forward
    # left 45
    # forward

    # right 120
    # repeat 2 more times


fred = tut.Turtle()
window = tut.Screen()
fred.speed(4)

#koch(fred,1,100)

drawKochCurve(fred,2,100)

window.exitonclick()



# def fuckrec(t,dis):
#     t.left(45)
#     t.forward(dis)
#     t.right(90)
#     t.forward(dis)
#     t.left(45)