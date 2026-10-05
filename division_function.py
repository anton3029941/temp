from math import sqrt

def division_function(number):
    prime_divs = {}
    while True:
        divisor = 2
        while divisor <= int(sqrt(number)):
            print(number, divisor)
            if number % divisor == 0:
                if not divisor in prime_divs:
                    prime_divs[divisor] = 2
                else:
                    prime_divs[divisor] += 1
                number //= divisor
                break

            divisor += 1

        if divisor > sqrt(number):
            prime_divs[number] = 2
            break

    prime_factorisation = 1
    for prime_exponent in prime_divs.values():
        prime_factorisation *= prime_exponent

    return prime_factorisation, prime_divs.items()

def find_divisors(number):
    pass

print(division_function(int(input())))