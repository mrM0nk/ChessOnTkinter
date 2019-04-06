import guiChess


if __name__ == '__main__':
    guiChess.инициализация_интерфейса(info_panel = True)

    guiChess.отрисовка_шахмат()


    guiChess.окно.mainloop()