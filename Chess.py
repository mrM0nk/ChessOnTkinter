import gui


def btn_click(event):
    try:
        gui.кнопка_расчитать.unbind('<Button-1>')
        gui.очистка_доски()

        gui.отрисовка_шахмат()

        gui.кнопка_расчитать.bind('<Button-1>', btn_click)

    except:
        pass


if __name__ == "__main__":
    gui.инициализация_интерфейса(info_panel=True, ask_for_change_settings=False)
    gui.отрисовка_доски()

    gui.кнопка_расчитать.bind('<Button-1>', btn_click)

    gui.окно.mainloop()