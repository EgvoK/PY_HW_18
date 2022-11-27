#### TASK 01 ####
# Создайте функцию, возвращающую список со всеми простыми числами от 0 до 1000.
# Используя механизм декораторов посчитайте сколько секунд, потребовалось для вычисления всех простых чисел.
# Отобразите на экран количество секунд и простые числа.

import time


simple_numbers = []


def timeCounter(func):
    def counter():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Processing time: {end_time - start_time} seconds")
    return counter()


@timeCounter
def getSimpleNumbers():
    for number in range(0, 1001):
        counter = 0
        divider = 2
        while divider < number:
            if number % divider == 0:
                counter += 1
            divider += 1

        if counter == 0 and number > 1:
            simple_numbers.append(number)
    print(f"List of simple numbers in range 0 - 1000:\n{simple_numbers}")


