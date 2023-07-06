#  fibonacci

def fib_up_to_n(num): #maybe i can do it without a list
    if num <= 1:
        return 1

    calc = fib_up_to_n(num -1) + fib_up_to_n(num -2)

    return calc


numtocount = 14

for i in range(numtocount):
    result = fib_up_to_n(i)
    print(fib_up_to_n(i))
    if result >= numtocount:
        break

# def fib_up_to_n(num, seq = None):
#     if not seq:
#         seq = [1,1]
#
#     seq.append(seq[-1]+seq[-2])
#
#     if seq[-1] < num:
#         fib_up_to_n(num, seq)
#
#     return seq
#
#
#
# print(fib_up_to_n(13))
