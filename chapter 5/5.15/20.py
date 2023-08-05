import random as rng


def shell_sort(a_list, stepfac):
    big_step = len(a_list) // stepfac
    while big_step > 0:
        for steps in range(big_step):  # this makes it move every steps'th while not colliding with past results
            insertion_sort(a_list, steps, big_step)
        big_step //= stepfac


def insertion_sort(alist, steps, big_step):
    global comparisons
    for i in range(steps + big_step, len(alist),
                   big_step):  # steps + big_step is here so we skip comparing 0 and -4 - its like that 1 in range(1,len(list)) in insertion sort
        saved_value = alist[i]
        pos = i
        while pos >= big_step:  # curpos >= gap is so we dont address -1 index, other condition is that we dont do anything if cur val is bigger than prev val
            comparisons += 1
            if alist[pos - big_step] < saved_value:
                break
            alist[pos] = alist[pos - big_step]
            pos -= big_step
        alist[pos] = saved_value

listlen = 50

for i in range(2, listlen//4+1):
    a_list = [rng.randint(0,60) for _ in range(listlen)]
    comparisons = 0
    shell_sort(a_list, i)
    print(f'For divider of {i}, used {comparisons} comparisons')
