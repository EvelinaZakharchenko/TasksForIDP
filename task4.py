# Найти кол-во счастливых билетов в 1 серии. Объяснить свое решение.


def get_lucky_tickets():
    counter = 0
    for i in range(1, 1000000):
        ticket = '{:0{}}'.format(i, 6)
        if sum(map(int, ticket[:3])) == sum(map(int, ticket[3:])):
            counter += 1
    return counter


if __name__ == "__main__":
    print("Количество счастливых билетов: ")
    counter = get_lucky_tickets()
    print(counter)
