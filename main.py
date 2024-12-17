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
    return 2000*X_win - 900*o1 + 20*x1 + 10*x2 - 10*o2 + 5*x3

def minimax_O(X_win, O_win, x1, x2, x3, o1, o2, o3):
    return 2000*O_win - 900*x1 + 20*o1 - 10*x2 + 10*o2 + 5*o3


def print_field(field):
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
func_numbs = [[0 for i in range(count)] for j in range(count)]


test_func_numbs = [[-1e5 for i in range(3)] for j in range(3)]


hod_count = 1
for i in range(9):
    if bool_X:
        print(f'Номер хода: {hod_count}. Крестики')
    else:
        print(f'Номер хода: {hod_count}. Нолики')

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
            else:
                test_func_numbs[i][j] = '-'



    maximum, indices = find_first_max_index_in_2d_list(test_func_numbs)
    if bool_X:
        field[indices[0]][indices[1]] = 'X'
    else:
        field[indices[0]][indices[1]] = 'O'


    print_field(field)
    print('\n')
    print_field(test_func_numbs)
    print('\n\n')
    hod_count += 1
    bool_X = not bool_X

