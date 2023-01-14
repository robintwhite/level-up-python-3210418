""" write a python function to factor a number to it's prime numbers
input int: num
output list: prime_factors

for integers i from 1 to num 
if num is divisible by i and is an integer
add i to factor list
repeat on quotient
end when factor is 1 

example
num = 32
i = 2
32 / 2 = 16
factors = [2]
num = 16
i = 2
16 / 2 = 8
factors = [2,2]
num = 8
i = 2
8 / 2 = 4
factors = [2,2,2]
num = 4
4 / 2 = 2
factors = [2,2,2,2]
num = 2
i = 2
2 / 2 = 1
end
"""
import argparse


def factorize(num):
    for i in range(2, num + 1):
        new_num = num / i
        if new_num == int(new_num):
            return int(i), int(new_num)


def get_primes(num):
    factor = 2
    tmp_num = int(num)
    primes = []
    while tmp_num > 1:
        factor, tmp_num = factorize(tmp_num)
        primes.append(factor)
    if not primes:
        primes.append[int(num)]
    return primes


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num", help="number to find prime factors", type=int)
    args = parser.parse_args()
    primes = get_primes(num=args.num)
    print(primes)
