from functools import reduce
import time

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def decorator1(func):
    def dec():
        start_time = time.time()
        func(numbers)
        print(time.time() - start_time, "seconds")
    return dec()


@decorator1
def calc_value(n):
    numbers1 = list(filter(lambda a: a % 2 == 0, n))
    numbers2 = map(lambda a: a * a, numbers1)
    numbers3 = reduce(lambda a, b: a + b, list(numbers2)) / len(list(numbers1))
    return numbers3


value = calc_value(numbers)
print(f"Середнє значення: {value}")
