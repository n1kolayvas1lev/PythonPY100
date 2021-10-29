if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end=" ")
        print()
# Таблица умножения
matrix = [[i * j for i in range(1, 10) for j in range(1, 10)]]
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end=" ")
    print()
# вывод просто таблицы без создания объекта
    for row in range(1, 10):
        for col in range(1, 10):
            print(row * col, end=" ") # f- string print(f'{row * col:2}', end=" ")
        print()