def greet():
    print(" Добро пожаловать в крестики-нолики")
    print(" формат ввода: x и y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def ask():
    while True:
        cords = input("Ваш ход (введите x и y: через пробел): ").split()

        if len(cords) != 2:
            print("Кажется чего-то не хватает")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Разрешено писать только числа из поля")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Вы вышли за пределы, пожалуйста, повторите")
            continue

        if field[x][y] != " ":
            print("Клетка уже занята другим игроком")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Победил игрок X")
            return True
        if symbols == ["O", "O", "O"]:
            print("Победил игрок O")
            return True
    return False


greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print("Ходит игрок X")
    else:
        print("Ходит игрок O")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if check_win():
        break

    if count == 9:
        print(" Вам удалось сыграть в ничью")
        break