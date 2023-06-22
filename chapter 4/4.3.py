sumlist = [2,4,5,6,7] #sum = 24

def sum_a_list(input):
    summer = 0
    for i in input:
        print(f"summing {summer} and {i}")
        summer+= i
    return summer

print("=====================summing list using for loop")
print(sum_a_list(sumlist))

def sum_a_list_recursively(input):
    if len(input) == 1:
        print(f"returning {input[0]}")
        return input[0]
    else:
        print(f"returning sum of {input[0]} and sumalist({input[1:]})")
        return input[0] + sum_a_list_recursively(input[1:])

print("=====================summing list recursively")
print(sum_a_list_recursively(sumlist))