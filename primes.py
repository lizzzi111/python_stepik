def primes():
    def is_prime(n):
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return d * d > n
    a = 2
    while True:        
        if is_prime(a):
            yield a
        a += 1
f =  primes()
next(f)
