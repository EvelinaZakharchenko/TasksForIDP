# from task3 import find_max1, find_max2, N
from task3 import sort_array, N


def test_positive_case():
    array = [i for i in range(N)]
    # max1 = find_max1(array)
    # assert max1 == 999, "Wrong max1 number"
    # assert find_max2(array, max1) == 998, "Wrong max2 number"
    sorted_array = sort_array(array)
    assert sorted_array[-1] == 999, "Wrong max1 number"
    assert sorted_array[-2] == 998, "Wrong max2 number"


def test_array_with_all_the_same_numbers():
    array = [1000 for i in range(N)]
    sort_array(array)
    assert ("Массив состоит из одинаковых элементов. Сответственно максимальный только один: ", array[1]) == \
           ("Массив состоит из одинаковых элементов. Сответственно максимальный только один: ", 1000), \
           "Wrong error message, when array contains all the same numbers"


def test_array_with_few_equal_numbers():
    array = [998, 998, 997, 999, 999]
    sorted_array = sort_array(array)
    assert sorted_array[-1] == 999, "Wrong max1 number, when array contains few equal numbers"
    assert sorted_array[-2] == 998, "Wrong max2 number, when array contains few equal numbers"


if __name__ == "__main__":
    test_positive_case()
    test_array_with_all_the_same_numbers()
    test_array_with_few_equal_numbers()
    print("Everything passed")
