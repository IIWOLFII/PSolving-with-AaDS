#blind attempt

def int_to_str_inbase(input,base):
    lookup = "0123456789ABCDEF"
    if input < base:
        return lookup[input]
    else:
        return int_to_str_inbase(input // base,base) + lookup[input % base]
# wtf it actually works


# a = 254
# thing = int_to_str_inbase(a,16)
# print(thing)
# print(type(thing))