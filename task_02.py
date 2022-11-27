#### TASK 02 ####
# Создайте функцию, возвращающую список со всеми простыми числами от 0 до 1000.
# Используя механизм декораторов посчитайте сколько секунд, потребовалось для вычисления всех простых чисел.
# Отобразите на экран количество секунд и простые числа.

# Добавьте к первому заданию возможность передавать границы диапазона для поиска всех простых чисел.

import time


ADD_TO_END_RANGE = 1
START_RANGE = 0
END_RANGE = 1000

simple_numbers = []


def timeCounter(func):
    def counter(start_range=START_RANGE, end_range=END_RANGE):
        start_time = time.time()
        func(start_range, end_range)
        end_time = time.time()
        print(f"Processing time: {end_time - start_time} seconds")
    return counter


@timeCounter
def getSimpleNumbers(start_range=START_RANGE, end_range=END_RANGE):
    for number in range(start_range, end_range + ADD_TO_END_RANGE):
        counter = 0
        divider = 2
        while divider < number:
            if number % divider == 0:
                counter += 1
            divider += 1

        if counter == 0 and number > 1:
            simple_numbers.append(number)
    print(f"List of simple numbers in range {start_range} - {end_range}:\n{simple_numbers}")


getSimpleNumbers(1, 10)


