if __name__ == "__main__":
    listN = [int(i) for i in input()]
    print('Получить список цифр числа N', listN)
    print('Найти сумму всех цифр', sum(listN))
    listN_4 = [int(i) for i in listN if i % 2 == 0]
    print('Найти сумму всех четных чисел', listN_4)
    print('Найти количество цифр', len(listN))
    print('Найти максимальную цифру числа', max(listN), 'Найти минимальную цифру числа',  min(listN))
    d = len(listN)
    print('Получить список всех цифр стоящих на нечетных местах.', listN[1::2])
    print('Получить список всех цифр стоящих на четных местах.', listN[::2])
    print('Найти разность первой и последней цифры', listN[0] - listN[-1])
    b = []
    for i in range(d):
        if listN[i] == min(listN):
            b.append(i + 1)
    print('Найти минимальную цифру числа, и указать на каком месте она стоит', b)


