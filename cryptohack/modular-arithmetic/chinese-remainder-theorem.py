"""
Function that receives two arrays and sorts both based on
the values of one of them
"""
def sort_together(mods, ints):
    temp = [(x, y) for x, y in sorted(zip(mods, ints), reverse=True)]
    
    sorted_mods = []
    sorted_ints = []
    for x, y in temp:
        sorted_mods.append(x)
        sorted_ints.append(y)

    return sorted_mods, sorted_ints

"""
Solution to the Chinese Remainder Theorem (CTR) through 
sieving. Definetly no the most efficient method, but it's
sufficient for the problem.
"""
def sieving_ctr(mods, ints):
    sorted_mods, sorted_ints = sort_together(mods, ints)

    sum_factor = 1
    sol = ints[0]
    for i in range(len(sorted_mods) - 1):
        sum_factor *= mods[i]
        while (sol % mods[i + 1]) != ints[i + 1]:
            sol += sum_factor
    return sol


if __name__ == "__main__":
    mods = [5, 11, 17]
    ints = [2, 3, 5]
    print(sieving_ctr(mods, ints))
