from functools import lru_cache
import time


def time_of_function(func):
    def wrapper():
        start_time = time.time()
        result = func()
        execution_time = round(time.time() - start_time, 3)
        print(f'Время выполнения: {execution_time} сек.')
        return result
    return wrapper

# После первого запуска программы раскомментируйте декоратор @lru_cache:
# результаты выполнения функции expensive_computation() закешируются;
# при втором и третьем вызовах выполнение функции будет почти мгновенным.
@time_of_function
@lru_cache
def expensive_computation():
    sequence = [1]
    for item in range(5000):
        sequence.append(sum(sequence))
    return sequence[10]


print(expensive_computation())

print(expensive_computation())

print(expensive_computation())