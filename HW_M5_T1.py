def caching_fibanacci(n):
    # Створюємо пустий словник
    cache = {}
    def fibonacci(n):
        # Робимо перевірку чи дорівнює введене значення 0 та менше 0
        if n <= 0:
            return 0
        # Робимо перевірку чи дорівнює введене значення 1
        elif n == 1:
            return 1
        # Робимо перевірку чи введене значення є у кеші
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibanacci(1)

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))
print(fib(15))
