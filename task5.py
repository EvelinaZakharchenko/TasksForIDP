# Написать функцию check_my_date, принимающую число месяц и год.
# Вернуть True, если такая дата существует и False иначе.
# Объяснить выбор решения. Написать тесты на свой код
# Note! This task still has no tests.

def check_leep_year(year):
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False

def check_my_date(day, month, year):
    try:
        int(day)
        int(month)
        int(year)
    except:
        raise Exception('Date must be a string')

    month_day = {
        1: 31,
        2: 29 if check_leep_year(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    # print(check_leep_year(year))
    # print(month_day[2])
    if year <= 0:
        return False
    if 12 < month or month <= 0:
        return False
    if 0 >= day or day > month_day[month]:
        return False
    return True

if __name__ == "__main__":
    # day = int(input())
    # month = int(input())
    # year = int(input())
    print(check_my_date(28, 2, 2021))




