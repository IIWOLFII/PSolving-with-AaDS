# inventing from scratch so i understand this kind of
# kind of understood better i guess, still feels like im missing something

def movedisk(frm,to):
    global poles
    disk = poles[frm].pop(0)
    print(f"Moved disk {disk} from pole {frm} to pole {to}.")
    poles[to].insert(0,disk)
    print(poles)
    return poles

def hanoi(frm,to,height):
    global poles
    other = 3 - (frm+to)

    if height <= 0:
        return

    hanoi(frm, other, height - 1)
    movedisk(frm, to)
    hanoi(other, to, height - 1)



pole1 = ['A','B','C']
pole2 = []
pole3 = []
poles = [pole1,pole2,pole3]

print('Starting poles:', poles)

hanoi(0,2,len(pole1))

print('End poles:', poles)