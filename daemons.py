# daemon thread =   a thread that runs in the background, not important for the program to run
#                   your program will not wait for daemon threads to complete before exiting
#                   non-daemon threads cannot normally be killed, live until task is complete

#                   ex. background tasks, garbage collection, waiting for input, long-running processes

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ",count,"seconds")


x = threading.Thread(target=timer, daemon=True)  # daemon = True so module doesn't wait to exit
# daemon methods are killed upon completion of main thread
# x.daemon = False  # daemon can be set later, but must be before start()
print(x.daemon)
x.start()

answer = input("Do you wish to exit?")
