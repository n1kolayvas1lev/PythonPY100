if __name__ == "__main__":
    # постарайтесь не использовать "магические" числа,
    # а по возможности дать переменным осмысленные названия и использовать их
    # TODO Распечатать строку лесенкой
    a = 'Hello, World'
    for i1, i2 in enumerate(a):
        print(((' ') * i1), i2)