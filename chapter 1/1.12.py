# Self Check
# Here’s a self check that really covers everything so far.
# You may have heard of the infinite monkey theorem?
# The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text,
# such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long do you think it would
# take for a Python function to generate just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”
#
# You’re not going to want to run this one in the browser, so fire up your favorite Python IDE.
# The way we’ll simulate this is to write a function that generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet
# plus the space. We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.
#
# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done.
# If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s progress
# this third function should print out the best string generated so far and its score every 1000 tries.

# Self Check Challenge
#
# See if you can improve upon the program in the self check by keeping letters that are correct and only modifying one character in the best string so far.
# This is a type of algorithm in the class of ‘hill climbing’ algorithms, that is we only keep the result if it is better than the previous one.
import random as rng

class Monkey:
    def __init__(self):
        self.goal = "methinks it is like a weasel" #len 28
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
        self.beststring = "".ljust(len(self.goal),"@") #permanent string across all loops

        self.lastscore = 0 #we track scores for if it is higher we report that

        self.goal = list(self.goal)  #work with indexes
        self.beststring = list(self.beststring) #work with indexes

        print("I live")

    def generate(self, myass = None):
        if myass is None:
            myass = self.alphabet
        output = ""
        for i in range(0,len(self.goal)): #generate an attempt with lenght of our goal
            output += rng.choice(myass)
        return output

    def addnewletters(self, string):
        string = list(string)
        for i in range(len(self.goal)):
            if string[i] == self.goal[i]:
                self.beststring[i] = string[i]

    def check(self):
        score = 0
        for i,f in zip(self.goal,self.beststring):
            if i == f:
                score += 1
        if score > self.lastscore:
            self.lastscore = score
            print(f"Solution is {(score/len(self.goal))*100:.2f}% accurate")
            print("".join(self.beststring))
            if (score/len(self.goal)) == 1: #if 100%
                return 100

    def doXpass(self,x):
        for i in range(0,x):
            if self.check() == 100:
                print("Iterations: %i" % (i))
                exit()
            else:
                self.addnewletters(self.generate())



ape = Monkey()
ape.doXpass(90)



