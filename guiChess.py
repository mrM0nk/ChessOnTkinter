from tkinter import Tk, Canvas, BOTH, Frame
from PIL import ImageTk, Image
from math import ceil
import time


окно = None
холст = None
отступ_x = None
отступ_y = None
клетка = None
фигуры = None
язык_игры = None
цветовая_схема = None
ширина_информационной_панели = None


def инициализация_интерфейса(info_panel):
    def настройки_игры():
        global язык_игры, цветовая_схема
        язык_игры = input('Select number your language? 1. Русский, 2. English: ')
        if язык_игры == '1':
            фон_игры = input('Выберите номер фона: 1. Природа, 2. Шахматы, 3. Космос: ')
            цветовая_схема = int(input('Выберите цветовую схему доски: 1. Светлая, 2. Обычная, 3. Гламур: '))
        else:
            фон_игры = input('Select background number: 1. Nature, 2. Chess, 3. Space: ')
            цветовая_схема = int(input('Choose board color scheme: 1. Light, 2. Ordinary, 3. Glamour: '))
        return фон_игры

    def создание_окна():
        global окно
        окно = Tk()
        ekranX = (окно.winfo_screenwidth())
        ekranY = (окно.winfo_screenheight())
#        окно.config(width=ekranX * 9 // 10, height=ekranY * 9 // 10, background="#CFFBA8")
        окно.title("Chess")
        окно.geometry("{}x{}+{}+{}".format(ekranX * 9 // 10, ekranY * 9 // 10, (ekranX - (ekranX * 9 // 10)) // 2, 0))
        окно.resizable(0, 0)

    def отрисовка_холста(фон_игры, info_panel = False):
        global холст, ширина_информационной_панели
        ekranX = (окно.winfo_screenwidth())
        ekranY = (окно.winfo_screenheight())
        контейнер1 = Frame(master=окно)
        if not info_panel:
            контейнер1.place(x=0, y=0, width=ekranX * 9 // 10, height=ekranY * 9 // 10)
            ширина_информационной_панели = 0
        if info_panel:
            ширина_информационной_панели = ekranX // 8
            контейнер1.place(x=0, y=0, width=ekranX * 9 // 10 - ширина_информационной_панели, height=ekranY * 9 // 10)
            контейнер2 = Frame(master = окно, background = "#CFFBA8")
            контейнер2.place(x = ekranX * 9 // 10 - ширина_информационной_панели, y = 0, width = ширина_информационной_панели, height = ekranY * 9 // 10)
        холст = Canvas(master=контейнер1)
        холст.pack(fill=BOTH, expand=True)
        if фон_игры == '1':
            фон = Image.open('background\image.jpg')
        elif фон_игры == '2':
            фон = Image.open('background\image2.jpg')
        else:
            фон = Image.open('background\image3.jpg')
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
        global отступ_x, отступ_y, клетка
        ekranX = (окно.winfo_screenwidth())
        клетка = переменная_ширины_экрана // 11
        отступ_x = ekranX * 9 // 20 - клетка * 4 - ширина_информационной_панели // 2
        отступ_y = клетка * 3 // 2

    def импорт_изображений():
        global фигуры
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

    def отрисовка_доски():
        цветовая_палитра = {1: ["#E8E8E8", "#B0B0B0"], 2: ["#C9862F", "#6F1203"], 3: ["#FFC4D7", "#6A7250"]}
        светлый_оттенок, темный_оттенок = цветовая_палитра.get(цветовая_схема)
        def отрисовка_полотна_доски():
            холст.update()
            time.sleep(1)
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
                        холст.create_rectangle(отступ_x + x * клетка, отступ_y + y * клетка, отступ_x + x * клетка + клетка,
                                               отступ_y + y * клетка + клетка, fill=светлый_оттенок)
                    else:
                        холст.create_rectangle(отступ_x + x * клетка, отступ_y + y * клетка, отступ_x + x * клетка + клетка,
                                               отступ_y + y * клетка + клетка, fill=темный_оттенок)

        def отрисовка_координат():
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

        отрисовка_полотна_доски()
        отрисовка_клеток()
        отрисовка_координат()


    фон_игры = настройки_игры()
    создание_окна()
    отрисовка_холста(фон_игры, info_panel)
    переменная_ширины_экрана = ориентация_экрана()
    расчет_координат(переменная_ширины_экрана)
    импорт_изображений()
    отрисовка_доски()


def отрисовка_шахмат():
    холст.update()
    time.sleep(1)

    def отрисовка_черных_шахмат():
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

    def отрисовка_белых_шахмат():
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

    отрисовка_черных_шахмат()
    отрисовка_белых_шахмат()


def подсветить_клетки(коорд_свободных_клеток):
    палитра_подсветки = [0, '#F7C8F3', '#E1C191', '#E8E8E8']
    for i in range(len(коорд_свободных_клеток)):
        x, y = коорд_свободных_клеток[i]
        холст.create_rectangle(отступ_x + x * клетка - клетка, отступ_y - y * клетка + клетка * 8,
                               отступ_x + x * клетка, отступ_y - y * клетка + клетка * 9, fill=палитра_подсветки[цветовая_схема])


def нарисовать_фигуру(координата_x, координата_y, фигура):
    холст.create_image(отступ_x - клетка // 2 + клетка * координата_x,
                       отступ_y + клетка * 8 - клетка * координата_y + клетка // 2, image=фигуры.get(фигура))


def get_mouse():
    time.sleep(1 / 8)
    холст.update()
    time.sleep(7)
    getxx = окно.winfo_pointerx() - окно.winfo_rootx()
    getyy = окно.winfo_pointery() - окно.winfo_rooty()
    x_мыши = ceil((getxx - отступ_x) / клетка)
    y_мыши = 9 - ceil((getyy - отступ_y) / клетка)
    time.sleep(1 / 2)
    return x_мыши, y_мыши


def перемести_фигуру(короткий_путь):
    палитра_подсветки = [0, '#F7C8F3', '#E1C191', '#E8E8E8']
    x, y = короткий_путь[0]
    time.sleep(1 / 2)
    холст.update()
    холст.create_rectangle(отступ_x + x * клетка - клетка, отступ_y - y * клетка + клетка * 8, отступ_x + x * клетка,
                           отступ_y - y * клетка + клетка * 9, fill=палитра_подсветки[цветовая_схема], tags="Квадрат")
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
        холст.move("Квадрат", x_прирост * клетка, - y_прирост * клетка)
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
    if язык_игры == '1':
        холст.create_text(отступ_x + клетка * 4, отступ_y - клетка // 2.2, font=("Purisa", клетка // 3),
                          text="Наведите мышкой на стартовую клетку", fill="blue")
    else:
        холст.create_text(отступ_x + клетка * 4, отступ_y - клетка // 2.2, font=("Purisa", клетка // 3),
                          text="Mouse over the starting cell", fill="blue")
    x_мыши, y_мыши = get_mouse()
    старт_x = x_мыши
    старт_y = y_мыши
    холст.create_rectangle(отступ_x + старт_x * клетка - клетка, отступ_y - старт_y * клетка + клетка * 8,
                           отступ_x + старт_x * клетка, отступ_y - старт_y * клетка + клетка * 9, width=клетка//11,
                           outline="blue")
    if язык_игры == '1':
        холст.create_text(отступ_x + клетка * 4, отступ_y + клетка * 17 // 2, font=("Purisa", клетка // 3),
                          text="Наведите мышкой на финишную клетку", fill="red")
    else:
        холст.create_text(отступ_x + клетка * 4, отступ_y + клетка * 17 // 2, font=("Purisa", клетка // 3),
                          text="Mouse over the finish cell", fill="red")
    x_мыши, y_мыши = get_mouse()
    финиш_х = x_мыши
    финиш_у = y_мыши
    холст.create_rectangle(отступ_x + финиш_х * клетка - клетка, отступ_y - финиш_у * клетка + клетка * 8,
                           отступ_x + финиш_х * клетка, отступ_y - финиш_у * клетка + клетка * 9, width=клетка//11,
                           outline="red")
    return старт_x, старт_y, финиш_х, финиш_у

def перемести_фигуру__по_доске(короткий_путь):
    палитра_подсветки = [0, '#F7C8F3', '#E1C191', '#E8E8E8']
    x, y = короткий_путь[0]
    time.sleep(1 / 2)
    холст.update()
    холст.create_rectangle(отступ_x + x * клетка - клетка, отступ_y - y * клетка + клетка * 8, отступ_x + x * клетка,
                           отступ_y - y * клетка + клетка * 9, fill=палитра_подсветки[цветовая_схема], tags="Квадрат")
    time.sleep(1 / 20)
    холст.update()
    холст.create_image(отступ_x - клетка // 2 + клетка * x, отступ_y + клетка * 8 - клетка * y + клетка // 2,
                       image=фигуры.get('КоньБ'), tags="Конь")
    time.sleep(1 / 20)
    холст.update()
    ch = 1
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
        time.sleep(1 / 4)
        холст.update()
        if abs(x_прирост) > abs(y_прирост):
            for ix in range(abs(x_прирост)):
                холст.move("Конь", клетка * ((x_прирост) / abs(x_прирост)), 0)
                time.sleep(1 / 20)
                холст.update()
            for iy in range(abs(y_прирост)):
                холст.move("Конь", 0, - клетка * ((y_прирост) / abs(y_прирост)))
                time.sleep(1 / 20)
                холст.update()
        else:
            for iy in range(abs(y_прирост)):
                холст.move("Конь", 0, - клетка * ((y_прирост) / abs(y_прирост)))
                time.sleep(1 / 20)
                холст.update()
            for ix in range(abs(x_прирост)):
                холст.move("Конь", клетка * ((x_прирост) / abs(x_прирост)), 0)
                time.sleep(1 / 20)
                холст.update()
        холст.create_text(отступ_x - клетка // 2 + клетка * x, отступ_y + клетка * 8 - клетка * y + клетка // 2, font=("Purisa", клетка // 3),
                          text=ch, fill="black")
        time.sleep(1 / 20)
        холст.update()
        ch = ch + 1


if __name__ == '__main__':
    инициализация_интерфейса(info_panel = True)


    окно.mainloop()
