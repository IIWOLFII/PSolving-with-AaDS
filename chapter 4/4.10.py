# def largest_number(l: list):
#     if not l:
#         return None
#
#     if len(l) <= 1:
#         return l[0]
#
#     if l[0] < largest_number(l[1:]):
#         return largest_number(l[1:])
#     else:
#         return l[0]

def movedisk(a, b, reccount):
    global poles
    hand = poles[a-1].pop(0)
    poles[b-1].insert(0,hand)
    print(f'{reccount}:' ,poles)



# holy FUCK this hanoi problem
# def tower(height, frm, to):
#     poles = {1:'A',2:'B',3:'C'}
#     fromlist = poles[frm]
#     tolist = poles[to]
#     other = 6 - (frm + to)
#     if len(fromlist) < 1:
#         return
#     hand = fromlist.pop(0)
#     tolist.insert(0, hand)
#     if tolist[0] < hand:
#         tower(height-1,frm, to)
#     else:
#         tower(height - 1, frm, other)
#     print(poles)
# i give up, time for youtube videos
class Recursion():
    def __init__(self):
        self.reccount = 0

    def tower(self,height, frm, to):
        self.reccount += 1
        other = 6 - (frm + to)  # in sequence of 1 2 3, with input of two of these (frm + to), returns the third one  3 + 2 +1 = 6

        if height == 1: #base case works for n 1
            return movedisk(frm, to, self.reccount)

        self.tower(height - 1, frm, other)  # we move all but the one at the base 'out of the way' so ...
        movedisk(frm, to, self.reccount)  # ... base disk can be moved to end location
        self.tower(height - 1, other, to)  # then we move the out of the way pile to destination



# pole1.insert(0,'value')
# print(pole1.pop(0))
p1 = [1, 2, 3]
p2 = list()
p3 = list()

poles = [p1, p2, p3]

print('starting with:', poles)
p = Recursion()

p. tower(len(p1), 1, p1[-1])
