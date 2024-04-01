"""
Practice asynchronous code

Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number.
Schedule the execution of this code using asyncio.gather for a list of integers from 1 to 10.
You need to get four lists of results from corresponding functions.

Rewrite the code to use simple functions to get the same results but using a multiprocessing library.
Time the execution of both realizations, explore the results, what realization is more effective, why did you get a result like this.
"""
import asyncio
import multiprocessing
from time import time


def measure_time(func):
    def inner():
        t0 = time()
        func()
        print(time() - t0)
    return inner


async def fibonacci(numb: int) -> str:

    if numb in {0, 1}:
        result = [0]
    else:
        count = 2
        n1 = 0
        n2 = 1
        result = [n1, n2]
        while count < numb:
            n1, n2 = n2, n1 + n2
            result.append(n2)
            count += 1
    return f"fibonacci: {result}"


async def factorial(numb: int) -> int:
    if numb < 2:
        result = 1

    elif numb == 2:
        result = 2

    else:
        result = numb * await factorial(numb - 1)

    return result


async def square(numb: int) -> str:
    return f"square {numb ** 2}"


async def cubic(numb: int) -> str:
    return f"cubic: {numb ** 3}"


async def main():
    results = []
    async with asyncio.TaskGroup() as tg:
        tasks = []
        for n in range(1, 11):
            # tasks.append(tg.create_task(fibonacci(n)))
            # tasks.append(tg.create_task(factorial(n)))
            # tasks.append(tg.create_task(square(n)))
            # tasks.append(tg.create_task(cubic(n)))
            t1 = asyncio.create_task(fibonacci(n))
            t2 = asyncio.create_task(factorial(n))
            t3 = asyncio.create_task(square(n))
            t4 = asyncio.create_task(cubic(n))

            result = await asyncio.gather(t1, t2, t3, t4)
            results.append(result)

        for i in results:
            print(i)

####################################################################
def fibonacci2(numb: int) -> str:

    if numb in {0, 1}:
        result = [0]
    else:
        count = 2
        n1 = 0
        n2 = 1
        result = [n1, n2]
        while count < numb:
            n1, n2 = n2, n1 + n2
            result.append(n2)
            count += 1
    return f"fibonacci: {result}"


def factorial2(numb: int) -> int:
    if numb < 2:
        result = 1

    elif numb == 2:
        result = 2

    else:
        result = numb * factorial2(numb - 1)

    return result


def square2(numb: int) -> str:
    return f"square {numb ** 2}"


def cubic2(numb: int) -> str:
    return f"cubic: {numb ** 3}"


def main2(numb, q: multiprocessing.Queue):
    result = []
    for f in (fibonacci2, factorial2, square2, cubic2):
        result.append(f(numb))

    q.put(result)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main())
    print(time() - t0)

####################################################################
    t0 = time()
    q = multiprocessing.Queue()
    processes = []
    for n in range(1, 11):
        processes.append(multiprocessing.Process(target=main2, args=(n, q)))

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    while not q.empty():
        print(q.get())

    print(time() - t0)
