import gui, КоньAtoB


def свободные_ходы(старт_х_у, теоретически_возможные_движения): #перебор ходов для фигруры
    варианты_ходов = теоретически_возможные_движения # список возможных ходов
    список_возможных_ходов=[]  # Список возможных ходов после проверки
    for прирост in варианты_ходов:
        новый_х = старт_х_у[0] + прирост[0]
        новый_у = старт_х_у[1] + прирост[1]
        if 0 < новый_х < 9:
            if 0 < новый_у < 9:
                список_возможных_ходов.append((новый_х,новый_у))
    return список_возможных_ходов


def обход_доски( старт_x, старт_y, type_figure = 1):
    старт_х_у = (старт_x, старт_y)
    пройденные_клетки = [старт_х_у]
    список_возможных_ходов = []   # инфа каждого хода, для возврата назад
    теоретически_возможные_движения = КоньAtoB.get_figure_movements(gui.выбор_фигуры())
    первый_ход = свободные_ходы(старт_х_у, теоретически_возможные_движения) # Делаем превый ход
    список_возможных_ходов.append(первый_ход)   # Делаем превый ход, добовляется список возможных ходов из первой клетки
    flag_found_way = False
    i = 0 #счетчик хода/волны
    while not flag_found_way:
        if len(пройденные_клетки) == 63:
            пройденные_клетки.append(список_возможных_ходов[-1][0])
            break
        новые_списки = [] # Список для выбора след хода по правилу, массив массивов возможных ходов, под индексом 0
        # хранится массив в котором под последним индексом хранится клетка в какую можно походить, остальный - свободные клетки
        for клетка in список_возможных_ходов[i]: # клетка -- tuple из списка возможных ходов предыдущей клетки
            свободные_ходы_клетки = свободные_ходы(клетка, теоретически_возможные_движения) # для каждой такой клетки узнаем возможные ходы
            свободные_ходы_клетки = [ w for w in свободные_ходы_клетки if w not in пройденные_клетки] # теперь нужно их проверить
            if len(свободные_ходы_клетки)!= 0:
                свободные_ходы_клетки.append(клетка) # клетка в списке на последнем месте !!!
                новые_списки.append(свободные_ходы_клетки)
        if len(новые_списки) == 0:
            список_возможных_ходов.pop(i)
            пройденные_клетки.pop()
            i -= 1
            continue
        длинна_списка = len(новые_списки[0])          # Вычисляем короткий список
        лучший_список = новые_списки[0]
        for подсписок in новые_списки:
            if len(подсписок) < длинна_списка:
                длинна_списка = len(подсписок)
                лучший_список = подсписок
        выбранная_клетка = лучший_список
        список_возможных_ходов[i].remove(выбранная_клетка[-1]) # удаляем выбраную клетку из возможных для предыдущего хода, на случ возврата)
        пройденные_клетки.append(выбранная_клетка[-1])
        выбранная_клетка.pop()
        список_возможных_ходов.append(выбранная_клетка)
        i += 1
    return пройденные_клетки

