wind = int(input())

# TODO напишите с помощью if-elif-else условие проверки скорости ветра
if 0 <= wind <= 4:
    print('Weak')
elif 5 <= wind <=10:
    print('Moderate')
elif 11 <=  wind <= 18:
    print('Strong')
else:
    print('Hurricane')