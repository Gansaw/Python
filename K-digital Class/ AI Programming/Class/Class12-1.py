from multiprocessing import Pool
import time


def work(x):
    for _ in range(10):
        y = x ** 2    

# def work(x):
#     print(x)

if __name__ == "__main__":
    pool = Pool(4)
    data = range(1, 10000)
    t0 = time.time_ns()
    pool.map(work, data)
    t1 = time.time_ns()

    print(f"Time:{t1-t0} (ns)")