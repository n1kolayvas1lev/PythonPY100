from logic import init_field, is_empty_cell, set_cell, is_win, is_available_cell

def print_field(field: list) -> None:
    for row in field:
        for cell in row:
            print(cell, end=' ')
        print()

def get_step(player_symbol: str, field: list) -> tuple[int, int]:
    while True:
        step = input(f"Игрок {player_symbol} введите координату от 1 до 9:")
        if not step.isdigit():
            print('Вы ввели не число. Повторите ввод.')
            continue

        int_step = int(step)
        if not 1 <= int_step <= 9:
            print('Вы ввели неверный индекс.')
            continue

        field_size = 3
        x = int_step // field_size
        y = int_step % field_size
        if not is_empty_cell(field, x, y):
            print('Ячейка занята.')
            continue

        return x, y

def main():
    size_field = 3
    field = init_field()
    print_field(field)

    first_player, second_player = 'X', 'O'
    while True:
        row_index, col_index = get_step(first_player, field)
        set_cell(field, row_index, col_index, first_player)
        print_field(field)

        if is_win(field):
            print(f'Подебил игрок {first_player}')
            break

        if not is_available_cell(field):
            print('Ничья.')
            break

        row_index, col_index = get_step(second_player, field)
        set_cell(field, row_index, col_index, second_player)
        print_field(field)

        if is_win(field):
            print(f'Подебил игрок {second_player}')
            break

        if not is_available_cell(field):
            print('Ничья.')
            break

if __name__ == '__main__':
    main()
