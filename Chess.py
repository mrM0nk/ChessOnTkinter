import gui


def btn_click(event):
    try:
        gui.кнопка_старт.unbind('<Button-1>')
        gui.очистка_доски()
        gui.отрисовка_шахмат()

    except:
        pass

    try:
        gui.кнопка_старт.bind('<Button-1>', btn_click)

    except:
        pass


def btn_click_1(event):
    try:
        gui.кнопка_очистки.unbind('<Button-1>')
        gui.очистка_доски()

    except:
        pass

    try:
        gui.кнопка_очистки.bind('<Button-1>', btn_click_1)

    except:
        pass


if __name__ == "__main__":
    gui.инициализация_интерфейса(info_panel=True, ask_for_change_settings=False)
    gui.отрисовка_доски()

    gui.кнопка_старт.bind('<Button-1>', btn_click)
    gui.кнопка_очистки.bind('<Button-1>', btn_click_1)

    gui.окно.mainloop()