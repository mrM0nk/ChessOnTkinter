from tkinter import Tk, Canvas, BOTH, Frame, Label, Spinbox, Button, StringVar, Radiobutton
from math import ceil
from PIL import ImageTk, Image
import time
import random


окно = None
холст = None
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
кнопка_очистки = None
список_фигур_белых = ("ФерзьБ", "КорольБ", "СлонБ", "КоньБ", "ЛадьяБ", "ПешкаБ")
список_фигур_черных = ("ФерзьЧ", "КорольЧ", "СлонЧ", "КоньЧ", "ЛадьяЧ", "ПешкаЧ")
цвет_шахмат_игрока = "Белые"
ввод_текста = {"rus": {"текст_фона": "Выберите номер фона: 1. Природа, 2. Шахматы, 3. Космос: ",
                       "текст_цветовой_схемы": "Выберите цветовую схему доски: 1. Светлая, 2. Обычная, 3. Гламур: ",
                       "координаты_конюАБ": ("Наведите мышкой на стартовую клетку", "Наведите мышкой на финишную клетку"),
                       "координаты_подсветки": ("Введите координату X: ", "Введите координату Y: ", "Введите фигуру: ")},
               "en": {"текст_фона": "Select background number: 1. Nature, 2. Chess, 3. Space: ",
                      "текст_цветовой_схемы": "Choose board color scheme: 1. Light, 2. Ordinary, 3. Glamour: ",
                      "координаты_конюАБ": ("Mouse over the starting cell", "Mouse over the finish cell"),
                      "координаты_подсветки": ("Enter the coordinate X: ", "Enter the coordinate Y: ", "Enter a shape: ")}}


def инициализация_интерфейса(info_panel, ask_for_change_settings=False):

    def настройки_игры():
        global язык_игры, цветовая_схема
        язык_игры = input("Select number your language? rus. Русский, en. English: ")
        фон_игры = int(input(ввод_текста.get(язык_игры).get("текст_фона")))
        цветовая_схема = int(input(ввод_текста.get(язык_игры).get("текст_цветовой_схемы")))
        return фон_игры

    def создание_окна():
        global окно
        окно = Tk()
        ekranX = (окно.winfo_screenwidth())
        ekranY = (окно.winfo_screenheight())
        окно.title("Chess")
        окно.geometry("{}x{}+{}+{}".format(ekranX * 9 // 10, ekranY * 9 // 10, (ekranX - (ekranX * 9 // 10)) // 2, 0))
        окно.resizable(0, 0)

    def отрисовка_холста(фон_игры, info_panel=False):
        global холст, ширина_панели, задержка_анимации, кнопка_старт, кнопка_очистки, цвет_шахмат_игрока
        ekranX = (окно.winfo_screenwidth())
        ekranY = (окно.winfo_screenheight())
        контейнер1 = Frame(master=окно)
        if not info_panel:
            контейнер1.place(x=0, y=0, width=ekranX * 9 // 10, height=ekranY * 9 // 10)
        if info_panel:
            ширина_панели = ekranX // 8
            контейнер1.place(x=0, y=0, width=ekranX * 9 // 10 - ширина_панели, height=ekranY * 9 // 10)
            контейнер2 = Frame(master=окно, background="#CFFBA8")
            контейнер2.place(x=ekranX * 9 // 10 - ширина_панели, y=0, width=ширина_панели, height=ekranY * 9 // 10)
            холст1 = Canvas(master=контейнер2)
            холст1.pack(fill=BOTH, expand=True)
            фон1 = Image.open("background\image{}{}.jpg".format(фон_игры, фон_игры))
            фон1.thumbnail((ekranX, ekranY), Image.ANTIALIAS)
            холст1.image = ImageTk.PhotoImage(фон1)
            холст1.create_image((-ekranX * 9 // 10 - ширина_панели) // 2 + ширина_панели * 1.1, ekranY * 9 // 20,
                                image=холст1.image, anchor="center")

            шаг = ekranY * 9 // 250
            метка_величина_задержки = Label(master=контейнер2, text="Задержка, с:")
            метка_величина_задержки.place(x=ширина_панели // 8, y=шаг)

            задержка_анимации = Spinbox(master=контейнер2, from_=0, to=1, increment=0.1)
            задержка_анимации.place(x=ширина_панели // 8, y=шаг * 2, width=ширина_панели * 3 // 4)

            кнопка_старт = Button(master=контейнер2, text="Старт", foreground="red")
            кнопка_старт.place(x=ширина_панели // 8, y=шаг * 3, width=ширина_панели * 3 // 4)

            кнопка_очистки = Button(master=контейнер2, text="Очистить", foreground="black")
            кнопка_очистки.place(x=ширина_панели // 8, y=шаг * 4, width=ширина_панели * 3 // 4)

            метка_цвет = Label(master=контейнер2, text="Цвет шахмат:")
            метка_цвет.place(x=ширина_панели // 8, y=шаг * 6)

            цвета = ["Белые", "Черные"]

            цвет_шахмат_игрока = StringVar()
            цвет_шахмат_игрока.set("Белые")

            for i, цвет in enumerate(цвета):
                b = Radiobutton(master=контейнер2, text=цвет, variable=цвет_шахмат_игрока, value=цвет, indicatoron=0)
                b.place(x=ширина_панели // 8, y=шаг * (7 + i), width=ширина_панели * 3 // 4)



        холст = Canvas(master=контейнер1)
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
    if ask_for_change_settings:
        фон_игры = настройки_игры()

    создание_окна()
    отрисовка_холста(фон_игры, info_panel)
    переменная_ширины_экрана = ориентация_экрана()
    расчет_координат(переменная_ширины_экрана)
    импорт_изображений()

def отрисовка_доски():
    светлый_оттенок, темный_оттенок = цветовая_палитра_клеток.get(цветовая_схема)

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
                              text=координаты[ix], fill="black")
        k_podpisY = 9
        for y in range(0, 8):
            k_podpisY = k_podpisY - 1
            холст.create_text(отступ_x - клетка * 1 // 4, отступ_y + клетка * y + клетка * 2 // 4, text=k_podpisY,
                              fill="black")

    отрисовка_полотна_доски()
    отрисовка_клеток()
    отрисовка_координат()


def get_delay():
    try:
        задержка = задержка_анимации.get()
    except:
        задержка = 1
    return float(задержка)


def очистка_доски():
    try:
        for элемент in холст.find_all():
            холст.delete(элемент)
        холст.create_image((окно.winfo_screenwidth() * 9 // 10 - ширина_панели)//2, окно.winfo_screenheight() * 9 // 20,
                           image=холст.image, anchor="center")
        отрисовка_доски()
    except:
        pass


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
        холст.create_rectangle(отступ_x + x * клетка - клетка, отступ_y - y * клетка + клетка * 8, отступ_x +
                               x * клетка, отступ_y - y * клетка + клетка * 9, fill=палитра_подсветки[цветовая_схема-1])
        окно.update()
        time.sleep(get_delay())

def нарисовать_фигуру(координата_x, координата_y, фигура):
    холст.create_image(отступ_x - клетка // 2 + клетка * координата_x,
                       отступ_y + клетка * 8 - клетка * координата_y + клетка // 2, image=фигуры.get(фигура))


def get_mouse():
    time.sleep(get_delay() / 4)
    окно.update()
    time.sleep(7)
    getxx = окно.winfo_pointerx() - окно.winfo_rootx()
    getyy = окно.winfo_pointery() - окно.winfo_rooty()
    x_мыши = ceil((getxx - отступ_x) / клетка)
    y_мыши = 9 - ceil((getyy - отступ_y) / клетка)
    time.sleep(get_delay())
    return x_мыши, y_мыши


def перемести_фигуру(короткий_путь, номера_ходов=False):
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

        x, y = короткий_путь[0]
        time.sleep(get_delay())
        окно.update()
        холст.create_rectangle(отступ_x + x * клетка - клетка, отступ_y - y * клетка + клетка * 8, отступ_x + x * клетка,
                               отступ_y - y * клетка + клетка * 9, fill=палитра_подсветки[цветовая_схема-1], tags="Квадрат")
        time.sleep(get_delay())
        окно.update()
        холст.create_image(отступ_x - клетка // 2 + клетка * x, отступ_y + клетка * 8 - клетка * y + клетка // 2,
                           image=фигуры.get("КоньБ"), tags="Конь")
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
            if abs(x_прирост) > abs(y_прирост):
                отрисовка_коня_х()
                отрисовка_коня_у()
            else:
                отрисовка_коня_у()
                отрисовка_коня_х()
            if номера_ходов:
                рандомный_цвет = '#' + ''.join([random.choice('0123456789abcdef') for i in range(6)])
                холст.create_text(отступ_x - клетка // 2 + клетка * x, отступ_y + клетка * 8 - клетка * y + клетка // 2,
                                  font=("Purisa", клетка // 3), text=номер_хода, fill=рандомный_цвет)
                time.sleep(get_delay() / 10)
                окно.update()
                номер_хода += 1
    except:
        pass


def ввод_координат_конюАБ():
    координаты_коня = []
    for i in range(0, 2):
        рандомный_цвет = '#' + ''.join([random.choice('0123456789abcdef') for i in range(6)])
        холст.create_text(отступ_x + клетка * 4, отступ_y - клетка // 2.2, font=("Purisa", клетка // 3),
                          text=ввод_текста.get(язык_игры).get("координаты_конюАБ")[i], fill=рандомный_цвет,
                          tag="координаты_конюАБ")
        x_мыши, y_мыши = get_mouse()
        холст.create_rectangle(отступ_x + x_мыши * клетка - клетка, отступ_y - y_мыши * клетка + клетка * 8,
                               отступ_x + x_мыши * клетка, отступ_y - y_мыши * клетка + клетка * 9, width=клетка//11,
                               outline=рандомный_цвет)
        холст.delete("координаты_конюАБ")
        координаты_коня.append((x_мыши, y_мыши))
    старт_x, старт_y = координаты_коня[0]
    финиш_х, финиш_у = координаты_коня[1]
    return старт_x, старт_y, финиш_х, финиш_у


def ввод_координат_подсветки():
    координата_x = int(input(ввод_текста.get(язык_игры).get("координаты_подсветки")[0]))
    координата_y = int(input(ввод_текста.get(язык_игры).get("координаты_подсветки")[1]))
    фигура = input(ввод_текста.get(язык_игры).get("координаты_подсветки")[2])
    return координата_x, координата_y, фигура


if __name__ == "__main__":
    инициализация_интерфейса(info_panel=True, ask_for_change_settings=False)
    отрисовка_доски()
    окно.mainloop()