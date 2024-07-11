# *************************************************************
# Python Multiprocessing
# *************************************************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

start_time = time.perf_counter()
def counter(num):
    count = 0
    while count < num:
        count += 1

def main(start):
    cores = cpu_count()
    count_to_goal = 1000000000
    print("\nYou have", cores, "cores, counting to", count_to_goal)
    counter(count_to_goal)
    print("\tIt took", str(time.perf_counter() - start), "with a single core")
    start = time.perf_counter()
    processes = []
    for i in range(cores):  # only create as many processes as you have cpu_count
        # creating more than this is a time hindrance due to creation and deletion and potentially worse proportions
        processes.append(Process(target=counter, args=((count_to_goal/cores),)))
        # add a comma to a single element to denote ^ as tuple assignment rather than equation
    for i in processes:
        i.start()
    for i in processes:
        i.join()
    print("\tIt took", str(time.perf_counter() - start), "using", cores, "cores")


if __name__ == "__main__":  # now if we're imported, this functionality won't run
    main(start_time)
