import turtle

data = '''
++++++++++++++++++++++
+   +   ++ ++     +  O
+ +   +       +++ + ++
+ + +  ++  ++++   + ++
+++ ++++++    +++ +  +
+          ++  ++    +
+++++ ++++++   +++++ +
+     +   +++++++  + +
+ +++++++      S +   +
+                + +++
++++++++++++++++++O+++'''
class MazeConstructor():
    def __init__(self,t,data):
        self.reachedexit = False
        self.step = 10
        self.tiledist = 2
        self.turtxy = None
        self.t = t
        self.leveldata = {}
        self.draw_maze(data)

    def placetile(self):
        self.t.dot(10)
    def setspawn(self):
        self.turtxy = self.t.pos()
    def empty(self):
        pass
    def draw_maze(self,data):
        t = self.t
        step = self.step
        tiledist = self.tiledist
        y = 0
        x = 0

        things = {
            '+':self.placetile,
            'S':self.setspawn,
            '\n':self.empty,
            '.':self.empty,
            ' ':self.empty,
            'O':self.empty
        }

        for i in data:
            if i == '\n':
                y -= tiledist
                x = 0
            things[i]()
            self.leveldata[(x*step,y*step)] = i

            x += tiledist
            t.goto(x*step,y*step)

        t.goto(self.turtxy)
        t.speed(2)
        print(self.leveldata)

    def coordstep(self,xory,sign = 1):
        step = self.step
        tdsit = self.tiledist * sign
        t = self.t
        return t.pos()[xory]+tdsit * step


    def solve(self):
        leveldata = self.leveldata
        t = self.t
        pos = t.pos()

        if self.reachedexit:
            return

        up = (pos[0], self.coordstep(1,1))
        down = (pos[0], self.coordstep(1,-1))
        left = (self.coordstep(0,-1), pos[1])
        right = (self.coordstep(0,1), pos[1])

        t.dot(5,'blue')

        if leveldata[pos] == 'O':
            print("We're free!")
            self.reachedexit = True
        else:
            leveldata[pos] = '.'

        for direction in [up,down,left,right]:
            if direction not in leveldata:
                leveldata[direction] = ' '

            if leveldata[direction] not in '+.' and not self.reachedexit:
                t.goto(direction)
                self.solve()
        return

fred = turtle.Turtle()
fred.speed(0)
window = turtle.Screen()
window.colormode(255)
fred.penup()

maze = MazeConstructor(fred,data)
fred.speed(0)
maze.solve()

window.exitonclick()