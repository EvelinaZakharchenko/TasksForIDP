# Сгенерировать массив из задачи b. Найти 2 максимальных элемента данного массива.
# Элементы не должны быть равны. Пример: [998, 998, 997, 999, 999].
# Результат = 998, 999
# Написать тесты для проверки этого кода

from random import randint

N = 1000


def create_array():
    original_array = [randint(-1000, 1000) for i in range(N)]
    return original_array


def find_max1(array):
    max1 = -1001
    for i in array:
        if i > max1:
            max1 = i
    return max1


def find_max2(array, max1):
    max2 = -1001
    for i in array:
        if max2 < i < max1:
            max2 = i
    if max2 == -1001:  # for case, when all numbers equal - will return two equal numbers, not clear requirements
        max2 = max1
    return max2


if __name__ == "__main__":
    print("Начальный массив: ")
    first_array = create_array()
    print(first_array)
    max1 = find_max1(first_array)
    max2 = find_max2(first_array, max1)
    print("Результат = ", max1, ", ", max2, sep='')

