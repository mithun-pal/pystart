from math import sqrt


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        #print(f'value of number in get_primes func is {number}')
        number += 1


def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for current in range(3, int(sqrt(num))+1, 2):
            if num % current == 0:
                return False
        return True
    return False


def solve_number_10():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return


if __name__ == '__main__':
    # primes = get_primes(2009173)
    # for prime in primes:
    #     print(prime)
    solve_number_10()


