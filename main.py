from itertools import chain


def analyze_tic_tac_toe(field, cur_x, cur_y):
    # Инициализация счетчиков
    O_win = 0
    X_win = 0
    x1 = 0
    x2 = 0
    x3 = 0

    o1 = 0
    o2 = 0
    o3 = 0

    # Функция для проверки выигрышных комбинаций
    def check_line(line):
        nonlocal O_win, X_win, x1, x2, o1, o2
        if line.count('X') == 3:
            X_win += 1
        elif line.count('O') == 3:
            O_win += 1
        elif line.count('X') == 2 and line.count('-') == 1:
            x1 += 1
        elif line.count('X') == 1 and line.count('-') == 2:
            x2 += 1
        elif line.count('O') == 2 and line.count('-') == 1:
            o1 += 1
        elif line.count('O') == 1 and line.count('-') == 2:
            o2 += 1

    # Проверка строк
    for row in field:
        check_line(row)

    # Проверка столбцов
    for col in range(3):
        check_line([field[row][col] for row in range(3)])

    # Проверка диагоналей
    check_line([field[i][i] for i in range(3)])  # Главная диагональ
    check_line([field[i][2 - i] for i in range(3)])  # Побочная диагональ



    if cur_x in [0, 2] and cur_y in [0, 2]:
        x3 = 3
        o3 = 0
    elif cur_x == 1 and cur_y == 1:
        x3 = 4
        o3 = 0
    else:
        x3 = 2
        o3 = 0

    if field[cur_x][cur_y] == 'O':
        x3, o3 = o3, x3


    return {
        "X_win": X_win,
        "O_win": O_win,
        "x1": x1,
        "x2": x2,
        "x3": x3,
        "o1": o1,
        "o2": o2,
        "o3": o3
    }


def minimax_X(X_win, O_win, x1, x2, x3, o1, o2, o3):
    return 10000*X_win - 3000*o1 + 20*x1 + 10*x2 - 10*o2 + 5*x3

def minimax_O(X_win, O_win, x1, x2, x3, o1, o2, o3):
    return 10000*O_win - 3000*x1 + 20*o1 - 10*x2 + 10*o2 + 5*o3


def print_field(field, k, krest):
    if k == 0:
        for i, row in enumerate(field):
            if krest[i//3][i%3] == '-':
                print(" ".join(f"{item:>7}" for item in row), f'\t{i//3}-{i%3}', '\tСумма =', sum([int(item) for item in row if item != '-']))  # Задаем ширину 4 для каждого
    else:
        for row in field:
            print(" ".join(f"{item:>4}" for item in row))  # Задаем ширину 4 для каждого

def find_first_max_index_in_2d_list(matrix):
    max_value = -1e7
    max_index = None  # Переменная для хранения индекса максимума

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value != '-' and value > max_value:
                max_value = value
                max_index = (i, j)  # Обновляем индекс максимума
                # Если нужно, можно сразу выйти из функции, если требуется только первый максимум
                # return max_value, max_index
    return max_value, max_index  # Возвращаем максимум и его индекс


# выигрышная комбинация для Х.
O_win = 0
# выигрышная комбинация для О.
X_win = 0

# количество строк, столбцов или диагоналей, где есть два крестика и одна пустая клетка.
x1 = 0
# количество строк, столбцов или диагоналей, где есть один крестик и две пустые клетки.
x2 = 0
# количество строк, столбцов или диагоналей, которые «бьет» поставленный на данном ходе крестик.
x3 = 0

# количество строк, столбцов или диагоналей, где есть два нолика и одна пустая клетка.
o1 = 0
# количество строк, столбцов или диагоналей, где есть один нолик и две пустые клетки.
o2 = 0
# количество строк, столбцов или диагоналей, которые «бьет» поставленный на данном ходе нолик.
o3 = 0


bool_X = True
field = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]



count = sum(1 for element in chain.from_iterable(field) if element == "-")
func_numbs = [['-' for i in range(count)] for i in range(count)]


test_func_numbs = [[-1e5 for i in range(3)] for j in range(3)]


hod_count = 1
for i in range(9):
    if bool_X:
        print(f'Номер хода: {hod_count}. Крестики')
    else:
        print(f'Номер хода: {hod_count}. Нолики')

    '''

    for i in range(3):
        for j in range(3):
            if field[i][j] == '-':
                cur_minimax = 0

                if bool_X:
                    field[i][j] = 'X'
                    params = analyze_tic_tac_toe(field, i, j)
                    cur_minimax = minimax_X(**params)
                    field[i][j] = '-'
                else:
                    field[i][j] = 'O'
                    params = analyze_tic_tac_toe(field, i, j)
                    cur_minimax = minimax_O(**params)
                    field[i][j] = '-'

                test_func_numbs[i][j] = cur_minimax
                print(params)
            else:
                test_func_numbs[i][j] = '-'

    '''
    if bool_X:
        for i in range(3):
            for j in range(3):
                if field[i][j] == '-':
                    x_minimax = 0
                    field[i][j] = 'X'
                    params_x = analyze_tic_tac_toe(field, i, j)
                    x_minimax = minimax_X(**params_x)

                    for i_o in range(3):
                        for j_o in range(3):
                            if field[i_o][j_o] == '-':
                                o_minimax = 0
                                field[i_o][j_o] = 'O'
                                params_o = analyze_tic_tac_toe(field, i, j)
                                o_minimax = minimax_O(**params_o)

                                func_numbs[i*3 + j][i_o*3 + j_o] = x_minimax - o_minimax
                                field[i_o][j_o] = '-'
                    field[i][j] = '-'
    else:
        for i in range(3):
            for j in range(3):
                if field[i][j] == '-':
                    o_minimax = 0
                    field[i][j] = 'O'
                    params_o = analyze_tic_tac_toe(field, i, j)
                    o_minimax = minimax_O(**params_o)

                    for i_o in range(3):
                        for j_o in range(3):
                            if field[i_o][j_o] == '-':
                                x_minimax = 0
                                field[i_o][j_o] = 'X'
                                params_x = analyze_tic_tac_toe(field, i, j)
                                x_minimax = minimax_X(**params_x)

                                func_numbs[i*3 + j][i_o*3 + j_o] = x_minimax - o_minimax
                                field[i_o][j_o] = '-'
                    field[i][j] = '-'


    print_field(func_numbs, 0, field)

    if bool_X:
        max_row = -1e6
        max_row_index = -1

        for i in range(len(func_numbs)):
            cur_row = 0
            for j in range(len(func_numbs)):
                if func_numbs[i][j] != '-':
                    cur_row += func_numbs[i][j]
            if max_row < cur_row and field[i // 3][i % 3] == '-':
                max_row = cur_row
                max_row_index = i
        field[max_row_index // 3][max_row_index % 3] = 'X'

    else:
        max_row = 1e6
        max_row_index = -1

        for i in range(len(func_numbs)):
            cur_row = 0
            for j in range(len(func_numbs)):
                if func_numbs[i][j] != '-':
                    cur_row += func_numbs[i][j]
            if max_row > cur_row and field[i // 3][i % 3] == '-':
                max_row = cur_row
                max_row_index = i
        field[max_row_index // 3][max_row_index % 3] = 'O'

    print('\n')
    print_field(field, 1, None)
    print('\n\n')
    hod_count += 1
    bool_X = not bool_X

