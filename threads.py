# thread =  a separated flow of execution, like a river segment
#           threads run on different processors on your computer, however only 1 at a time in Python
#           each thread takes a turn running to achieve concurrency
#           GIL = (global interpreter lock)
#                   allows only one thread to hold the control
#                   of the Python interpreter at any one time

# cpu bound = program/task spends most of its time waiting for internal events (CPU intensive)
#           use multiprocessing
# io bound = program/task spends most of its time waiting for external events (user input, web browsing)
#           use multithreading
import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You've eaten breakfast")
def drink_coffee():
    time.sleep(4)  # <-- external
    print("You've drank coffee")

def study():
    time.sleep(5)
    print("You've studied")

x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()

x.join()  # main thread now needs to wait for this thread before it can continue
y.join()  # "", it's as if these calls combine the threads
z.join()  # ""

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())  # gives execution time of main thread (excludes runtime of any other threads)

# eat_breakfast()
# drink_coffee()
# study()