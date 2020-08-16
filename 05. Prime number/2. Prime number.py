a = int(input())

def prime_not_prime(n):
    if n == 1:
        return 'not prime'
    for i in range(2,n):
        if n % i == 0:
            return 'not prime'
    else:
        return 'prime'

if a > 0:
    print(prime_not_prime(a))

