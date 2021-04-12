# Создать массив из 1000 элементов и рандомно заполнить его числами от -1000 до 1000.
# Найти среднее арифметическое всех элементов.
# Создать другой массив и записать в него все элементы, которые на +- 20 % отличаются от среднего
from random import randint

N = 1000


def create_array():
    original_array = [randint(-1000, 1000) for i in range(N)]
    return original_array


def find_average(array):
    average = sum(array) / N
    return average


def create_final_array(array, average):
    final_array = [i for i in array if (average*0.8) <= i <= (average*1.2)]
    return final_array


if __name__ == "__main__":
    print("Начальный массив: ")
    first_array = create_array()
    print(first_array)
    print("Среднее арифметическое: ")
    average = find_average(first_array)
    print(average)
    print("Среднее арифметическое +- 20%: ")
    print(average*1.2, average*0.8)
    print("Финальный массив: ")
    second_array = create_final_array(first_array, average)
    print(second_array)
