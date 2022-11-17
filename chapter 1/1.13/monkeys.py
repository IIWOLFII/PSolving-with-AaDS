class Fraction():
    def __init__(self, top, bottom):
        self.top = top
        self.bot = bottom

    def __str__(self):
        return (f"{self.top}/{self.bot}")

    def gcd(self, m, n):
        while m % n != 0:
            m, n = n, m % n
        return n

    def gcdreturn(self,newtop,newbot):
        gcd = self.gcd(newtop, newbot)
        return Fraction(newtop // gcd, newbot // gcd)

    def __add__(self, other):
        newtop = self.top * other.bot + other.top * self.bot
        newbot = self.bot * other.bot
        return self.gcdreturn(newtop,newbot)

    # Self Check
    #
    # To make sure you understand how operators are implemented in Python classes, and
    # how to properly write methods, write some methods to implement !!*!!, !!/!!, and !!-!! .
    # Also implement comparison operators > and <

    def __eq__(self, other):
        return self.top/self.bot == other

    def __gt__(self, other):
        return self.top/self.bot > other

    def __lt__(self, other):
        return self.top/self.bot < other

    def __mul__(self, other):
        newtop = self.top * other.top
        newbot = self.bot * other.bot
        return self.gcdreturn(newtop,newbot)

    def __truediv__(self, other):
        newtop = self.top * other.bot
        newbot = self.bot * other.top
        return self.gcdreturn(newtop,newbot)

    def __sub__(self, other):
        newtop = self.top * other.bot - other.top * self.bot
        newbot = self.bot * other.bot
        return self.gcdreturn(newtop,newbot)

f = Fraction(1, 3)
g = Fraction(1, 5)
h = f+g
j = Fraction(2,6)
print(f.top) #+
print(g.bot) #+
print(h) #+
print("substraction")
print(f-j) #+
print("multiplication")
print(f*j) #+
print("div")
print(f/j) #+
print(g>f) #+
print(g<f) #+
print(g==f) #+
print(f==j) #+
print(f!=j) #+