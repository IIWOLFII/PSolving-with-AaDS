#hilbert curve
import turtle as tut



# looked it up at stack overflow and making the turns alternate makes it kinda work ..
# i still dont get why it kind of works


# looking at the only video about coding this fuckass curve, the guy eventually got to counting binary numbers
# also he uses coordinates of a box (x,y), makes sense considering this is a space filling curve


def draw1curve_left(t,dist,right = 1):
    t.forward(dist)
    t.left(90*right)
    t.forward(dist)
    t.left(90 * right)
    t.forward(dist)

def hilbertcurve(t,dist,depth, turn = 1):
    if depth <= 0:
        draw1curve_left(fred, dist, turn)
        return

    hilbertcurve(t, dist/2, depth - 1, turn)
    fred.right(90*turn)
    fred.forward(dist)
    hilbertcurve(t, dist/2, depth - 1, turn * -1)
    fred.left(90*turn)
    fred.forward(dist)
    fred.left(90*turn)
    hilbertcurve(t, dist/2, depth - 1, turn * -1)
    fred.forward(dist)
    fred.right(90*turn)
    hilbertcurve(t, dist/2, depth - 1, turn)





fred = tut.Turtle()
spawn = fred.pos()
fred.seth(0)
window = tut.Screen()
fred.speed(0)

clrs = ['red','blue','orange']

for i in range(3):
    fred.color(clrs[i])
    hilbertcurve(fred,100,i) # breaks at 3+
    fred.penup()
    fred.goto(spawn)
    fred.seth(0)
    fred.pendown()


# this is the closest ive gotten to this thing working
# if i comment out drawcurve() then its first order, if i comment them in then its second order
# how do i turn this into a recursion is the question

# #draw1curve_left(fred,50)
# fred.right(90)
# fred.forward(50)
# #draw1curve_right(fred,50)
# fred.left(90)
# fred.forward(50)
# fred.left(90)
# #draw1curve_right(fred,50)
# fred.forward(50)
# fred.right(90)
# #draw1curve_left(fred,50)

window.exitonclick()


# # i dont get it
#
# def draw1curve_right(t,dist):
#     t.forward(dist)
#     t.right(90)
#     t.forward(dist)
#     t.right(90)
#     t.forward(dist)
#
# def draw1curve_left(t,dist):
#     t.forward(dist)
#     t.left(90)
#     t.forward(dist)
#     t.left(90)
#     t.forward(dist)
#
# def hilbertcurve(t,dist,depth):
#     if depth <= 1:
#         return
#
#     hilbertcurve(t, dist/depth, depth - 1)
#     fred.left(90)
#     fred.forward(50)
#     hilbertcurve(t, dist/depth, depth - 1)
#     fred.left(90)
#     fred.forward(50)
#     fred.left(90)
#     hilbertcurve(t, dist/depth, depth - 1)
#     fred.forward(50)
#     fred.left(90)
#     hilbertcurve(t, dist/depth, depth - 1)



# # i dont get it
#
# def drawcurve(which,distance,t):
#     if which == "A":
#         t.forward(distance)
#         t.left(90)
#         t.forward(distance)
#         t.left(90)
#         t.forward(distance)
#     if which == "B":
#         pass
#     if which == "C":
#         pass
#     if which == "D":
#         pass
#
#
# def hcurve(t,depth):
#     distance = 30
#
#     if depth < 0:
#         return
#     elif depth % 4 == 0:
#         drawcurve('A',distance,t)
#         t.right(90)
#         t.forward(distance)
#     elif depth % 3 == 0:
#         drawcurve('B',distance,t)
#         t.left(90)
#         t.forward(distance)
#     elif depth % 2 == 0:
#         drawcurve('B',distance,t)
#         t.left(90)
#         t.forward(distance)
#     else:
#         drawcurve('B',distance,t)
#         t.left(90)
#         t.forward(distance)
#
#     hcurve(t, depth - 1)
#
#
#     pass