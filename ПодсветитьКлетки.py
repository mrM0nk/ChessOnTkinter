import gui


def свободные_клетки(координата_x, координата_y, фигура):
    коорд_свободных_клеток = []

    if фигура == 'КоньБ' or фигура == 'КоньЧ':
        возможные_ходы = [(-1, 2), (1, 2), (-2, 1), (2, 1), (-2, -1), (2, -1), (-1, -2), (1, -2)]
        for i in range(len(возможные_ходы)):
            x, y = возможные_ходы[i]
            x = координата_x + x
            y = координата_y + y
            if 0 < x < 9 and 0 < y < 9:
                клеточка = x, y
                коорд_свободных_клеток.append(клеточка)

    if фигура == 'КорольБ' or фигура == 'КорольЧ':
        возможные_ходы = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(len(возможные_ходы)):
            x, y = возможные_ходы[i]
            x = координата_x + x
            y = координата_y + y
            if 0 < x < 9 and 0 < y < 9:
                клеточка = x, y
                коорд_свободных_клеток.append(клеточка)

    if фигура == 'ЛадьяБ' or фигура == 'ЛадьяЧ':
        for i in range(-8, 9):
            x = координата_x + i
            y = координата_y
            if 0 < x < 9 and 0 < y < 9 and x != координата_x:
                клеточка = x, y
                коорд_свободных_клеток.append(клеточка)
        for i in range(-8, 9):
            x = координата_x
            y = координата_y + i
            if 0 < x < 9 and 0 < y < 9 and y != координата_y:
                клеточка = x, y
                коорд_свободных_клеток.append(клеточка)

    if фигура == 'СлонБ' or фигура == 'СлонЧ':
        for yi in range(-8, 9):
            for xi in range(-8, 9):
                if abs(xi) == abs(yi) and xi != 0 and yi != 0:
                    x = координата_x + xi
                    y = координата_y + yi
                    if 0 < x < 9 and 0 < y < 9:
                        клеточка = x, y
                        коорд_свободных_клеток.append(клеточка)

    if фигура == 'ФерзьБ' or фигура == 'ФерзьЧ':
        for i in range(-8, 9):
            x = координата_x + i
            if 0 < x < 9 and x != координата_x:
                клеточка = x, координата_y
                коорд_свободных_клеток.append(клеточка)
        for i in range(-8, 9):
            y = координата_y + i
            if 0 < y < 9 and y != координата_y:
                клеточка = координата_x, y
                коорд_свободных_клеток.append(клеточка)
        for yi in range(-8, 9):
            for xi in range(-8, 9):
                if abs(xi) == abs(yi) and xi != 0 and yi != 0:
                    x = координата_x + xi
                    y = координата_y + yi
                    if 0 < x < 9 and 0 < y < 9:
                        клеточка = x, y
                        коорд_свободных_клеток.append(клеточка)

    if фигура == 'ПешкаЧ' or фигура == 'ПешкаБ':
        if фигура == 'ПешкаБ':
            List = [(0, 1), (0, 2)]
            for i in range(len(List)):
                x, y = List[i]
                x = координата_x + x
                y = координата_y + y
                if 0 < x < 9 and 0 < y < 9:
                    клеточка = x, y
                    коорд_свободных_клеток.append(клеточка)
        elif фигура == 'ПешкаЧ':
            List = [(0, -1), (0, -2)]
            for i in range(len(List)):
                x, y = List[i]
                x = координата_x + x
                y = координата_y + y
                if 0 < x < 9 and 0 < y < 9:
                    клеточка = x, y
                    коорд_свободных_клеток.append(клеточка)
    return коорд_свободных_клеток


if __name__ == '__main__':
    gui.инициализация_интерфейса(info_panel = True, ask_for_change_settings = False)
    if gui.язык_игры == 1:
        координата_x = int(input('Введите координату X: '))
        координата_y = int(input('Введите координату Y: '))
        фигура = input('Введите фигуру: ')
    else:
        координата_x = int(input('Enter the coordinate X: '))
        координата_y = int(input('Enter the coordinate Y: '))
        фигура = input('Enter a shape: ')
    gui.нарисовать_фигуру(координата_x, координата_y, фигура)
    коорд_свободных_клеток = свободные_клетки(координата_x, координата_y, фигура)
    gui.подсветить_клетки (коорд_свободных_клеток)


    gui.окно.mainloop()