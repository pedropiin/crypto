from sympy import isprime


"""
We've got a sequence of consecutive powers as
x^n (mod p) = 588
x^n+1 (mod p) = 665
x^n+2 (mod p) = 216
...
...
such that we can rearrange them as
558 * x = 665 (mod p)
216 * x = 216 (mod p)
...
...

So the only thing we need to do is test all primes between 100 and 999
(the exercise gives us that p is a 3-digit number) that satisfy these equations
with the same x.
"""
def solve():
    powers = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
    for p in range(100, 1000):
        if isprime(p):
            x = (powers[1] * pow(powers[0], p - 2, p)) % p
            valid_count = 0
            for i in range(2, len(powers)):
                new_x = (powers[i] * pow(powers[i-1], p - 2, p)) % p
                if new_x != x:
                    break
                valid_count += 1
            if valid_count == len(powers) - 2:
                print("The value of p is: ", p)
                print("The value of x is: ", x)
                break


if __name__ == '__main__':
    solve()