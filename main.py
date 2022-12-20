# Создаём строки поля
L1 = ['-', '-', '-']
L2 = ['-', '-', '-']
L3 = ['-', '-', '-']


# Функция отрисовки поля
def table(x1, x2, x3):
    return print("  1 2 3\n"
                 + "1 " + x1[0] + " " + x1[1] + " " + x1[2] + "\n"
                 + "2 " + x2[0] + " " + x2[1] + " " + x2[2] + "\n"
                 + "3 " + x3[0] + " " + x3[1] + " " + x3[2])


# Функция проверки победителя по линии
def chek_line(x1, x2, x3):
    return (x1[0] == x1[1] and x1[1] == x1[2] and (x1[0] != "-") or
            x2[0] == x2[1] and x2[1] == x2[2] and (x2[0] != "-") or
            x3[0] == x3[1] and x3[1] == x3[2] and (x3[0] != "-"))


# Функция проверки победителя по столбцу
def chek_column(x1, x2, x3):
    return (x1[0] == x2[0] and x1[0] == x3[0] and (x1[0] != "-") or
            x1[1] == x2[1] and x1[1] == x3[1] and (x1[1] != "-") or
            x1[2] == x2[2] and x1[2] == x3[2] and (x1[2] != "-"))


# Функция проверки победителя по диагонали
def chek_diagonal(x1, x2, x3):
    return (x1[0] == x2[1] and x1[0] == x3[2] and (x1[0] != "-") or
            x1[2] == x2[1] and x1[2] == x3[0] and (x1[2] != "-"))


# Функция проверки победителя по всем вариантам
def logics(x1, x2, x3):
    return chek_line(x1, x2, x3) or chek_column(x1, x2, x3) or chek_diagonal(x1, x2, x3)


# Функция выбора линии ввода
def choice_line(x):
    if x == 1:
        return L1
    elif x == 2:
        return L2
    elif x == 3:
        return L3


# Функция ввода позиции игрока
def player_input(symbol):
    while True:
        player_value = input("Введите через пробел строку и колонку, куда хотите поставить: " + symbol + "\n")
        if len(player_value) != 3:
            print("Ошибка!")
            continue
        if not ((player_value[0] in "123") and (player_value[2] in "123")):
            print("Ошибка!")
            continue
        line = int(player_value[0])
        column = int(player_value[2])
        if str(choice_line(line)[column - 1]) in "XO":
            print("Занято")
            table(L1, L2, L3)
            continue
        choice_line(line)[column - 1] = symbol
        break


# Функция логики игры
def game():
    step = 0
    while True:
        table(L1, L2, L3)
        if step % 2 == 0:
            player_input("X")
        else:
            player_input("O")
        if logics(L1, L2, L3):
            print("Победа!")
            table(L1, L2, L3)
            break
        step += 1
        if step > 8:
            table(L1, L2, L3)
            print("Ничья")


game()
