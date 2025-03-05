import time

def timer_wrapper(func):
    def wrapper(n):
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

def prime_generator():
    num = 2
    while True:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
        num += 1

@timer_wrapper
def prime_num_getter(n):
    primes = []
    gen = prime_generator()
    for _ in range(n):
        primes.append(next(gen))
    print(primes)
    return primes

prime_num_getter(10)