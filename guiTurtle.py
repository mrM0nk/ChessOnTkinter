import turtle #робот чертежник
turtle.tracer(0, 0) # Отключить режим отладки
cher = turtle.Turtle() #внутри модуля подключить класс который через точку

from ctypes  import *       # Определяем разрешение монитора
Ширина_монитора=(windll.user32.GetSystemMetrics(0))
Высота_монитора=(windll.user32.GetSystemMetrics(1))

turtle.colormode(255)
окно = turtle.Screen()  #Указываем размер окна игры
#Ширина_монитора = 485
#Высота_монитора = 325
окно.setup(Ширина_монитора, Высота_монитора)
окно.title("Наша будущая игра на Черепашке")
окно.bgcolor(207, 251, 168)

turtle.delay(0) #задержка рисовки стандарт 10 милисекунд
cher.penup()

кол_во_досок = int(input('Пожалуйста введите кол-во досок от 1 до 3 шт: '))


def нарисовать_доску(доска_Х, доска_У, клетка):
    cher.goto(доска_Х, доска_У)
    cher.color(201, 134, 47)
    cher.pendown()
    cher.begin_fill()
    for i in range(4):
        cher.forward(клетка * 10)
        cher.left(90)
    cher.end_fill()
    cher.penup()


def нарисовать_тени_доски(доска_Х, доска_У, клетка):
    cher.goto(доска_Х, доска_У)
    r = 90
    g = 40
    b = 40
    for i in range (4):
        r = r + 40
        g = g + 40
        b = b + 40
        cher.color(r, g, b)
        cher.pendown()
        cher.begin_fill()
        cher.forward(клетка * 10)
        cher.left(135)
        cher.forward(клетка / 8)
        cher.left(45)
        cher.forward(клетка * 10 -(1.41421356 * клетка / 8))
        cher.left(45)
        cher.forward(клетка / 8)
        cher.end_fill()
        cher.penup()
        cher.left(135)
        cher.forward(клетка * 10)
        cher.left(90)
    r = 0                           # Делаем контур тени
    g = 0
    b = 0
    for i in range (4):
        r = r + 50
        g = g + 15
        b = b + 5
        cher.color(r, g, b)
        cher.pendown()
        cher.forward(клетка * 10)
        cher.left(135)
        cher.forward(клетка / 8)
        cher.left(45)
        cher.forward(клетка * 10 -(1.41421356 * клетка / 8))
        cher.left(45)
        cher.forward(клетка / 8)
        cher.penup()
        cher.left(135)
        cher.forward(клетка * 10)
        cher.left(90)


def нарисовать_рамку_и_клетки (доска_Х, доска_У, клетка):
    cher.color(111, 18, 3)
    for y in range(доска_У + клетка, доска_У + клетка * 9, клетка * 2):
        for x in range(доска_Х + клетка, доска_Х + клетка * 9, клетка * 2):
            cher.goto(x, y)
            cher.pendown()
            cher.begin_fill()
            for k in range(4):
                cher.forward(клетка)
                cher.left(90)
            cher.end_fill()
            cher.penup()
    for y in range(доска_У + клетка * 2, доска_У + клетка * 10, клетка * 2):
        for x in range(доска_Х + клетка * 2, доска_Х + клетка * 10, клетка * 2):
            cher.goto(x, y)
            cher.pendown()
            cher.begin_fill()
            for k in range(4):
                cher.forward(клетка)
                cher.left(90)
            cher.end_fill()
            cher.penup()
    cher.color(0, 0, 0)
    cher.goto(доска_Х + клетка, доска_У + клетка)
    cher.pensize(2)
    cher.pendown()
    for i in range(4):
        cher.forward(клетка * 8)
        cher.left(90)
    cher.penup()
    cher.pensize(1)
    cher.color(0, 0, 0)
    for y in range(доска_У + клетка, доска_У + клетка * 9, клетка * 2):
        for x in range(доска_Х + клетка, доска_Х + клетка * 9, клетка * 2):
            cher.goto(x, y)
            cher.pendown()
            for k in range(4):
                cher.forward(клетка)
                cher.left(90)
            cher.penup()
    for y in range(доска_У + клетка * 2, доска_У + клетка * 10, клетка * 2):
        for x in range(доска_Х + клетка * 2, доска_Х + клетка * 10, клетка * 2):
            cher.goto(x, y)
            cher.pendown()
            for k in range(4):
                cher.forward(клетка)
                cher.left(90)
            cher.penup()


def нарисовать_координаты(доска_Х, доска_У, клетка):
    cher.goto(доска_Х+клетка * 3 // 2, доска_У + клетка // 2)
    ListY = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    iy = - 1
    for x in range(доска_Х+клетка * 3 // 2, доска_Х + клетка // 2 + клетка * 9, клетка):
        cher.goto(x, доска_У + клетка // 2)
        iy = iy + 1
        cher.write(ListY[iy], font=("Arial", round(клетка / 5)))
    cher.goto(доска_Х + клетка // 2, доска_У + клетка * 3 // 2)

    k_podpisX = 0                        # Пишем цифры
    for y in range(доска_У + клетка * 3 // 2, доска_У + клетка // 2 + клетка * 9, клетка):
        cher.goto(доска_Х + клетка // 2, y)
        k_podpisX = k_podpisX + 1
        cher.write(k_podpisX, font=("Arial", round(клетка / 5)))


def нарисовать_белые_шашки(доска_Х, доска_У, клетка):
    for y in range(round(доска_У + клетка + клетка / 10), round(доска_У + клетка / 10 + клетка * 4), клетка * 2):
        for x in range(round(доска_Х + клетка + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
            cher.color(153, 217, 234)
            cher.goto(x, y)
            cher.pendown()
            cher.begin_fill()
            cher.circle(клетка * 4 / 10)
            cher.end_fill()
            cher.penup()
    for y in range(round(доска_У + клетка + клетка / 5), round(доска_У + клетка / 5 + клетка * 4), клетка * 2):
        for x in range(round(доска_Х + клетка + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
            cher.color(220, 242, 248)
            cher.goto(x, y)
            cher.pendown()
            cher.begin_fill()
            cher.circle(клетка * 3 / 10)
            cher.end_fill()
            cher.penup()
    for x in range(round(доска_Х + клетка * 2 + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
        cher.color(153, 217, 234)
        cher.goto(x, round(доска_У + клетка * 2 + клетка / 10))
        cher.pendown()
        cher.begin_fill()
        cher.circle(клетка * 4 / 10)
        cher.end_fill()
        cher.penup()
    for x in range(round(доска_Х + клетка * 2 + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
        cher.color(220, 242, 248)
        cher.goto(x, round(доска_У + клетка * 2 + клетка / 5))
        cher.pendown()
        cher.begin_fill()
        cher.circle(клетка * 3 / 10)
        cher.end_fill()
        cher.penup()
    for y in range(round(доска_У + клетка + клетка *4 / 10), round(доска_У + клетка / 5 + клетка * 4), клетка * 2):
        for x in range(round(доска_Х + клетка + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
            cher.color(153, 217, 234)
            cher.goto(x, y)
            cher.pendown()
            cher.begin_fill()
            cher.circle(клетка / 10)
            cher.end_fill()
            cher.penup()
    for x in range(round(доска_Х + клетка * 2 + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
        cher.color(153, 217, 234)
        cher.goto(x, round(доска_У + клетка * 2 + клетка * 4 / 10))
        cher.pendown()
        cher.begin_fill()
        cher.circle(клетка / 10)
        cher.end_fill()
        cher.penup()                        # Рисуем контуры шашек
    for y in range(round(доска_У + клетка + клетка / 10), round(доска_У + клетка / 10 + клетка * 4), клетка * 2):
        for x in range(round(доска_Х + клетка + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
            cher.color(0, 0, 0)
            cher.goto(x, y)
            cher.pendown()
            cher.circle(клетка * 4 / 10)
            cher.penup()
    for y in range(round(доска_У + клетка + клетка / 5), round(доска_У + клетка / 5 + клетка * 4), клетка * 2):
        for x in range(round(доска_Х + клетка + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
            cher.color(0, 0, 0)
            cher.goto(x, y)
            cher.pendown()
            cher.circle(клетка * 3 / 10)
            cher.penup()
    for x in range(round(доска_Х + клетка * 2 + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
        cher.color(0, 0, 0)
        cher.goto(x, round(доска_У + клетка * 2 + клетка / 10))
        cher.pendown()
        cher.circle(клетка * 4 / 10)
        cher.penup()
    for x in range(round(доска_Х + клетка * 2 + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
        cher.color(0, 0, 0)
        cher.goto(x, round(доска_У + клетка * 2 + клетка / 5))
        cher.pendown()
        cher.circle(клетка * 3 / 10)
        cher.penup()
    for y in range(round(доска_У + клетка + клетка *4 / 10), round(доска_У + клетка / 5 + клетка * 4), клетка * 2):
        for x in range(round(доска_Х + клетка + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
            cher.color(0, 0, 0)
            cher.goto(x, y)
            cher.pendown()
            cher.circle(клетка / 10)
            cher.penup()
    for x in range(round(доска_Х + клетка * 2 + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
        cher.color(0, 0, 0)
        cher.goto(x, round(доска_У + клетка * 2 + клетка * 4 / 10))
        cher.pendown()
        cher.circle(клетка / 10)
        cher.penup()


def нарисовать_черные_шашки(доска_Х, доска_У, клетка):
    for x in range(round(доска_Х + клетка + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
        cher.color(119, 14, 137)
        cher.goto(x, round(доска_У + клетка * 7 + клетка / 10))
        cher.pendown()
        cher.begin_fill()
        cher.circle(клетка * 4 / 10)
        cher.end_fill()
        cher.penup()
    for x in range(round(доска_Х + клетка + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
        cher.color(72, 19, 70)
        cher.goto(x, round(доска_У + клетка * 7 + клетка / 5))
        cher.pendown()
        cher.begin_fill()
        cher.circle(клетка * 3 / 10)
        cher.end_fill()
        cher.penup()
    for y in range(round(доска_У + клетка * 6 + клетка / 10), round(доска_У + клетка / 10 + клетка * 9), клетка * 2):
        for x in range(round(доска_Х + клетка * 2 + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
            cher.color(119, 14, 137)
            cher.goto(x, y)
            cher.pendown()
            cher.begin_fill()
            cher.circle(клетка * 4 / 10)
            cher.end_fill()
            cher.penup()
    for y in range(round(доска_У + клетка * 6 + клетка / 5), round(доска_У + клетка / 5 + клетка * 9), клетка * 2):
        for x in range(round(доска_Х + клетка * 2 + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
            cher.color(72, 19, 70)
            cher.goto(x, y)
            cher.pendown()
            cher.begin_fill()
            cher.circle(клетка * 3 / 10)
            cher.end_fill()
            cher.penup()
    for x in range(round(доска_Х + клетка + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
        cher.color(119, 14, 137)
        cher.goto(x, round(доска_У + клетка * 7 + клетка * 4 / 10))
        cher.pendown()
        cher.begin_fill()
        cher.circle(клетка / 10)
        cher.end_fill()
        cher.penup()
    for y in range(round(доска_У + клетка * 6 + клетка * 4 / 10), round(доска_У + клетка / 5 + клетка * 9), клетка * 2):
         for x in range(round(доска_Х + клетка * 2 + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
            cher.color(119, 14, 137)
            cher.goto(x, y)
            cher.pendown()
            cher.begin_fill()
            cher.circle(клетка / 10)
            cher.end_fill()
            cher.penup()                         # Рисуем контуры шашек
    for x in range(round(доска_Х + клетка + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
        cher.color(0, 0, 0)
        cher.goto(x, round(доска_У + клетка * 7 + клетка / 10))
        cher.pendown()
        cher.circle(клетка * 4 / 10)
        cher.penup()
    for x in range(round(доска_Х + клетка + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
        cher.color(0, 0, 0)
        cher.goto(x, round(доска_У + клетка * 7 + клетка / 5))
        cher.pendown()
        cher.circle(клетка * 3 / 10)
        cher.penup()
    for y in range(round(доска_У + клетка * 6 + клетка / 10), round(доска_У + клетка / 10 + клетка * 9), клетка * 2):
        for x in range(round(доска_Х + клетка * 2 + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
            cher.color(0, 0, 0)
            cher.goto(x, y)
            cher.pendown()
            cher.circle(клетка * 4 / 10)
            cher.penup()
    for y in range(round(доска_У + клетка * 6 + клетка / 5), round(доска_У + клетка / 5 + клетка * 9), клетка * 2):
        for x in range(round(доска_Х + клетка * 2 + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
            cher.color(0, 0, 0)
            cher.goto(x, y)
            cher.pendown()
            cher.circle(клетка * 3 / 10)
            cher.penup()
    for x in range(round(доска_Х + клетка + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
        cher.color(0, 0, 0)
        cher.goto(x, round(доска_У + клетка * 7 + клетка * 4 / 10))
        cher.pendown()
        cher.circle(клетка / 10)
        cher.penup()
    for y in range(round(доска_У + клетка * 6 + клетка * 4 / 10), round(доска_У + клетка / 5 + клетка * 9), клетка * 2):
         for x in range(round(доска_Х + клетка * 2 + клетка / 2), round(доска_Х + клетка / 2 + клетка * 9), клетка * 2):
            cher.color(0, 0, 0)
            cher.goto(x, y)
            cher.pendown()
            cher.circle(клетка / 10)
            cher.penup()


def проверка_соотношения_сторон_экрана(Высота_монитора, Ширина_монитора):
    if Высота_монитора <= Ширина_монитора:
        Ширина_доски_с_погрешностью = Высота_монитора - Высота_монитора // 10
        Дельта_ширины_доски = Ширина_доски_с_погрешностью % 10
        Ширина_доски = Ширина_доски_с_погрешностью - Дельта_ширины_доски
        return Ширина_доски
    else:
        Ширина_доски_с_погрешностью = Ширина_монитора - Ширина_монитора // 10
        Дельта_ширины_доски = Ширина_доски_с_погрешностью % 10
        Ширина_доски = Ширина_доски_с_погрешностью - Дельта_ширины_доски
        return Ширина_доски


def нарисовать (доска_Х, доска_У, клетка):
    нарисовать_доску(доска_Х, доска_У, клетка)
    нарисовать_тени_доски(доска_Х, доска_У, клетка)
    нарисовать_рамку_и_клетки(доска_Х, доска_У, клетка)
    нарисовать_координаты(доска_Х, доска_У, клетка)
    нарисовать_белые_шашки(доска_Х, доска_У, клетка)
    нарисовать_черные_шашки(доска_Х, доска_У, клетка)


def расчеты_координат (кол_во_досок, Ширина_доски):
    a = []
    for n in range (1, кол_во_досок):
        a.append(n)
    z = 0
    for m in a:
        z = z + m
    z_ширины_доски = ['10', '12', '17']
    z_оси_Х = ['None', '5', '11', '-1', '16', '5', '-6']
    i = кол_во_досок - 1
    for x in range (1, кол_во_досок + 1, 1):
        z = z + 1
        клетка = Ширина_доски // int(z_ширины_доски[i])
        доска_Х = - клетка * int(z_оси_Х [z])
        доска_У = - клетка * 5

        нарисовать(доска_Х, доска_У, клетка)


Ширина_доски = проверка_соотношения_сторон_экрана(Высота_монитора, Ширина_монитора)
#доска_Х, доска_У, клетка = расчеты_координат(кол_во_досок, Ширина_доски)

проверка_соотношения_сторон_экрана(Высота_монитора, Ширина_монитора)
расчеты_координат(кол_во_досок, Ширина_доски)

#cher.goto(доска_Х, доска_У)


turtle.mainloop()
























