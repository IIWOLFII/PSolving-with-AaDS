# connector replaces the inputs inside by itself
# when we call last gate it looks at it input to try and do get_output
# instead of it being None (it would call input if that would be the case)
# it is connector class that looks at output of previous gate then performs get output then looks at inputs and its
# connector class again
# do this until we reach first gates where inputs are actually None (output is being listened at by connector class)
# then it goes back to the top


class LogicGate():
    instcount = 0
    def __init__(self, label = None):
        self.label = label
        if label == None:
            LogicGate.instcount += 1
            self.label = f"G{LogicGate.instcount}"
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

    def ttable(self):
        if hasattr(self, "pin_b"):
            testnumbers = [(0, 0), (0, 1), (1, 0), (1, 1)]
        else:
            testnumbers = [(0, 0), (1, 1)]
        testgate = self
        L = []
        for i in testnumbers:
            def get_pin_a(): #original implementation made me do this
                return i[0]
            setattr(testgate, "get_pin_a", get_pin_a)

            def get_pin_b():
                return i[1]
            setattr(testgate, "get_pin_b", get_pin_b)

            L.append(testgate.perform_gate_logic())
        print(f"Truth table for {self.label}:\n"
              f"Input1 | Input2 | Output")
        for i,l in zip(testnumbers,L):
            print("{:^7} {:^7} {:^10}".format(i[0], i[1], l))
###############################
class UnaryGate(LogicGate):
    def __init__(self, label = None):
        super().__init__(label)
        self.pin_a = None
        #self.testing()

    def get_pin_a(self):
        if self.pin_a == None:
            return int(input(f"Input pin_a for {self.label}\n"))
        else:
            return self.pin_a.get_from().get_output()

    def set_next_pin(self, source): # i dont get this bullshit
        if self.pin_a == None:
            self.pin_a = source
        else:
            raise RuntimeError("Error: Empty Pins")
class BinaryGate(LogicGate):
    def __init__(self, label = None):
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            return int(input(f"Input pin_a for {self.label}\n"))
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b == None:
            return int(input(f"Input pin_b for {self.label}\n"))
        else:
            return self.pin_b.get_from().get_output()

    def set_next_pin(self, source): # awful
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                raise RuntimeError("Error: Empty Pins")
###############################
class AndGate(BinaryGate):
    def __init__(self, label = None):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a and b:
            return 1
        else:
            return 0
class OrGate(BinaryGate):
    def __init__(self, label = None):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a or b:
            return 1
        else:
            return 0
class NotGate(UnaryGate):
    def __init__(self, label = None):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        if a == 1:
            return 0
        if a == 0:
            return 1
###############################
class NOrGate(BinaryGate):
    def __init__(self, label = None):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a or b:
            return 0
        else:
            return 1
class NAndGate(BinaryGate):
    def __init__(self, label = None):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a and b:
            return 0
        else:
            return 1
###############################
class Connector():
    def __init__(self, fgate, tgate):
        self.fromg = fgate
        self.tog = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.fromg

    def get_to(self):
        return self.tog
###############################

g1 = AndGate()
# g2 = AndGate()
# g3 = AndGate()
g4 = NotGate()
# g5 = AndGate()
g6 = NAndGate("ImportantGate")
#
# print(g5.get_label())
# print(g6.get_output())
#
g6.ttable()

############################

# g1 = NAndGate("G1")
# g2 = AndGate("G2")
# g3 = OrGate("G3")
# c1 = Connector(g1,g3)
# c2 = Connector(g2,g3)
#
# g4 = NAndGate("G1")
# g5 = NAndGate("G2")
# g6 = AndGate("G3")
# c3 = Connector(g4,g6)
# c4 = Connector(g5,g6)
#
# if g3.get_output() == g6.get_output():
#     print(True)
# else:
#     print(False)
###############################
# g1 = AndGate("G1")
# g2 = AndGate("G2")
# g3 = OrGate("G3")
# g4 = NotGate("G4")
# c1 = Connector(g1, g3)
# c2 = Connector(g2, g3)
# c3 = Connector(g3, g4)
#
# print(g4.get_output())
# g4.ttable()


