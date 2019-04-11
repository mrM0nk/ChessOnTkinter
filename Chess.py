import gui, ПодсветитьКлетки, КоньAtoB, обход_доски


def btn_click(event):
    try:
        gui.кнопка_старт.unbind('<Button-1>')
        принятая_задача = gui.принятая_задача.get()

        if принятая_задача == "Очистить_поле":
            gui.очистка_доски()
            gui.сброс_старт_финиш()

        if принятая_задача == "Отрисовать_шахматы":
            gui.очистка_доски()
            gui.отрисовка_шахмат()
            gui.сброс_старт_финиш()

        if принятая_задача == "Подсветить_клетки":
            gui.очистка_доски()
            gui.нарисовать_фигуру(gui.старт_x, gui.старт_y, gui.выбор_фигуры())
            коорд_свободных_клеток = ПодсветитьКлетки.свободные_клетки(gui.старт_x, gui.старт_y, gui.выбор_фигуры())
            gui.подсветить_клетки(коорд_свободных_клеток)

        if принятая_задача == "Переместить_коня":
            gui.очистка_доски()
            короткий_путь = КоньAtoB.задача_коня(gui.старт_x, gui.старт_y, gui.финиш_х, gui.финиш_у)
            gui.перемести_фигуру(короткий_путь, gui.выбор_фигуры(), номера_ходов=True)

        if принятая_задача == "Обойти_доску":
            gui.очистка_доски()
            пройденные_клетки = обход_доски.обход_доски(gui.старт_x, gui.старт_y)
            gui.перемести_фигуру(пройденные_клетки, gui.выбор_фигуры(), номера_ходов=True)

    except:
        pass

    try:
        gui.кнопка_старт.bind('<Button-1>', btn_click)

    except:
        pass


if __name__ == "__main__":
    gui.инициализация_интерфейса(info_panel=True, ask_for_change_settings=False)
    gui.отрисовка_доски()

    gui.окно.bind('<Button-3>', gui.позиция)
    gui.кнопка_старт.bind('<Button-1>', btn_click)

    gui.окно.mainloop()