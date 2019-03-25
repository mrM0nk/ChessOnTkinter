from tkinter import Tk, Canvas, BOTH
from PIL import ImageTk, Image
import time


окно = None
холст = None


def инициализация_интерфейса():
    def создание_окна():
        global окно
        окно = Tk()
        ekranX = (окно.winfo_screenwidth())
        ekranY = (окно.winfo_screenheight())
        # ekranX = 1366
        # ekranY = 768
        окно.config(width=ekranX * 9 // 10, height=ekranY * 9 // 10, background="#CFFBA8")
        окно.title("Working Tkinter")
        окно.geometry("{}x{}+{}+{}".format(ekranX * 9 // 10, ekranY * 9 // 10, ekranX // 30, 0))
        окно.resizable(0, 0)

    def отрисовка_холста():
        global холст
        ekranX = (окно.winfo_screenwidth())
        ekranY = (окно.winfo_screenheight())
        холст = Canvas(width=ekranX * 9 // 10, height=ekranY * 9 // 10)
        холст.pack(fill=BOTH, expand=True)
        фон = Image.open('images\image2.jpg')
        фон.thumbnail((ekranX, ekranY), Image.ANTIALIAS)
        холст.image = ImageTk.PhotoImage(фон)
        холст.create_image(0, 0, image=холст.image, anchor='nw')

    def ориентация_экрана():
        ekranX = (окно.winfo_screenwidth())
        ekranY = (окно.winfo_screenheight())
        if ekranY <= ekranX:
            переменная_ширины_экрана = ekranY * 9 // 10
        else:
            переменная_ширины_экрана = ekranX * 9 // 10
        return переменная_ширины_экрана

    def расчет_координат(переменная_ширины_экрана):
        ekranX = (окно.winfo_screenwidth())
        клетка = переменная_ширины_экрана // 11
        отступ_x = ekranX * 9 / 20 - клетка * 4
        отступ_y = клетка * 3 // 2
        return отступ_x, отступ_y, клетка

    создание_окна()
    отрисовка_холста()
    переменная_ширины_экрана = ориентация_экрана()
    отступ_x, отступ_y, клетка = расчет_координат(переменная_ширины_экрана)
    return отступ_x, отступ_y, клетка


def импорт_изображений(клетка):
    фигуры = {}
    pilImage = Image.open("images\ПешкаЧ.png")
    pilImage.thumbnail((клетка, клетка), Image.ANTIALIAS)
    ПешкаЧ = ImageTk.PhotoImage(pilImage)
    фигуры['ПешкаЧ'] = ПешкаЧ
    pilImage = Image.open("images\ПешкаБ.png")
    pilImage.thumbnail((клетка, клетка), Image.ANTIALIAS)
    ПешкаБ = ImageTk.PhotoImage(pilImage)
    фигуры['ПешкаБ'] = ПешкаБ
    pilImage = Image.open("images\ЛадьяЧ.png")
    pilImage.thumbnail((клетка, клетка), Image.ANTIALIAS)
    ЛадьяЧ = ImageTk.PhotoImage(pilImage)
    фигуры['ЛадьяЧ'] = ЛадьяЧ
    pilImage = Image.open("images\ЛадьяБ.png")
    pilImage.thumbnail((клетка, клетка), Image.ANTIALIAS)
    ЛадьяБ = ImageTk.PhotoImage(pilImage)
    фигуры['ЛадьяБ'] = ЛадьяБ
    pilImage = Image.open("images\КоньЧ.png")
    pilImage.thumbnail((клетка, клетка), Image.ANTIALIAS)
    КоньЧ = ImageTk.PhotoImage(pilImage)
    фигуры['КоньЧ'] = КоньЧ
    pilImage = Image.open("images\КоньБ.png")
    pilImage.thumbnail((клетка, клетка), Image.ANTIALIAS)
    КоньБ = ImageTk.PhotoImage(pilImage)
    фигуры['КоньБ'] = КоньБ
    pilImage = Image.open("images\СлонЧ.png")
    pilImage.thumbnail((клетка, клетка), Image.ANTIALIAS)
    СлонЧ = ImageTk.PhotoImage(pilImage)
    фигуры['СлонЧ'] = СлонЧ
    pilImage = Image.open("images\СлонБ.png")
    pilImage.thumbnail((клетка, клетка), Image.ANTIALIAS)
    СлонБ = ImageTk.PhotoImage(pilImage)
    фигуры['СлонБ'] = СлонБ
    pilImage = Image.open("images\ФерзьЧ.png")
    pilImage.thumbnail((клетка, клетка), Image.ANTIALIAS)
    ФерзьЧ = ImageTk.PhotoImage(pilImage)
    фигуры['ФерзьЧ'] = ФерзьЧ
    pilImage = Image.open("images\ФерзьБ.png")
    pilImage.thumbnail((клетка, клетка), Image.ANTIALIAS)
    ФерзьБ = ImageTk.PhotoImage(pilImage)
    фигуры['ФерзьБ'] = ФерзьБ
    pilImage = Image.open("images\КорольЧ.png")
    pilImage.thumbnail((клетка, клетка), Image.ANTIALIAS)
    КорольЧ = ImageTk.PhotoImage(pilImage)
    фигуры['КорольЧ'] = КорольЧ
    pilImage = Image.open("images\КорольБ.png")
    pilImage.thumbnail((клетка, клетка), Image.ANTIALIAS)
    КорольБ = ImageTk.PhotoImage(pilImage)
    фигуры['КорольБ'] = КорольБ
    return фигуры


def отрисовка_доски(отступ_x, отступ_y, клетка):
    def отрисовка_полотна_доски(отступ_x, отступ_y, клетка):
        холст.update()
        time.sleep(1)
        холст.create_rectangle(отступ_x - клетка * 3 // 4, отступ_y - клетка * 3 // 4,
                               отступ_x + клетка * 8 + клетка * 3 // 4, отступ_y + клетка * 8 + клетка * 3 // 4,
                               fill="#C9862F")
        холст.create_line(отступ_x - клетка * 3 // 4, отступ_y + клетка * 3 // 4 + клетка * 8, отступ_x,
                          отступ_y + клетка * 8, width=2, fill="#6F1203")
        холст.create_line(отступ_x - клетка * 3 // 4, отступ_y - клетка * 3 // 4, отступ_x, отступ_y, width=2,
                          fill="#6F1203")
        холст.create_line(отступ_x + клетка * 8, отступ_y, отступ_x + клетка * 3 // 4 + клетка * 8,
                          отступ_y - клетка * 3 // 4, width=2, fill="#6F1203")
        холст.create_line(отступ_x + клетка * 8, отступ_y + клетка * 8, отступ_x + клетка * 3 // 4 + клетка * 8,
                          отступ_y + клетка * 3 // 4 + клетка * 8, width=2, fill="#6F1203")
        холст.create_rectangle(отступ_x - клетка * 3 // 4, отступ_y - клетка * 3 // 4,
                               отступ_x + клетка * 8 + клетка * 3 // 4, отступ_y + клетка * 8 + клетка * 3 // 4,
                               width=5, outline="#770E89")
        холст.create_rectangle(отступ_x, отступ_y, отступ_x + клетка * 8, отступ_y + клетка * 8, width=7)

    def отрисовка_клеток(отступ_x, отступ_y, клетка):
        for y in range(8):
            for x in range(8):
                if (x + y) % 2 == 0:
                    холст.create_rectangle(отступ_x + x * клетка, отступ_y + y * клетка, отступ_x + x * клетка + клетка,
                                           отступ_y + y * клетка + клетка, fill="#C9862F")
                else:
                    холст.create_rectangle(отступ_x + x * клетка, отступ_y + y * клетка, отступ_x + x * клетка + клетка,
                                           отступ_y + y * клетка + клетка, fill="#6F1203")

    def отрисовка_координат(отступ_x, отступ_y, клетка):
        ListY = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        iy = - 1
        for x in range(0, 8):
            iy = iy + 1
            холст.create_text(отступ_x + клетка * 2 // 4 + клетка * x, отступ_y + клетка * 8 + клетка * 1 // 4,
                              text=ListY[iy], fill="black")
        k_podpisX = 9
        for y in range(0, 8):
            k_podpisX = k_podpisX - 1
            холст.create_text(отступ_x - клетка * 1 // 4, отступ_y + клетка * y + клетка * 2 // 4, text=k_podpisX,
                              fill="black")

    отрисовка_полотна_доски(отступ_x, отступ_y, клетка)
    отрисовка_клеток(отступ_x, отступ_y, клетка)
    отрисовка_координат(отступ_x, отступ_y, клетка)


def отрисовка_шахмат(отступ_x, отступ_y, клетка):
    холст.update()
    time.sleep(1)

    def отрисовка_черных_шахмат(отступ_x, отступ_y, клетка):
        List = ('ЛадьяЧ', 'КоньЧ', 'СлонЧ', 'ФерзьЧ', 'КорольЧ', 'СлонЧ', 'КоньЧ', 'ЛадьяЧ')
        b = 0
        for x in range(8):
            imagesprite = холст.create_image(отступ_x + x * клетка + клетка // 2, отступ_y + клетка * 3 // 2,
                                             image=фигуры.get('ПешкаЧ'))
            time.sleep(1 / 6)
            холст.update()
        for i in range(len(List)):
            imagesprite = холст.create_image(отступ_x + клетка // 2 + клетка * b, отступ_y + клетка // 2,
                                             image=фигуры.get(List[b]))
            time.sleep(1 / 4)
            холст.update()
            b = b + 1

    def отрисовка_белых_шахмат(отступ_x, отступ_y, клетка):
        List = ('ЛадьяБ', 'КоньБ', 'СлонБ', 'ФерзьБ', 'КорольБ', 'СлонБ', 'КоньБ', 'ЛадьяБ')
        b = 0
        for x in range(8):
            imagesprite = холст.create_image(отступ_x + x * клетка + клетка // 2, отступ_y + 6 * клетка + клетка // 2,
                                             image=фигуры.get('ПешкаБ'))
            time.sleep(1 / 6)
            холст.update()
        for i in range(len(List)):
            imagesprite = холст.create_image(отступ_x + клетка // 2 + клетка * b, отступ_y + клетка * 15 // 2,
                                             image=фигуры.get(List[b]))
            time.sleep(1 / 4)
            холст.update()
            b = b + 1

    отрисовка_черных_шахмат(отступ_x, отступ_y, клетка)
    отрисовка_белых_шахмат(отступ_x, отступ_y, клетка)


def свободные_клетки(координата_x, координата_y, фигура):
    коорд_свободных_клеток = []

    if фигура == 'КоньБ' or фигура == 'КоньЧ':
        List = [(-1, 2), (1, 2), (-2, 1), (2, 1), (-2, -1), (2, -1), (-1, -2), (1, -2)]
        for i in range(len(List)):
            x, y = List[i]
            x = координата_x + x
            y = координата_y + y
            if 0 < x < 9 and 0 < y < 9:
                клеточка = x, y
                коорд_свободных_клеток.append(клеточка)

    elif фигура == 'КорольБ' or фигура == 'КорольЧ':
        List = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(len(List)):
            x, y = List[i]
            x = координата_x + x
            y = координата_y + y
            if 0 < x < 9 and 0 < y < 9:
                клеточка = x, y
                коорд_свободных_клеток.append(клеточка)

    elif фигура == 'ЛадьяБ' or фигура == 'ЛадьяЧ':
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

    elif фигура == 'СлонБ' or фигура == 'СлонЧ':
        for yi in range(-8, 9):
            for xi in range(-8, 9):
                if abs(xi) == abs(yi) and xi != 0 and yi != 0:
                    x = координата_x + xi
                    y = координата_y + yi
                    if 0 < x < 9 and 0 < y < 9:
                        клеточка = x, y
                        коорд_свободных_клеток.append(клеточка)

    elif фигура == 'ФерзьБ' or фигура == 'ФерзьЧ':
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

    elif фигура == 'ПешкаЧ' or фигура == 'ПешкаБ':
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


def подсветить_клетки(коорд_свободных_клеток, отступ_x, отступ_y, клетка):
    for i in range(len(коорд_свободных_клеток)):
        x, y = коорд_свободных_клеток[i]
        холст.create_rectangle(отступ_x + x * клетка - клетка, отступ_y - y * клетка + клетка * 8,
                               отступ_x + x * клетка, отступ_y - y * клетка + клетка * 9, fill="#E1C191")


def нарисовать_фигуру(отступ_x, отступ_y, клетка, фигуры, координата_x, координата_y, фигура):
    холст.create_image(отступ_x - клетка // 2 + клетка * координата_x,
                       отступ_y + клетка * 8 - клетка * координата_y + клетка // 2, image=фигуры.get(фигура))


def задача_коня(старт_x, старт_y, финиш_х, финиш_у):
    стартовая_точка = (старт_x, старт_y)
    финишная_точка = (финиш_х, финиш_у)
    Карта_точек = {}
    Карта_точек[стартовая_точка] = None
    новые_точки = [стартовая_точка]
    for очередная_точка in новые_точки:
        for прирост_х, прирост_у in ((-1, 2), (1, 2), (-2, 1), (2, 1), (-2, -1), (2, -1), (-1, -2), (1, -2)):
            очередная_точка_x, очередная_точка_у = очередная_точка
            новая_точка_x = очередная_точка_x + прирост_х
            новая_точка_у = очередная_точка_у + прирост_у
            if 1 <= новая_точка_x <= 8 and 1 <= новая_точка_у <= 8 and (
                    новая_точка_x, новая_точка_у) not in Карта_точек:
                Карта_точек[(новая_точка_x, новая_точка_у)] = очередная_точка
                новые_точки.append((новая_точка_x, новая_точка_у))
        if финишная_точка in Карта_точек:
            предпоследння_точка = финишная_точка
            короткий_путь = [предпоследння_точка]
            while Карта_точек[предпоследння_точка]:
                предпоследння_точка = Карта_точек[предпоследння_точка]
                короткий_путь.append(предпоследння_точка)
            короткий_путь.reverse()
            return короткий_путь


def get_mouse():
    time.sleep(1 / 8)
    холст.update()
    time.sleep(7)
    getxx = окно.winfo_pointerx() - окно.winfo_rootx()
    getyy = окно.winfo_pointery() - окно.winfo_rooty()
    if отступ_x <= getxx <= (отступ_x + клетка): x_мыши = 1
    if (отступ_y + клетка * 7) <= getyy <= (отступ_y + клетка * 8): y_мыши = 1
    if (отступ_x + клетка) <= getxx <= (отступ_x + клетка * 2): x_мыши = 2
    if (отступ_y + клетка * 6) <= getyy <= (отступ_y + клетка * 7): y_мыши = 2
    if (отступ_x + клетка * 2) <= getxx <= (отступ_x + клетка * 3): x_мыши = 3
    if (отступ_y + клетка * 5) <= getyy <= (отступ_y + клетка * 6): y_мыши = 3
    if (отступ_x + клетка * 3) <= getxx <= (отступ_x + клетка * 4): x_мыши = 4
    if (отступ_y + клетка * 4) <= getyy <= (отступ_y + клетка * 5): y_мыши = 4
    if (отступ_x + клетка * 4) <= getxx <= (отступ_x + клетка * 5): x_мыши = 5
    if (отступ_y + клетка * 3) <= getyy <= (отступ_y + клетка * 4): y_мыши = 5
    if (отступ_x + клетка * 5) <= getxx <= (отступ_x + клетка * 6): x_мыши = 6
    if (отступ_y + клетка * 2) <= getyy <= (отступ_y + клетка * 3): y_мыши = 6
    if (отступ_x + клетка * 6) <= getxx <= (отступ_x + клетка * 7): x_мыши = 7
    if (отступ_y + клетка * 1) <= getyy <= (отступ_y + клетка * 2): y_мыши = 7
    if (отступ_x + клетка * 7) <= getxx <= (отступ_x + клетка * 8): x_мыши = 8
    if (отступ_y) <= getyy <= (отступ_y + клетка): y_мыши = 8
    time.sleep(1 / 2)
    return x_мыши, y_мыши


def перемести_фигуру(фигуры):
    x, y = короткий_путь[0]
    time.sleep(1 / 2)
    холст.update()
    холст.create_rectangle(отступ_x + x * клетка - клетка, отступ_y - y * клетка + клетка * 8, отступ_x + x * клетка,
                           отступ_y - y * клетка + клетка * 9, fill="#E1C191", tags="Квадрат")
    time.sleep(1 / 2)
    холст.update()
    холст.create_image(отступ_x - клетка // 2 + клетка * x, отступ_y + клетка * 8 - клетка * y + клетка // 2,
                       image=фигуры.get('КоньБ'), tags="Конь")
    time.sleep(1 / 2)
    холст.update()
    for i in range(len(короткий_путь)):
        if i == 0:
            x_предыдущая, y_предыдущая = короткий_путь[i]
        else:
            x_предыдущая, y_предыдущая = короткий_путь[i - 1]
        x_точки, y_точки = короткий_путь[i]
        x_прирост = (x_точки - x_предыдущая)
        y_прирост = (y_точки - y_предыдущая)
        холст.move("Квадрат", x_прирост * клетка, -y_прирост * клетка)
        time.sleep(1 / 2)
        холст.update()
        if abs(x_прирост) > abs(y_прирост):
            for ix in range(abs(x_прирост)):
                холст.move("Конь", клетка * ((x_прирост) / abs(x_прирост)), 0)
                time.sleep(1 / 4)
                холст.update()
            for iy in range(abs(y_прирост)):
                холст.move("Конь", 0, - клетка * ((y_прирост) / abs(y_прирост)))
                time.sleep(1 / 4)
                холст.update()
        else:
            for iy in range(abs(y_прирост)):
                холст.move("Конь", 0, - клетка * ((y_прирост) / abs(y_прирост)))
                time.sleep(1 / 4)
                холст.update()
            for ix in range(abs(x_прирост)):
                холст.move("Конь", клетка * ((x_прирост) / abs(x_прирост)), 0)
                time.sleep(1 / 4)
                холст.update()


def ввод_координат_коню():
    холст.create_text(отступ_x + клетка * 4, отступ_y - клетка // 2.2, font=("Purisa", клетка // 3),
                      text="Наведите мышкой на стартовую клетку", fill="green")
    x_мыши, y_мыши = get_mouse()
    старт_x = x_мыши
    старт_y = y_мыши
    холст.create_rectangle(отступ_x + старт_x * клетка - клетка, отступ_y - старт_y * клетка + клетка * 8,
                           отступ_x + старт_x * клетка, отступ_y - старт_y * клетка + клетка * 9, width=5,
                           outline="green")
    холст.create_text(отступ_x + клетка * 4, отступ_y + клетка * 17 // 2, font=("Purisa", клетка // 3),
                      text="Наведите мышкой на финишную клетку", fill="red")
    x_мыши, y_мыши = get_mouse()
    финиш_х = x_мыши
    финиш_у = y_мыши
    холст.create_rectangle(отступ_x + финиш_х * клетка - клетка, отступ_y - финиш_у * клетка + клетка * 8,
                           отступ_x + финиш_х * клетка, отступ_y - финиш_у * клетка + клетка * 9, width=5,
                           outline="red")
    return старт_x, старт_y, финиш_х, финиш_у


отступ_x, отступ_y, клетка = инициализация_интерфейса()
фигуры = импорт_изображений(клетка)
отрисовка_доски(отступ_x, отступ_y, клетка)
отрисовка_шахмат(отступ_x, отступ_y, клетка)
'''##нарисовать_фигуру (отступ_x, отступ_y, клетка, фигуры, координата_x, координата_y, фигура)
##x_мыши, y_мыши = get_mouse()'''

# подсветить клетки возможных ходов по заданной фигуре
# координата_x = int(input('Введите координату X: '))
# координата_y = int(input('Введите координату Y: '))
# фигура = input('Введите фигуру: ')
# холст.create_image(отступ_x - клетка // 2 + клетка * координата_x, отступ_y + клетка * 8 - клетка * координата_y + клетка // 2, image=фигуры.get(фигура))
# коорд_свободных_клеток = свободные_клетки(координата_x, координата_y, фигура)
# подсветить_клетки (коорд_свободных_клеток, отступ_x, отступ_y, клетка)

# Задача пройти конем из точки А в точку Б
#старт_x, старт_y, финиш_х, финиш_у = ввод_координат_коню()
#короткий_путь = задача_коня(старт_x, старт_y, финиш_х, финиш_у)
#перемести_фигуру(фигуры)
окно.mainloop()