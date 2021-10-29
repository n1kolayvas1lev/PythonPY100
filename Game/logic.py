EMPTY_CELL = '_'

def init_field(size = 3): #размер поля 3х3
    #empty_cell = '_' заполняем таблицу некими символами
    field = [[EMPTY_CELL for i in range(size)] for j in range(size)] #генерация матрицы 3х3
    return field

def get_cell(field: list, row_index: int, col_index: int):
    return field[row_index][col_index]

def set_cell(field: list, row_index: int, col_index: int, symbol) -> None:
    field[row_index][col_index] = symbol

def is_win(field) -> bool: # обычно функции is возвращают bool
    win_conditions = [
        [(1, 1), (1, 2), (1, 3)],
        [(2, 1), (2, 2), (2, 3)],
        [(3, 1), (3, 2), (3, 3)],

        [(1, 1), (2, 1), (3, 1)],
        [(1, 2), (2, 2), (3, 2)],
        [(1, 3), (2, 3), (3, 3)],

        [(1, 1), (2, 2), (3, 3)],
        [(1, 3), (2, 2), (3, 1)]
    ]

    for win_comb in win_conditions:
        cell_1 = get_cell(field, row_index = win_comb[0][0] - 1, col_index = win_comb[0][1] - 1)
        cell_2 = get_cell(field, row_index = win_comb[1][0] - 1, col_index = win_comb[1][1] - 1)
        cell_3 = get_cell(field, row_index = win_comb[2][0] - 1, col_index = win_comb[2][1] - 1)
        if cell_1 == cell_2 == cell_3 != EMPTY_CELL:
            return True
        else:
            return False

def is_available_cell(field) -> bool: # проверка на доступность клеток для хода с возвратом да/нет
    for row in field:
        for cell in row:
            if cell == EMPTY_CELL:
                return True
    return False
def is_empty_cell(field: list, x: int, y: int) -> bool: #определяем занята ли клетка
    cell = field[x][y]
    # if cell == EMPTY_CELL:
    #     return  True
    # else:
    #     return False
    return True if cell == EMPTY_CELL else False