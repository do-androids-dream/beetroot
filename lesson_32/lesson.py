# import os
# import threading
#
# import requests
# from bs4 import BeautifulSoup
#
# lst = []
#
#
# def test(name):
#     for i in range(10):
#         print(f"{name}: {i}")
#         lst.append((name, i))
#     print(lst)
#
#
# def test2(name):
#     for i in range(10):
#         print(f"{name}: {i}")
#
#
# t1 = threading.Thread(target=test, args=("t1",))
# t2 = threading.Thread(target=test, args=("t2",))
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
# print(os.name)
# print(os.getcwd())
#
# import concurrent.futures
#
#
# counter = 0
#
#
# def increment_counter(fake_value):
#     global counter
#     for _ in range(100):
#         counter += 1


# if __name__ == "__main__":
    # """Race conditions are an entire class of subtle bugs that can and frequently do happen in multi-threaded code.
    # Race conditions happen because the programmer has not sufficiently protected data accesses to prevent threads from
    # interfering with each other. You need to take extra steps when writing threaded code to ensure things are thread-safe."""
    #
    # fake_data = [x for x in range(5000)]
    # counter = 0
    # with concurrent.futures.ThreadPoolExecutor(max_workers=5000) as executor:
    #     executor.map(increment_counter, fake_data)
    #
    # print(counter)


   ##########################################################################################################
    # import asyncio
    #
    #
    # async def say_hello(word):
    #     for i in range(2000000):
    #         print(f"Hello {word} {i}")
    #     await asyncio.sleep(3)  # Pause execution for `delay` seconds
    #     print(f"World {word}")
    #
    #
    # async def main():
    #     task1 = asyncio.create_task(say_hello(1))  # Create task for first call
    #     task2 = asyncio.create_task(say_hello(2))  # Create task for second call
    #     task3 = asyncio.create_task(say_hello(3))
    #     task4 = asyncio.create_task(say_hello(4))
    #     task5 = asyncio.create_task(say_hello(5))  # Create task for first call
    #     task6 = asyncio.create_task(say_hello(6))  # Create task for second call
    #     task7 = asyncio.create_task(say_hello(7))
    #     task8 = asyncio.create_task(say_hello(8))
    #     await asyncio.gather(task1, task2, task3, task4, task5, task6, task7, task8)  # Await both tasks concurrently
    #
    #
    # asyncio.run(main())  # Run the `main` coroutine function


import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.create_task(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")


   ###########################################################################################################

# import multiprocessing
#
# # empty list with global scope
# result = []
#
#
# def square_list(mylist):
#     """
#     function to square a given list
#     """
#     global result
#     # append squares of mylist to global list result
#     for num in mylist:
#         result.append(num * num)
#         # print global list result
#     print("Result(in process p1): {}".format(result))
#
#
# if __name__ == "__main__":
#     # input list
#     mylist = [1, 2, 3, 4]
#
#     # creating new process
#     p1 = multiprocessing.Process(target=square_list, args=(mylist,))
#     # starting process
#     p1.start()
#     # wait until process is finished
#     p1.join()
#
#     # print global result list
#     print("Result(in main program): {}".format(result))

# import multiprocessing
#
#
# def square_list(mylist, result, square_sum):
#     """
#     function to square a given list
#     """
#     # append squares of mylist to result array
#     for idx, num in enumerate(mylist):
#         result[idx] = num * num
#
#         # square_sum value
#     square_sum.value = sum(result)
#
#     # print result Array
#     print("Result(in process p1): {}".format(result[:]))
#
#     # print square_sum Value
#     print("Sum of squares(in process p1): {}".format(square_sum.value))
#
#
# if __name__ == "__main__":
#     # input list
#     mylist = [1, 2, 3, 4]
#
#     # creating Array of int data type with space for 4 integers
#     result = multiprocessing.Array('i', 4)
#
#     # creating Value of int data type
#     square_sum = multiprocessing.Value('i')
#
#     # creating new process
#     p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))
#
#     # starting process
#     p1.start()
#
#     # wait until the process is finished
#     p1.join()
#
#     # print result array
#     print("Result(in main program): {}".format(result[:]))
#
#     # print square_sum Value
#     print("Sum of squares(in main program): {}".format(square_sum.value))

# import multiprocessing
#
#
# def sender(conn, msgs):
#     """
#     function to send messages to other end of pipe
#     """
#     for msg in msgs:
#         conn.send(msg)
#         print("Sent the message: {}".format(msg))
#     conn.close()
#
#
# def receiver(conn):
#     """
#     function to print the messages received from other
#     end of pipe
#     """
#     while 1:
#         msg = conn.recv()
#         if msg == "END":
#             break
#         print("Received the message: {}".format(msg))
#
#
# if __name__ == "__main__":
#     # messages to be sent
#     msgs = ["hello", "hey", "hru?", "END"]
#
#     # creating a pipe
#     parent_conn, child_conn = multiprocessing.Pipe()
#
#     # creating new processes
#     p1 = multiprocessing.Process(target=sender, args=(parent_conn, msgs))
#     p2 = multiprocessing.Process(target=receiver, args=(child_conn,))
#
#     # running processes
#     p2.start()
#     p1.start()
#
#     # wait until processes finish
#     p1.join()
#     p2.join()


# # Python program to illustrate
# # the concept of locks
# # in multiprocessing
# import multiprocessing
#
#
# # function to withdraw from account
# def withdraw(balance, lock):
#     for _ in range(10000):
#         lock.acquire()
#         balance.value = balance.value - 1
#         lock.release()
#
#     # function to deposit to account
#
#
# def deposit(balance, lock):
#     for _ in range(10000):
#         lock.acquire()
#         balance.value = balance.value + 1
#         lock.release()
#
#
# def perform_transactions():
#     # initial balance (in shared memory)
#     balance = multiprocessing.Value('i', 100)
#
#     # creating a lock object
#     lock = multiprocessing.Lock()
#
#     # creating new processes
#     p1 = multiprocessing.Process(target=withdraw, args=(balance, lock))
#     p2 = multiprocessing.Process(target=deposit, args=(balance, lock))
#
#     # starting processes
#     p1.start()
#     p2.start()
#
#     # wait until processes are finished
#     p1.join()
#     p2.join()
#
#     # print final balance
#     print("Final balance = {}".format(balance.value))
#
#
# if __name__ == "__main__":
#     for _ in range(10):
#         # perform same transaction process 10 times
#         perform_transactions()


# Python program to understand
# the concept of pool
# import multiprocessing
# import os
# import time
#
#
# def square(n):
#     time.sleep(n)
#     print("Worker process id for {0}: {1}".format(n, os.getpid()))
#     return (n*n)
#
#
# if __name__ == "__main__":
#     # input list
#     mylist = [1,2,3,4,5]
#
#     # creating a pool object
#     p = multiprocessing.Pool()
#
#     # map list to target function
#     result = p.map(square, mylist)
#
#     print(result)


import requests
import multiprocessing
import time

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")