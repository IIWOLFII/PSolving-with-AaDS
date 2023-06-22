def testEqual(a,b):
    return print(a == b)

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

testEqual(reverse("hello"), "olleh")
testEqual(reverse("l"), "l")
testEqual(reverse("follow"), "wollof")
testEqual(reverse(""), "")
