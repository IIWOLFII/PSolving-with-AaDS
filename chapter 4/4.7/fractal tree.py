# blind attempt going off the resulting image
import turtle
import random as rng


# def maketree(turtl,branches,drawleaves=False):
#     length = 60
#     if branches > 0:
#         fred.forward(length/2*branches)
#         fred.right(20)
#         fred.forward(30)
#         maketree(turtl,branches-1)
#         fred.color('blue')
#         print('branch 1')
#         if drawleaves:
#             fred.dot(20,'green')
#         fred.left(180)
#         fred.forward(30)
#         fred.left(180)
#         fred.left(40)
#         fred.forward(30)
#         maketree(turtl,branches-1)
#         fred.color('red')
#         print('branch 2')
#         if drawleaves:
#             fred.dot(20,'green')
#         fred.left(180)
#         fred.forward(30)
#         fred.right(20)
#         fred.forward(length/2*branches)
# i dont get it

def randomcolor(brightness, mod):  # range of (brightness, 255)
    return int(min(((brightness + rng.randint(0, 255)) * mod), 255))


def randomangle(a=15, b=45):
    return rng.randint(a, b)


def color_the_branch(branches):
    red = int(40 * branches)
    green = (255 / (0.7 * branches)) % 255
    blue = 40
    capred = min(red, 120)
    return (int(capred), int(green), int(blue))

def color_the_foliage(brightness):
    red = randomcolor(brightness, 0.1)
    green = randomcolor(brightness, 0.8)
    blue = randomcolor(brightness, 0.4)
    return (red,green,blue)

def place_foliage(turtl,brightness):
    turtl.dot(rng.randint(10, 50), color_the_foliage(brightness))


def maketree(turtl, branches):
    brightness = 100  # 0 - 255
    length = rng.randint(20, 40) / 2 * branches
    angle = randomangle(30, 60)
    if branches > 0:
        turtl.pencolor(color_the_branch(branches))  # the thinner the stem the greener it is
        turtl.pensize(length / 8)  # width of the tree

        turtl.forward(length)  # initial trunk
        maketree(turtl, min(branches - 1, 1))  # pop off tiny tree where two big trunks connect
        #place_foliage(turtl, brightness) #foliage where branches connect

        turtl.right(angle)
        maketree(turtl, branches - 1)  # right recursive branch

        turtl.left(angle * 2)
        maketree(turtl, branches - 1)  # left recursive branch

        turtl.right(angle)  # look perpendicular to how we arrived
        turtl.backward(length)  # go back to tha roots

    else:  # means we're at the tip of the branch, slap a circle 'foliage'
        place_foliage(turtl,brightness)

fred = turtle.Turtle()
window = turtle.Screen()
window.colormode(255)

fred.left(90)
fred.backward(70)
fred.speed(0)

maketree(fred, 7)
window.exitonclick()
