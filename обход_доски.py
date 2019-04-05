import guiChess


def свободные_ходы(xy_start): #перебор ходов для фигруры
    xy_end = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)) # список возможных ходов
    moves=[]  # Список возможных ходов после проверки
    for xy in xy_end:
        new_x = xy_start[0] + xy[0]
        new_y = xy_start[1] + xy[1]
        if new_x > 0 and new_x < 9:
            if new_y > 0 and new_y < 9:
                moves.append((new_x,new_y))
    return moves


def way_figure( x_start, y_start, type_figure = 1): # Пытается решить задачу коня
    xy_start = (x_start, y_start)
    reached_cells = [xy_start] #пройденые клетки
    list_moves = []   # инфа каждого хода, для возврата назад
    first_move = свободные_ходы(xy_start) # Делаем превый ход
    list_moves.append(first_move)   # Делаем превый ход, добовляется список возможных ходов из первой клетки
    flag_found_way = False
    i = 0 #счетчик хода/волны
    while not flag_found_way:
        if len(reached_cells) == 63:
            reached_cells.append(list_moves[-1][0])
            break
        new_list = [] # Список для выбора след хода по правилу
        for cell in list_moves[i]: # cell -- tuple из списка возможных ходов предыдущей клетки
            ways = свободные_ходы(cell) # для каждой такой клетки узнаем возможные ходы
            ways = [ w for w in ways if w not in reached_cells] # теперь нужно их проверить
            if len(ways)!= 0:
                ways.append(cell) # Сell в списке на последнем месте !!!
                new_list.append(ways)
        if len(new_list) == 0:
            list_moves.pop(i)
            reached_cells.pop()
            i -=1
            continue
        L = len(new_list[0])          # Вычисляем короткий список
        best_list = new_list[0]       # Вычисляем короткий список
        for sub_list in new_list:     # Вычисляем короткий список
            if len(sub_list) < L:     # Вычисляем короткий список
                L = len(sub_list)     # Вычисляем короткий список
                best_list = sub_list  # Вычисляем короткий список
        new_cell = best_list          # Вычисляем короткий список
        list_moves[i].remove(new_cell[-1]) # удаляем выбраную клетку из возможных для предыдущего хода, на случ возврата)
        reached_cells.append(new_cell[-1])
        new_cell.pop()
        list_moves.append(new_cell)
        i +=1

    return reached_cells


if __name__ == '__main__':
    guiChess.инициализация_интерфейса()
    координата_x = int(input('Введите координату X: '))
    координата_y = int(input('Введите координату Y: '))
    reached_cells = way_figure(координата_x, координата_y)
    guiChess.перемести_фигуру__по_доске(reached_cells)

    guiChess.окно.mainloop()






