"""
Primes

We have the following input list of numbers, some of them are prime. You need to create a utility function that takes as input a number and returns a bool, whether it is prime or not.

Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent implementations for filtering NUMBERS.

Compare the results and performance of each of them.

"""

import multiprocessing
import concurrent.futures


NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]


def print_numb(numb):
    print(numb, check_for_prime(numb))


def check_for_prime(numb):

    if numb < 2:
        return False

    if numb in {2, 3}:
        return True

    if numb % 2 != 0:
        for i in range(3, numb // 2, 2):
            if numb % i == 0:
                return False
        return True
    return False

    #  multithreading

# with concurrent.futures.ThreadPoolExecutor() as thread_executer:
#     thread_executer.map(print_numb, NUMBERS)

    # multiprocessing
if __name__ == '__main__':

    with concurrent.futures.ProcessPoolExecutor() as p_exec:
        p_exec.map(print_numb, NUMBERS)
