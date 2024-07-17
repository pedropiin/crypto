import primefac

def solve():
    n = 510143758735509025530880200653196460532653147
    factors = list(primefac.primefac(n))
    if factors[0] > factors[1]:
        smallest = factors[1]
    else:
        smallest = factors[0]
    
    print(smallest)

if __name__ == '__main__':
    solve()