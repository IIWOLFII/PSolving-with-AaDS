#holy FUCK this hanoi problem
def largest_number(l: list):
    if not l:
        return None

    if len(l) <= 1:
        return l[0]

    if l[0] < largest_number(l[1:]):
        return largest_number(l[1:])
    else:
        return l[0]

# gh = [2,4,1,2,-5,20]
# print(largest_number(gh))
def tower(frm, to, mink = None):
    global poles

    if len(poles[0]) == 0 and len(poles[1]) == 0:
        return

    if not mink:
        mink = max(poles[0])


    hands = poles[frm].pop(0)

    if len(poles[2]):
        if poles[2][0] > hands:
            return tower(0, 1, mink)

    poles[to].insert(0,hands)

    print(poles)





# pole1.insert(0,'value')
# print(pole1.pop(0))
p1 = [1,2]
p2 = list()
p3 = list()

poles = [p1,p2,p3]

print('starting with:', poles)
tower(0,2)




