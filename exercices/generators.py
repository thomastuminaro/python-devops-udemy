import time

def load_data_eager(count, delay=0.1):
    result = []
    for i in range(count):
        time.sleep(delay)
        result.append(f"Data item {i}.")
    return result

def load_data_lazy(count, delay=0.1):
    for i in range(count):
        time.sleep(delay)
        yield(f"Data item {i}.")

if __name__ == "__main__":
    t0 = time.time() # gets current time of execution
    data = load_data_eager(5)
    t1 = time.time() # to check time after our function is called
    print(f"Eager : returned {data} in {t1-t0:.2f}s") # to round up to 2 decimals 

    data_lazy = load_data_eager(5)
    t2 = time.time()
    for d in data_lazy:
        print(d)
    t3 = time.time()
    print(f"Eager : returned {data} in {t3-t2:.5f}s")
