def testEqual(a,b):
    return print(a == b)

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

def remove_white(s):
    forbiddenchars = " '\""
    if len(s) <= 1:
        return s
    elif s[0] in forbiddenchars:
        return "" + remove_white(s[1:])
    else:
        return s[0] + remove_white(s[1:])

def is_pal(s):
    return s == reverse(s)

testEqual(is_pal(remove_white("x")), True)
testEqual(is_pal(remove_white("x")), True)
testEqual(is_pal(remove_white("radar")), True)
testEqual(is_pal(remove_white("hello")), False)
testEqual(is_pal(remove_white("")), True)
testEqual(is_pal(remove_white("hannah")), True)
testEqual(is_pal(remove_white('madam i"m adam')), True)
