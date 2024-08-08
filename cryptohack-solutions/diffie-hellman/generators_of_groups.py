"""
There are more clever ways to do this, such as only testing powers to 
combinations of factors of (p - 1), but it would require lots of coding
when brute-force works perfectly for this small case.
The idea of the brute-force approach is to just calculate all powers of 
all numbers in the group. If the algorithm never finds a repeated 
result for a potential generator, it means that it is a primitive element.
"""
def solve():
    p = 28151

    generators = []
    for g in range(1, p):
        print(f"--- analising g = {g} ---")
        powers = set()
        for x in range(1, p):
            print(f"currently in power x = {x}")
            e = pow(g, x, p)
            if e in powers:
                break
            powers.add(e)
        
        if len(powers) == (p - 1):
            generators.append(g)
            break

    print(generators)


if __name__ == '__main__':
    solve()