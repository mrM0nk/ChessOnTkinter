from tkinter import Tk, Canvas, BOTH
from PIL import ImageTk, Image


def инициализация_интерфейса():
    def создание_окна():
        окно = Tk()
        ekranX = (окно.winfo_screenwidth())
        ekranY = (окно.winfo_screenheight())
        # ekranX = 1366
        # ekranY = 768
        окно.config(width=ekranX * 9 // 10, height=ekranY * 9 // 10, background="#CFFBA8")
        окно.title("Working Tkinter")
        окно.geometry("+50+0")  # !!!
        окно.resizable(0, 0)
        return окно


    def отрисовка_холста (окно):
        ekranX = (окно.winfo_screenwidth())
        ekranY = (окно.winfo_screenheight())
        холст = Canvas(width = ekranX * 9 // 10, height = ekranY * 9 // 10)
        холст.pack(fill = BOTH, expand = True)
        фон = Image.open('images\image2.jpg')
        фон.thumbnail((ekranX, ekranY),Image.ANTIALIAS)
        холст.image = ImageTk.PhotoImage(фон)
        холст.create_image(0, 0, image=холст.image, anchor='nw')
        return холст, окно


    def ориентация_экрана(окно):
        ekranX = (окно.winfo_screenwidth())
        ekranY = (окно.winfo_screenheight())
        if ekranY <= ekranX:
            переменная_ширины_экрана = ekranY * 9 // 10
        else:
            переменная_ширины_экрана = ekranX * 9 // 10
        return переменная_ширины_экрана


    def расчет_координат(переменная_ширины_экрана):
        ekranX = (окно.winfo_screenwidth())
        клетка = переменная_ширины_экрана // 12
        отступ_x = ekranX * 9 / 20 - клетка * 4
        отступ_y = клетка * 3 // 2
        return отступ_x, отступ_y, клетка


    окно = создание_окна()
    холст, окно = отрисовка_холста(окно)
    переменная_ширины_экрана = ориентация_экрана (окно)
    отступ_x, отступ_y, клетка = расчет_координат(переменная_ширины_экрана)
    return холст, отступ_x, отступ_y, клетка, окно


def импорт_изображений(клетка):
    pilImage = Image.open("images\shashka21.png")
    pilImage.thumbnail((клетка * 9 // 10, клетка * 9 // 10), Image.ANTIALIAS)
    ШашкаЧ = ImageTk.PhotoImage(pilImage)

    pilImage = Image.open("images\shashka20.png")
    pilImage.thumbnail((клетка * 9 // 10, клетка * 9 // 10), Image.ANTIALIAS)
    ШашкаБ = ImageTk.PhotoImage(pilImage)
    return ШашкаЧ, ШашкаБ


def отрисовка_доски(холст, отступ_x, отступ_y, клетка):
    def отрисовка_полотна_доски (холст, отступ_x, отступ_y, клетка):
        холст.create_rectangle(отступ_x - клетка * 3 // 4, отступ_y - клетка * 3 // 4, отступ_x + клетка * 8 + клетка * 3 // 4, отступ_y + клетка * 8  + клетка * 3 // 4, fill = "#C9862F")
        холст.create_line(отступ_x - клетка * 3 // 4, отступ_y + клетка * 3 // 4 + клетка * 8, отступ_x, отступ_y + клетка * 8, width = 2, fill = "#6F1203")
        холст.create_line(отступ_x - клетка * 3 // 4, отступ_y - клетка * 3 // 4, отступ_x, отступ_y, width = 2, fill = "#6F1203")
        холст.create_line(отступ_x + клетка * 8, отступ_y, отступ_x + клетка * 3 // 4 + клетка * 8, отступ_y - клетка * 3 // 4, width = 2, fill = "#6F1203")
        холст.create_line(отступ_x + клетка * 8, отступ_y  + клетка * 8, отступ_x + клетка * 3 // 4 + клетка * 8, отступ_y + клетка * 3 // 4 + клетка * 8, width = 2, fill = "#6F1203")
        холст.create_rectangle(отступ_x - клетка * 3 // 4, отступ_y - клетка * 3 // 4, отступ_x + клетка * 8 + клетка * 3 // 4, отступ_y + клетка * 8  + клетка * 3 // 4, width = 5, outline = "#770E89")
        холст.create_rectangle(отступ_x, отступ_y, отступ_x + клетка * 8, отступ_y + клетка * 8, width = 7)


    def отрисовка_клеток(холст, отступ_x, отступ_y, клетка):
        for y in range(8):
            for x in range(8):
                if (x + y) % 2 == 0:
                    холст.create_rectangle(отступ_x + x * клетка, отступ_y + y * клетка, отступ_x + x * клетка + клетка, отступ_y + y * клетка + клетка, fill = "#C9862F")
                else:
                    холст.create_rectangle(отступ_x + x * клетка, отступ_y + y * клетка, отступ_x + x * клетка + клетка, отступ_y + y * клетка + клетка,  fill = "#6F1203")


    def отрисовка_координат(холст, отступ_x, отступ_y, клетка):
        ListY = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        iy = - 1
        for x in range(0, 8):
            iy = iy + 1
            холст.create_text(отступ_x + клетка * 2 // 4 + клетка * x, отступ_y + клетка * 8  + клетка * 1 // 4, text=ListY[iy], fill="black")
        k_podpisX = 9
        for y in range(0, 8):
            k_podpisX = k_podpisX - 1
            холст.create_text(отступ_x - клетка * 1 // 4, отступ_y + клетка * y  + клетка * 2 // 4, text=k_podpisX, fill="black")


    отрисовка_полотна_доски(холст, отступ_x, отступ_y, клетка)
    отрисовка_клеток(холст, отступ_x, отступ_y, клетка)
    отрисовка_координат(холст, отступ_x, отступ_y, клетка)


def отрисовка_шашек(холст, отступ_x, отступ_y, клетка):
    def отрисовка_черных_шашек(холст, отступ_x, отступ_y, клетка):
        for y in range(3):
            for x in range(8):
                if (x + y) % 2 == 0:
                    continue
                else:
                    imagesprite = холст.create_image(отступ_x + x * клетка + клетка // 2, отступ_y + y * клетка + клетка // 2, image=ШашкаЧ)


    def отрисовка_белых_шашек(холст, отступ_x, отступ_y, клетка):
        for y in range(5, 8):
            for x in range(8):
                if (x + y) % 2 == 0:
                    continue
                else:
                    imagesprite = холст.create_image(отступ_x + x * клетка + клетка // 2, отступ_y + y * клетка + клетка // 2, image=ШашкаБ)


    отрисовка_черных_шашек(холст, отступ_x, отступ_y, клетка)
    отрисовка_белых_шашек(холст, отступ_x, отступ_y, клетка)


холст, отступ_x, отступ_y, клетка, окно = инициализация_интерфейса()
ШашкаЧ, ШашкаБ = импорт_изображений(клетка)
отрисовка_доски(холст, отступ_x, отступ_y, клетка)
отрисовка_шашек(холст, отступ_x, отступ_y, клетка)



окно.mainloop()





