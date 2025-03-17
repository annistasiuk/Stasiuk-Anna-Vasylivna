def fibonacci_seq_generat():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_seq_generat()

print("Перші 10 чисел Фібоначчі:")
for _ in range(10):
    print(next(fib_gen), end=' ')