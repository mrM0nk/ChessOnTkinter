import gui


if __name__ == '__main__':
    gui.инициализация_интерфейса(info_panel = True, ask_for_change_settings = True)

    gui.отрисовка_шахмат()

    gui.окно.mainloop()