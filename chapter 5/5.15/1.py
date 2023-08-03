def hash_performance(occupied,total):
    load_factor = occupied/total
    success = 0.5*(1+(1/(1-load_factor)))
    unsuccess = 0.5*(1+(1/(1-load_factor))**2)
    return round(success,2),round(unsuccess,2)


total = 11

for loadpct in [10,25,50,75,90,99]:
    percentage = loadpct/100
    occupied = total * percentage
    succ,unsucc = hash_performance(occupied,total)
    print(f'Hash table performance for size {total} while {loadpct}% full:\nFor successful search: {succ}\nFor unsuccessful search: {unsucc}\n','=='*10)
