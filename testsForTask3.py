from task3 import find_max1, find_max2, N


def test_positive_case():
    array = [i for i in range(N)]
    max1 = find_max1(array)
    assert max1 == 999, "Wrong max1 number"
    assert find_max2(array, max1) == 998, "Wrong max2 number"


def test_array_with_all_the_same_numbers():
    array = [1000 for i in range(N)]
    max1 = find_max1(array)
    max2 = find_max2(array, max1)
    assert max1 == 1000, "Wrong max1 number, when array contains all the same numbers"
    assert max2 == 1000, "Wrong max2 number, when array contains all the same numbers"


def test_array_with_few_equal_numbers():
    array = [998, 998, 997, 999, 999]
    max1 = find_max1(array)
    max2 = find_max2(array, max1)
    assert max1 == 999, "Wrong max1 number, when array contains few equal numbers"
    assert max2 == 998, "Wrong max2 number, when array contains few equal numbers"


if __name__ == "__main__":
    test_positive_case()
    test_array_with_all_the_same_numbers()
    test_array_with_few_equal_numbers()
    print("Everything passed")