#  greendingbat @ github java solution rewritten in python because i dont understand ..
#  ..  how he doesnt run into infinite loops
#
# https://github.com/greendingbat/missionaries-cannibals/blob/master/MissionariesAndCannibalsFinal.java
#
#  thank u greendingbat @ github

# personal notes:
#
# i shouldnt have tried spliced attempts such as MM CM CC
# actually he technically goes through m:c such as C CC M MC MCC MM MMC MMCC -- he handles these at safeMove() first IF
# i could not really handle it this way because of dumb representation of data
#
# i also didnt have proper 'rollback' system or 'peek' system which made everything harder
#
# sending single guy is not an issue as long as u handle it properly
#
# still dont understand why we iterate m and c in range of boat slots EXPLANATION by future me: ..
# .. because we cant load more than 2 of the same bruddas on the boat, despite that we still try 2x2 2x1 which is ..
# .. more than the limit, but we catch that at safemove first IF statement
#
# still dont understand how he doesnt get stuck in a loop by only looking at previous move ### future me doesnt get it
#
# note for future:
# if i dont get the problem at 2 hours then i should stop bashing my head in and just look up the solution
# even if i almost didnt find the solution

# actually this solution does an illegal move of moving 4 people at once with 4/4 and boat size of 2


def moveBoat(m, c, movenum):
    global leftM, leftC, rightM, rightC
    # direction of the boat can be derived from even-niess of move number

    if movenum % 2 == 0:
        # left ---> right

        leftM -= m
        leftC -= c
        rightM += m
        rightC += c

    elif movenum % 2 != 0:
        # left <--- right

        rightM -= m
        rightC -= c
        leftM += m
        leftC += c



def safeMove(m,c,movenum):

    moveBoat(m,c,movenum)
    if rightM < 0 or rightC < 0 or leftM < 0 or leftC < 0:  # this is where he handles MCC MMC MMCC
        # instant failure if at any bank we have -1 amount of people
        moveBoat(m, c, movenum + 1)
        return False
    elif leftM != 0 and leftM < leftC:
        # ungas eat missionaries on left bank
        moveBoat(m, c, movenum + 1)
        return False
    elif rightM != 0 and rightM < rightC:
        # ungas eat missionaries on right bank
        moveBoat(m, c, movenum + 1)
        return False
    else:
        moveBoat(m, c, movenum + 1)
        return True


def solve(prevmove = None):
    global movenum, solutionsequence

    if rightM == totalM and rightC == totalC:
        print('Solved!')
        return True

    for m in range(boatsize+1):  # i iterated by basically using range(2,0, -1) which takes infinitely longer
        for c in range(boatsize+1):  # im a dumbass
            currmove = f"{m=} {c=}"

            if (m == 0 and c == 0) or prevmove == currmove:
                continue # ignore zero moves or moves that undo the last move
                # i think he dodges going into a loop exactly here

            if safeMove(m,c,movenum):
                # make move
                moveBoat(m,c,movenum)
                if movenum % 2 == 0:
                    dir = "--->"
                elif movenum % 2 != 0:
                    dir = "<---"

                print(f"moving {m=} and {c=} {dir}")
                movenum += 1

                if solve(currmove):
                    solutionsequence += currmove + ' ' + dir + '\n'
                    return True

                # undo move
                movenum -= 1
                moveBoat(m,c,movenum+1) # undoes the move
                print('undoing')

    return False



people_per_group = 4

totalM = people_per_group
totalC = people_per_group

leftM = totalM
leftC = totalC

rightM = 0
rightC = 0

movenum = 0

boatsize = 2

solutionsequence = ""

print(f"Initial problem state {boatsize=} {leftM=} {leftC=}")

solve()

print('Solved with sequence of moves:')

print(solutionsequence)
