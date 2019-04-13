from tkinter import Tk, Canvas, BOTH, Frame, Label, Spinbox, Button, StringVar, Radiobutton
from math import ceil
from PIL import ImageTk, Image
import time
import random


окно = None
холст = None
холст1 = None
отступ_x = None
отступ_y = None
клетка = None
фигуры = None
язык_игры = "rus"
ширина_панели = 0
цветовая_схема = 2
цветовая_палитра_клеток = {1: ["#E8E8E8", "#B0B0B0"], 2: ["#C9862F", "#6F1203"], 3: ["#FFC4D7", "#6A7250"]}
палитра_подсветки = ["#F7C8F3", "#E1C191", "#E8E8E8"]
задержка_анимации = 1
кнопка_старт = None
список_фигур_белых = ("ФерзьБ", "КорольБ", "СлонБ", "КоньБ", "ЛадьяБ", "ПешкаБ")
список_фигур_черных = ("ФерзьЧ", "КорольЧ", "СлонЧ", "КоньЧ", "ЛадьяЧ", "ПешкаЧ")
цвет_шахмат_игрока = None
принятая_задача = None
выбранная_фигура = None
фон_игры1 = None
цвет_доски = None
старт_x = None
старт_y = None
финиш_х = None
финиш_у = None
фигура = None
ввод_текста = {"rus": {"текст_фона": "Выберите номер фона: 1. Природа, 2. Шахматы, 3. Космос: ",
                       "текст_цветовой_схемы": "Выберите цветовую схему доски: 1. Светлая, 2. Обычная, 3. Гламур: ",
                       "координаты_конюАБ": ("Наведите мышкой на стартовую клетку", "Наведите мышкой на финишную клетку"),
                       "координаты_подсветки": ("Введите координату X: ", "Введите координату Y: ", "Введите фигуру: ")},
               "en": {"текст_фона": "Select background number: 1. Nature, 2. Chess, 3. Space: ",
                      "текст_цветовой_схемы": "Choose board color scheme: 1. Light, 2. Ordinary, 3. Glamour: ",
                      "координаты_конюАБ": ("Mouse over the starting cell", "Mouse over the finish cell"),
                      "координаты_подсветки": ("Enter the coordinate X: ", "Enter the coordinate Y: ", "Enter a shape: ")}}


def инициализация_интерфейса(info_panel):

    def создание_окна():
        global окно
        окно = Tk()
        ekranX = (окно.winfo_screenwidth())
        ekranY = (окно.winfo_screenheight())
        окно.title("Chess")
        окно.geometry("{}x{}+{}+{}".format(ekranX * 9 // 10, ekranY * 9 // 10, (ekranX - (ekranX * 9 // 10)) // 2, 0))
        окно.resizable(0, 0)

    def отрисовка_холста(фон_игры, info_panel=False):
        global холст, ширина_панели, задержка_анимации, кнопка_старт, цвет_шахмат_игрока, принятая_задача, фигура,\
               фон_игры1, цвет_доски, холст1, выбранная_фигура
        ekranX = (окно.winfo_screenwidth())
        ekranY = (окно.winfo_screenheight())
        контейнер1 = Frame(master=окно)
        if not info_panel:
            контейнер1.place(x=0, y=0, width=ekranX * 9 // 10, height=ekranY * 9 // 10)
        if info_panel:
            ширина_панели = ekranX // 6.5
            контейнер1.place(x=0, y=0, width=ekranX * 9 // 10 - ширина_панели, height=ekranY * 9 // 10)
            контейнер2 = Frame(master=окно, background="#CFFBA8")
            контейнер2.place(x=ekranX * 9 // 10 - ширина_панели, y=0, width=ширина_панели, height=ekranY * 9 // 10)
            холст1 = Canvas(master=контейнер2, background="Black")
            холст1.pack(fill=BOTH, expand=True)
            фон1 = Image.open("background\image{}{}.jpg".format(фон_игры, фон_игры))
            фон1.thumbnail((ekranX, ekranY), Image.ANTIALIAS)
            холст1.image = ImageTk.PhotoImage(фон1)
            холст1.create_image((-ekranX * 9 // 10 - ширина_панели) // 2 + ширина_панели * 1.16, ekranY * 9 // 20,
                                image=холст1.image, anchor="center")

            шаг = ekranY // 27

            метка_величина_задержки = Label(master=контейнер2, text="Задержка, с:", foreground="blue",
                                            font="Arial {}".format(шаг // 3))
            метка_величина_задержки.place(x=ширина_панели // 2, y=шаг//1.9, anchor="center", height=шаг // 1.2)

            задержка_анимации = Spinbox(master=контейнер2, from_=0, to=1, increment=0.1)
            задержка_анимации.place(x=ширина_панели // 2, y=шаг * 1.1, width=ширина_панели * 3 // 4, anchor="center")

            кнопка_старт = Button(master=контейнер2, text="Старт", foreground="red", font="Arial {}".format(шаг // 3))
            кнопка_старт.place(x=ширина_панели // 2, y=шаг * 2.23, width=ширина_панели * 3 // 4, anchor="center")

            метка_цвет = Label(master=контейнер2, text="Цвет шахмат:", foreground="blue",
                               font="Arial {}".format(шаг // 3))
            метка_цвет.place(x=ширина_панели // 2, y=шаг * 3.4, anchor="center", height=шаг // 1.2)

            цвета = ["Белые", "Черные"]
            цвет_шахмат_игрока = StringVar()
            цвет_шахмат_игрока.set("Белые")

            for i, цвет in enumerate(цвета):
                b = Radiobutton(master=контейнер2, text=цвет, variable=цвет_шахмат_игрока, value=цвет, indicatoron=0,
                                font="Arial {}".format(шаг // 3))
                b.place(x=ширина_панели // 3 + i * ширина_панели // 3, y=шаг * 4.2, width=ширина_панели // 3,
                        height=шаг // 1.2, anchor="center")

            метка_задача = Label(master=контейнер2, text="Выбор задачи:", foreground="blue",
                                 font="Arial {}".format(шаг // 3))
            метка_задача.place(x=ширина_панели // 2, y=шаг * 5.2, anchor="center", height=шаг // 1.2)

            задачи = ["Очистить_поле", "Отрисовать_шахматы", "Подсветить_клетки", "Переместить_фигуру", "Обойти_доску"]
            принятая_задача = StringVar()
            принятая_задача.set("Отрисовать_шахматы")

            for i, задача in enumerate(задачи):
                b = Radiobutton(master=контейнер2, text=задача, variable=принятая_задача, value=задача, indicatoron=0,
                                font="Arial {}".format(шаг // 3))
                b.place(x=ширина_панели // 2, y=шаг // 1.2 * (7.3 + i), width=ширина_панели * 3 // 4, height=шаг // 1.2,
                        anchor="center")

            метка_фигуры = Label(master=контейнер2, text="Выбор фигуры:", foreground="blue",
                                 font="Arial {}".format(шаг // 3))
            метка_фигуры.place(x=ширина_панели // 2, y=шаг * 10.25, anchor="center", height=шаг // 1.2)

            список_фигур = ["Ферзь", "Король", "Слон", "Конь", "Ладья", "Пешка"]
            выбранная_фигура = StringVar()
            выбранная_фигура.set("Конь")

            for i, элемент in enumerate(список_фигур):
                b = Radiobutton(master=контейнер2, text=элемент, variable=выбранная_фигура, value=элемент,
                                indicatoron=0, font="Arial {}".format(шаг // 3))
                b.place(x=ширина_панели // 2, y=шаг // 1.2 * (13.4 + i), width=ширина_панели * 3 // 4,
                        height=шаг // 1.2, anchor="center")

            метка_фона = Label(master=контейнер2, text="Выбор фона:", foreground="blue",
                               font="Arial {}".format(шаг // 3))
            метка_фона.place(x=ширина_панели // 2, y=шаг * 16.15, anchor="center", height=шаг // 1.2)

            список_фонов = ["Природа", "Шахматы", "Космос"]
            фон_игры1 = StringVar()
            фон_игры1.set("Шахматы")

            for i, элемент_фона in enumerate(список_фонов):
                b = Radiobutton(master=контейнер2, text=элемент_фона, variable=фон_игры1, value=элемент_фона,
                                indicatoron=0, font="Arial {}".format(шаг // 3))
                b.place(x=ширина_панели // 2, y=шаг // 1.2 * (20.55 + i), width=ширина_панели * 3 // 4,
                        height=шаг // 1.2, anchor="center")

            метка_доски = Label(master=контейнер2, text="Выбор цвета доски:", foreground="blue",
                                font="Arial {}".format(шаг // 3))
            метка_доски.place(x=ширина_панели // 2, y=шаг * 19.55, anchor="center", height=шаг // 1.2)

            цвета_досок = ["Светлая", "Обычная", "Гламур"]
            цвет_доски = StringVar()
            цвет_доски.set("Обычная")

            for i, элемент_доски in enumerate(цвета_досок):
                b = Radiobutton(master=контейнер2, text=элемент_доски, variable=цвет_доски, value=элемент_доски,
                                indicatoron=0, font="Arial {}".format(шаг // 3))
                b.place(x=ширина_панели // 2, y=шаг // 1.2 * (24.7 + i), width=ширина_панели * 3 // 4,
                        height=шаг // 1.2, anchor="center")

            метка_координат_1 = Label(master=контейнер2, text="Стартовая клетка - нажмите ПКМ", foreground="red",
                                      font="Arial {}".format(шаг // 3))
            метка_координат_1.place(x=ширина_панели // 2, y=шаг * 23, anchor="center", height=шаг // 1.2,
                                    width=ширина_панели * 8 // 9)

            метка_координат_2 = Label(master=контейнер2, text="Финишная клетка - нажмите ЛКМ", foreground="blue",
                                      font="Arial {}".format(шаг // 3))
            метка_координат_2.place(x=ширина_панели // 2, y=шаг * 23.8, anchor="center", height=шаг // 1.2,
                                    width=ширина_панели * 8 // 9)

        холст = Canvas(master=контейнер1, background="Black")
        холст.pack(fill=BOTH, expand=True)
        фон = Image.open("background\image{}.jpg".format(фон_игры))
        фон.thumbnail((ekranX, ekranY), Image.ANTIALIAS)
        холст.image = ImageTk.PhotoImage(фон)
        холст.create_image((ekranX * 9 // 10 - ширина_панели)//2, ekranY * 9 // 20, image=холст.image, anchor="center")

    def ориентация_экрана():
        ekranX = (окно.winfo_screenwidth())
        ekranY = (окно.winfo_screenheight())
        if ekranY <= ekranX:
            переменная_ширины_экрана = ekranY * 9 // 10
        else:
            переменная_ширины_экрана = ekranX * 9 // 10
        return переменная_ширины_экрана

    def расчет_координат(переменная_ширины_экрана):
        global отступ_x, отступ_y, клетка
        ekranX = (окно.winfo_screenwidth())
        клетка = переменная_ширины_экрана // 11
        отступ_x = ekranX * 9 // 20 - клетка * 4 - ширина_панели // 2
        отступ_y = клетка * 3 // 2

    def импорт_изображений():
        global фигуры
        фигуры = {}
        список_фигур = список_фигур_черных + список_фигур_белых
        for фигура in список_фигур:
            pilImage = Image.open("images\{}.png".format(фигура))
            pilImage.thumbnail((клетка, клетка), Image.ANTIALIAS)
            фигуры["{}".format(фигура)] = ImageTk.PhotoImage(pilImage)

    фон_игры = 2
    создание_окна()
    отрисовка_холста(фон_игры, info_panel)
    переменная_ширины_экрана = ориентация_экрана()
    расчет_координат(переменная_ширины_экрана)
    импорт_изображений()


def номер_цвета_доски():
    if цвет_доски.get() == "Светлая":
        номер_цвета_доски = 1
    if цвет_доски.get() == "Обычная":
        номер_цвета_доски = 2
    if цвет_доски.get() == "Гламур":
        номер_цвета_доски = 3
    return номер_цвета_доски


def отрисовка_доски():
    светлый_оттенок, темный_оттенок = цветовая_палитра_клеток.get(номер_цвета_доски())

    def отрисовка_полотна_доски():
        холст.create_rectangle(отступ_x - клетка * 3 // 4, отступ_y - клетка * 3 // 4,
                               отступ_x + клетка * 8 + клетка * 3 // 4, отступ_y + клетка * 8 + клетка * 3 // 4,
                               fill=светлый_оттенок)
        холст.create_line(отступ_x - клетка * 3 // 4, отступ_y + клетка * 3 // 4 + клетка * 8, отступ_x,
                          отступ_y + клетка * 8, width=2, fill="#291F1E")
        холст.create_line(отступ_x - клетка * 3 // 4, отступ_y - клетка * 3 // 4, отступ_x, отступ_y, width=2,
                          fill="#291F1E")
        холст.create_line(отступ_x + клетка * 8, отступ_y, отступ_x + клетка * 3 // 4 + клетка * 8,
                          отступ_y - клетка * 3 // 4, width=2, fill="#291F1E")
        холст.create_line(отступ_x + клетка * 8, отступ_y + клетка * 8, отступ_x + клетка * 3 // 4 + клетка * 8,
                          отступ_y + клетка * 3 // 4 + клетка * 8, width=2, fill="#291F1E")
        холст.create_rectangle(отступ_x - клетка * 3 // 4, отступ_y - клетка * 3 // 4,
                               отступ_x + клетка * 8 + клетка * 3 // 4, отступ_y + клетка * 8 + клетка * 3 // 4,
                               width=5, outline="#770E89")
        холст.create_rectangle(отступ_x, отступ_y, отступ_x + клетка * 8, отступ_y + клетка * 8, width=7)

    def отрисовка_клеток():
        for y in range(8):
            for x in range(8):
                if (x + y) % 2 == 0:
                    холст.create_rectangle(отступ_x + x * клетка, отступ_y + y * клетка, отступ_x + x * клетка +
                                           клетка, отступ_y + y * клетка + клетка, fill=светлый_оттенок,
                                           tags="rect{}{}".format(x+1, y+1))
                else:
                    холст.create_rectangle(отступ_x + x * клетка, отступ_y + y * клетка, отступ_x + x * клетка +
                                           клетка, отступ_y + y * клетка + клетка, fill=темный_оттенок,
                                           tags="rect{}{}".format(x+1, y+1))

    def отрисовка_координат():
        координаты = ["A", "B", "C", "D", "E", "F", "G", "H"]
        ix = - 1
        for x in range(0, 8):
            ix += 1
            холст.create_text(отступ_x + клетка * 2 // 4 + клетка * x, отступ_y + клетка * 8 + клетка * 1 // 4,
                              text=координаты[ix], font="Arial {}".format(клетка // 6), fill="black")
        k_podpisY = 9
        for y in range(0, 8):
            k_podpisY = k_podpisY - 1
            холст.create_text(отступ_x - клетка * 1 // 4, отступ_y + клетка * y + клетка * 2 // 4, text=k_podpisY,
                              font="Arial {}".format(клетка // 6), fill="black")

    отрисовка_полотна_доски()
    отрисовка_клеток()
    отрисовка_координат()


def get_delay():

    try:
        задержка = задержка_анимации.get()

    except:
        задержка = 1

    return float(задержка)


def выбор_фигуры():

    try:
        фигура1 = выбранная_фигура.get()
        фигура2 = цвет_шахмат_игрока.get()[:1]
        фигура = "{}{}".format(фигура1, фигура2)
        return фигура

    except:
        pass


def очистка_доски():

    try:
        for элемент in холст.find_all():
            холст.delete(элемент)
        фон = Image.open("background\image{}.jpg".format(номер_фона()))
        фон.thumbnail((окно.winfo_screenwidth(), окно.winfo_screenheight()), Image.ANTIALIAS)
        холст.image = ImageTk.PhotoImage(фон)
        холст.create_image((окно.winfo_screenwidth() * 9 // 10 - ширина_панели)//2, окно.winfo_screenheight() * 9 // 20,
                           image=холст.image, anchor="center")
        отрисовка_доски()
        for элемент1 in холст1.find_all():
            холст1.delete(элемент1)
        фон1 = Image.open("background\image{}{}.jpg".format(номер_фона(), номер_фона()))
        фон1.thumbnail((окно.winfo_screenwidth(), окно.winfo_screenheight()), Image.ANTIALIAS)
        холст1.image = ImageTk.PhotoImage(фон1)
        холст1.create_image((-окно.winfo_screenwidth() * 9 // 10 - ширина_панели) // 2 + ширина_панели * 1.16,
                            окно.winfo_screenheight() * 9 // 20, image=холст1.image, anchor="center")

    except:
        pass


def сброс_старт_финиш():
    global старт_x, старт_y, финиш_х, финиш_у
    старт_x = None
    старт_y = None
    финиш_х = None
    финиш_у = None


def номер_фона():
    if фон_игры1.get() == "Природа":
        номер_фона = 1
    if фон_игры1.get() == "Шахматы":
        номер_фона = 2
    if фон_игры1.get() == "Космос":
        номер_фона = 3
    return номер_фона


def отрисовка_шахмат():
    окно.update_idletasks()
    окно.update()
    time.sleep(get_delay() * 2)

    try:
        def отрисовка_фигур(переменная):
            for i in range(0,2):
                for x in range(8):
                    холст.create_image(отступ_x + x * клетка + клетка // 2, отступ_y - переменная[2+i][0] *
                                       клетка + клетка * 17 // 2, image=фигуры.get(переменная[0+i][-1]),
                                       tags=переменная[0+i][-1] + "{}{}".format(x+1, переменная[2+i][0]))
                    time.sleep(get_delay() / 3)
                    окно.update()
                positions = (4, 3, 2, 0, 1, 2, 3, 4)
                for x in range(0, 8):
                    pos = positions[x]
                    холст.create_image(отступ_x + x * клетка + клетка // 2, отступ_y - переменная[2+i][1] *
                                       клетка + клетка * 17 // 2, image=фигуры.get(переменная[0+i][pos]),
                                       tags=переменная[0+i][pos] + "{}{}".format(x+1, переменная[2+i][1]))
                    time.sleep(get_delay() / 2)
                    окно.update_idletasks()
                    окно.update()

        if цвет_шахмат_игрока.get() == "Белые":
            переменная = (список_фигур_белых, список_фигур_черных, (2, 1), (7, 8))
            отрисовка_фигур(переменная)

        if цвет_шахмат_игрока.get() == "Черные":
            переменная = (список_фигур_черных, список_фигур_белых, (2, 1), (7, 8))
            отрисовка_фигур(переменная)
    except:
        pass


def подсветить_клетки(коорд_свободных_клеток):
    for i in range(len(коорд_свободных_клеток)):
        x, y = коорд_свободных_клеток[i]
        холст.create_rectangle(отступ_x + x * клетка - клетка, отступ_y - y * клетка + клетка * 8, отступ_x + x *
                               клетка, отступ_y - y * клетка + клетка * 9,
                               fill=палитра_подсветки[номер_цвета_доски()-1])
        окно.update()
        time.sleep(get_delay())
    сброс_старт_финиш()


def нарисовать_фигуру(координата_x, координата_y, фигура):
    холст.create_image(отступ_x - клетка // 2 + клетка * координата_x,
                       отступ_y + клетка * 8 - клетка * координата_y + клетка // 2, image=фигуры.get(фигура))


def позиция(event):

    try:
        def motion1(event):
            global финиш_х, финиш_у
            x, y = event.x, event.y
            ш_х = ceil((x - отступ_x) / клетка)
            ш_у = 9 - ceil((y - отступ_y) / клетка)
            if 0 < ш_х < 9 and 0 < ш_у < 9:
                финиш_х = ш_х
                финиш_у = ш_у
                холст.delete("rectBlue1")
                холст.create_rectangle(отступ_x + финиш_х * клетка - клетка, отступ_y - финиш_у * клетка + клетка * 8,
                                       отступ_x + финиш_х * клетка, отступ_y - финиш_у * клетка + клетка * 9,
                                       width=клетка // 11, outline="Blue", tags="rectBlue1")

        global старт_x, старт_y
        x, y = event.x, event.y
        ш_х1 = ceil((x - отступ_x) / клетка)
        ш_у1 = 9 - ceil((y - отступ_y) / клетка)
        if 0 < ш_х1 < 9 and 0 < ш_у1 < 9:
            старт_x = ш_х1
            старт_y = ш_у1
            очистка_доски()
            холст.create_rectangle(отступ_x + старт_x * клетка - клетка, отступ_y - старт_y * клетка + клетка * 8,
                                   отступ_x + старт_x * клетка, отступ_y - старт_y * клетка + клетка * 9,
                                   width=клетка // 11, outline="Red", tags="rectRed")
        окно.bind('<Button-1>', motion1)

    except:
        pass


def перемести_фигуру(короткий_путь, фигура="КоньБ", номера_ходов=False):

    try:
        def отрисовка_коня_х():
            for ix in range(abs(x_прирост)):
                холст.move("Конь", клетка * (x_прирост / abs(x_прирост)), 0)
                time.sleep(get_delay() / 2)
                окно.update()

        def отрисовка_коня_у():
            for iy in range(abs(y_прирост)):
                холст.move("Конь", 0, - клетка * (y_прирост / abs(y_прирост)))
                time.sleep(get_delay() / 2)
                окно.update()

        def отрисовка_фигуры():
            холст.move("Конь", клетка * x_прирост, - клетка * y_прирост)
            time.sleep(get_delay() / 2)
            окно.update()

        x, y = короткий_путь[0]
        холст.create_rectangle(отступ_x + старт_x * клетка - клетка, отступ_y - старт_y * клетка + клетка * 8,
                               отступ_x + старт_x * клетка, отступ_y - старт_y * клетка + клетка * 9,
                               width=клетка // 11, outline="Red", tags="rectRed1")
        холст.create_rectangle(отступ_x + финиш_х * клетка - клетка, отступ_y - финиш_у * клетка + клетка * 8,
                               отступ_x + финиш_х * клетка, отступ_y - финиш_у * клетка + клетка * 9,
                               width=клетка // 11, outline="Blue", tags="rectBlue1")
        time.sleep(get_delay())
        окно.update()
        холст.create_rectangle(отступ_x + x * клетка - клетка, отступ_y - y * клетка + клетка * 8, отступ_x + x *
                               клетка, отступ_y - y * клетка + клетка * 9,
                               fill=палитра_подсветки[номер_цвета_доски()-1], tags="Квадрат")
        time.sleep(get_delay())
        окно.update()
        холст.create_image(отступ_x - клетка // 2 + клетка * x, отступ_y + клетка * 8 - клетка * y + клетка // 2,
                           image=фигуры.get(фигура), tags="Конь")
        time.sleep(get_delay())
        окно.update()
        номер_хода = 1
        for i in range(len(короткий_путь)):
            x, y = короткий_путь[i]
            if i == 0:
                x_предыдущая, y_предыдущая = короткий_путь[i]
            else:
                x_предыдущая, y_предыдущая = короткий_путь[i - 1]
            x_точки, y_точки = короткий_путь[i]
            x_прирост = (x_точки - x_предыдущая)
            y_прирост = (y_точки - y_предыдущая)
            холст.move("Квадрат", x_прирост * клетка, - y_прирост * клетка)
            time.sleep(get_delay())
            окно.update()
            if фигура == "КоньБ" or фигура == "КоньЧ":
                if abs(x_прирост) > abs(y_прирост):
                    отрисовка_коня_х()
                    отрисовка_коня_у()
                else:
                    отрисовка_коня_у()
                    отрисовка_коня_х()
            else:
                отрисовка_фигуры()
            if номера_ходов:
                рандомный_цвет = '#' + ''.join([random.choice('0123456789abcdef') for i in range(6)])
                холст.create_text(отступ_x - клетка // 2 + клетка * x, отступ_y + клетка * 8 - клетка * y + клетка // 2,
                                  font=("Purisa", клетка // 3), text=номер_хода, fill=рандомный_цвет)
                time.sleep(get_delay() / 10)
                окно.update()
                номер_хода += 1
        сброс_старт_финиш()

    except:
        pass


if __name__ == "__main__":
    инициализация_интерфейса(info_panel=True)
    отрисовка_доски()

    окно.mainloop()