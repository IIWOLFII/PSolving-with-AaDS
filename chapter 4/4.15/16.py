# Pascal’s triangle is a number triangle with numbers arranged in staggered rows such that
# Anr = n!/(r!(n-r)!)
# This is the equation for a binomial coefficient.You can build Pascal’s triangle by adding the two numbers
# that are diagonally above a number in the triangle. An example of Pascal’s triangle is shown below.

#         1
#       1   1
#     1   2   1
#   1   3   3   1
# 1   4   6   4   1

def fac(num):
    global global_fac_memo
    if num in global_fac_memo:
        return global_fac_memo[num]

    if num <= 1:
        return 1

    global_fac_memo[num] = num * fac(num - 1)
    return global_fac_memo[num]


def printrow(m, total):
    if m <= 0:
        return
    n = m - 1
    st = ''
    for r in range(m):
        anr = fac(n) // (fac(r) * fac(n - r))
        st += str(anr) + '  '
    print(st.center(total * 5, ' '))


def pasctriag(totalrows, currow=0):
    if currow == totalrows:
        printrow(currow, totalrows)
        return

    printrow(currow, totalrows)
    pasctriag(totalrows, currow + 1)


global_fac_memo = dict()

pasctriag(5)

# rows = 3
#
# printrow(1)
# printrow(2)
# printrow(3)

# for n in range(rows):
#     print(f'{n=}')
#     for r in range(rows):
#         anr = fac(n)//(fac(r)*fac(n-r))
#         print(anr,end='')
#         #anr = fac(n) // (fac(r) * fac(n - r))
#     print('')
