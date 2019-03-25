import guiChess


if __name__ == '__main__':
    guiChess.инициализация_интерфейса()
    guiChess.импорт_изображений()
    guiChess.отрисовка_доски()

    guiChess.отрисовка_шахмат()

    guiChess.окно.mainloop()