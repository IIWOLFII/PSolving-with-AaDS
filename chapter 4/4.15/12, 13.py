class jug():
    def __init__(self, cap):
        self.maxcap = cap
        self.capacity = 0

    def statusreport(func):
        def inner (self, *args, **kwargs):
            res = func(self, *args, **kwargs)
            print(f"Jug {self.maxcap}: {self.capacity}/{self.maxcap}")
            return res
        return inner

    @statusreport
    def update(self):
        pass

    @statusreport
    def empty(self):
        print("Emptying out jug of capacity", self.maxcap)
        self.capacity = 0

    @statusreport
    def fill(self):
        print("Filling jug of capacity", self.maxcap)
        self.capacity = self.maxcap

    @statusreport
    def pourintojug(self, destination):
        djug = destination
        print(f"Pouring water from jug {self.maxcap} to jug {djug.maxcap}")
        while djug.capacity != djug.maxcap:
            if self.capacity == 0:
                break
            djug.capacity += 1
            self.capacity -= 1

        djug.update()




jug4 = jug(4)
jug3 = jug(3)
required_amount = 2

# jug4 = jug(3)
# jug3 = jug(2)
# required_amount = 4 idk this is BFS search or whatever, so why is it here
                    # either way, slightly upset that idk how to even approach this

while jug4.capacity != required_amount:
    jug4.pourintojug(jug3)
    jug4.fill()

    if jug4.capacity == required_amount:
        break

    jug4.pourintojug(jug3)
    jug3.empty()
