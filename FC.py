from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
import time
import random

tk = Tk()  # Создаём окно
tk.title('Фризские шашки')  # Заголовок окна
board = Canvas(tk, width=1400, height=1000, bg='#FFFFFF')
tk.resizable(width=False, height=False)
board.pack()
app_running = True
tk.update()

hod_igroka = True
vozmozhnost_belih_shodit = False
vozmozhnost_chernih_shodit = False
white_count = 20
black_count = 20
vozm_b_zabrat_vverh = False
vozm_b_zabrat_vniz = False
vozm_b_zabrat_vlevo = False
vozm_b_zabrat_vpravo = False
vozm_b_zabrat_vpravo_vverh = False
vozm_b_zabrat_vlevo_vverh = False
vozm_b_zabrat_vpravo_vniz = False
vozm_b_zabrat_vlevo_vniz = False
vozm_b_zabrat = False
vozm_b_d_zabrat_vverh = False
vozm_b_d_zabrat_vniz = False
vozm_b_d_zabrat_vlevo = False
vozm_b_d_zabrat_vpravo = False
vozm_b_d_zabrat = False
vozm_b_d_zabrat_vpravo_vverh = False
vozm_b_d_zabrat_vlevo_vverh = False
vozm_b_d_zabrat_vlevo_vniz = False
vozm_b_d_zabrat_vpravo_vniz = False
vozm_ch_zabrat_vniz = False
vozm_ch_zabrat_vlevo = False
vozm_ch_zabrat_vpravo = False
vozm_ch_zabrat_vverh = False
vozm_ch_zabrat_vpravo_vverh = False
vozm_ch_zabrat_vlevo_vverh = False
vozm_ch_zabrat_vpravo_vniz = False
vozm_ch_zabrat_vlevo_vniz = False
vozm_ch_zabrat = False
vozm_ch_d_zabrat_vverh = False
vozm_ch_d_zabrat_vniz = False
vozm_ch_d_zabrat_vlevo = False
vozm_ch_d_zabrat_vpravo = False
vozm_ch_d_zabrat_vpravo_vverh = False
vozm_ch_d_zabrat_vlevo_vverh = False
vozm_ch_d_zabrat_vlevo_vniz = False
vozm_ch_d_zabrat_vpravo_vniz = False
vozm_ch_d_zabrat = False

def izobrazheniya_figur():  # загружаем изображения фигур
    global figuri
    i1 = PhotoImage(file="res\\white_checkers.png")
    i2 = PhotoImage(file="res\\black_checkers.png")
    i3 = PhotoImage(file="res\\white_checkers_king.png")
    i4 = PhotoImage(file="res\\black_checkers_king.png")
    figuri = [0, i1, i2, i3, i4]


def novaya_igra():  # начинаем новую игру
    global pole

    pole =  [[0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
             [2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
             [0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
             [2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]

def Start_new():
    global white_count
    global black_count
    global hod_igroka
    if askyesno("Игра закончена","Хотите начать новую?"):
        novaya_igra()
        vivod(-1,-1)
        hod_igroka = True
        white_count = 20
        black_count = 20

def vivod(x_poz_1, y_poz_1):  # рисуем игровое поле
    global figuri
    global pole
    k = 100
    x = 0
    board.delete('all')

    while x < 10 * k:  # рисуем доску
        y = k
        while y < 10 * k:
            board.create_rectangle(x, y, x + k, y + k, fill="Black")
            y += 2 *k
        x += 2 * k
    x = k
    while x < 10 * k:  # рисуем доску
        y = 0
        while y < 10 * k:
            board.create_rectangle(x, y, x + k, y + k, fill="Black")
            y += 2 * k
        x += 2 * k

    for y in range(10):  # рисуем стоячие пешки
        for x in range(10):
            z = pole[y][x]
            if z:
                if (x_poz_1, y_poz_1) != (x, y):  # стоячие пешки?
                    board.create_image(x * k, y * k, anchor=NW, image=figuri[z])


def vozmozhnost_belih_hodit(x, y): #метод, проверяющий белые шашки на доступность хода(что им ничего не преграждает путь)
    global vozmozhnost_belih_shodit
    global prev_b_coord_x
    global prev_b_coord_y
    if pole[x][y] == 1: # для белой не дамки
        if (pole[x - 1][y - 1] == 0 and x > 0 and y > 0) or (y < 9 and x > 0 and pole[x - 1][y + 1] == 0):
            vozmozhnost_belih_shodit = True
        else:
            vozmozhnost_belih_shodit = False
        prev_b_coord_x = x
        prev_b_coord_y = y
    elif pole[x][y] == 3: # для белой дамки
        if (pole[x - 1][y - 1] == 0 and x > 0 and y > 0) or (y < 9 and x > 0 and pole[x - 1][y + 1] == 0) or (pole[x + 1][y - 1] == 0 and x < 9 and y > 0) or (x < 9 and y < 9 and pole[x + 1][y + 1] == 0):
            vozmozhnost_belih_shodit = True
        else:
            vozmozhnost_belih_shodit = False
        prev_b_coord_x = x
        prev_b_coord_y = y


def vozmozhnost_chernih_hodit(x, y): #метод, проверяющий черные шашки на доступность хода(что им ничего не преграждает путь)
    global vozmozhnost_chernih_shodit
    global prev_ch_coord_x
    global prev_ch_coord_y

    if pole[x][y] == 2: # для черной не дамки
        if (pole[x + 1][y - 1] == 0 and x < 9 and y > 0) or (y < 9 and x < 9 and pole[x + 1][y + 1] == 0):
            vozmozhnost_chernih_shodit = True
        else:
            vozmozhnost_chernih_shodit = False
        prev_ch_coord_x = x
        prev_ch_coord_y = y
    elif pole[x][y] == 4: # для черной дамки
        if (pole[x - 1][y - 1] == 0 and x > 0 and y > 0) or (y < 9 and x > 0 and pole[x - 1][y + 1] == 0) or (pole[x + 1][y - 1] == 0 and x < 9 and y > 0) or (x < 9 and y < 9 and pole[x + 1][y + 1] == 0):
            vozmozhnost_chernih_shodit = True
        else:
            vozmozhnost_chernih_shodit = False
        prev_ch_coord_x = x
        prev_ch_coord_y = y

def belie_proverka():
    global vozm_b_zabrat_vverh
    global vozm_b_zabrat_vniz
    global vozm_b_zabrat_vlevo
    global vozm_b_zabrat_vpravo
    global vozm_b_zabrat_vpravo_vverh
    global vozm_b_zabrat_vlevo_vverh
    global vozm_b_zabrat_vlevo_vniz
    global vozm_b_zabrat_vpravo_vniz
    global vozm_b_zabrat
    global vozm_b_d_zabrat_vverh
    global vozm_b_d_zabrat_vniz
    global vozm_b_d_zabrat_vlevo
    global vozm_b_d_zabrat_vpravo
    global vozm_b_d_zabrat
    global vozm_b_d_zabrat_vpravo_vverh
    global vozm_b_d_zabrat_vlevo_vverh
    global vozm_b_d_zabrat_vlevo_vniz
    global vozm_b_d_zabrat_vpravo_vniz

    for i in range(10):      # ищем на поле возможность случая забирания
        for j in range(10):
            if (pole[i][j] == 1 and i > 3) and (pole[i - 2][j] == 2 or pole[i - 2][j] == 4) and pole[i - 4][j] == 0: # для белой шашки вверх
                vozm_b_zabrat_vverh = True
                vozm_b_zabrat = True

            if (pole[i][j] == 1 and i < 6) and (pole[i + 2][j] == 2 or pole[i+2][j] == 4) and pole[i+4][j] == 0:
                vozm_b_zabrat_vniz = True
                vozm_b_zabrat = True

            if (pole[i][j] == 1 and j > 3) and (pole[i][j - 2] == 2 or pole[i][j - 2] == 4) and pole[i][j - 4] == 0: # для белой шашки влево
                vozm_b_zabrat_vlevo = True
                vozm_b_zabrat = True

            if (pole[i][j] == 1 and j < 6) and (pole[i][j + 2] == 2 or pole[i][j+2] == 4) and pole[i][j + 4] == 0: # для белой шашки вправо
                vozm_b_zabrat = True
                vozm_b_zabrat_vpravo = True

            if (pole[i][j] == 1 and i > 1 and j < 8) and (pole[i - 1][j + 1] == 2 or pole[i - 1][j + 1] == 4) and pole[i - 2][j + 2] == 0:
                vozm_b_zabrat = True
                vozm_b_zabrat_vpravo_vverh = True

            if (pole[i][j] == 1 and i > 1 and j > 1) and (pole[i - 1][j - 1] == 2 or pole[i - 1][j - 1] == 4) and pole[i - 2][j - 2] == 0:
                vozm_b_zabrat = True
                vozm_b_zabrat_vlevo_vverh = True

            if (pole[i][j] == 1 and i < 8 and j < 8) and (pole[i + 1][j + 1] == 2 or pole[i + 1][j + 1] == 4) and pole[i + 2][j + 2] == 0:
                vozm_b_zabrat = True
                vozm_b_zabrat_vpravo_vniz = True

            if (pole[i][j] == 1 and i < 8 and j > 1) and (pole[i + 1][j - 1] == 2 or pole[i + 1][j - 1] == 4) and pole[i + 2][j - 2] == 0:
                vozm_b_zabrat = True
                vozm_b_zabrat_vlevo_vniz = True

            if i > 1 and pole[i][j] == 3:  # для белой дамки вверх
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    count = 0
                    if pole[k][j] == 0 and ((k < 8 and pole[k + 2][j] == 2) or (k < 8 and pole[k + 2][j] == 4)) and (k < 6 and pole[k + 4][j] == 0 or k < 6 and pole[k + 4][j] == 3):
                        while pole[k][j] != 3:
                            if j < 9 and pole[i][j + 2] == 3:
                                vozm_b_d_zabrat_vverh = True
                                vozm_b_d_zabrat = True
                                break
                            ch_count += 1
                            if k < 8:
                                k += 2
                            else:
                                break
                            if pole[k][j] == 0:
                                zero_count += 1
                            if pole[k][j] == 2 or pole[k][j] == 4 and j > 0:
                                count += 1
                            if count == 2:
                                break
                            if zero_count == ch_count - 2 and pole[k][j] == 3 and k > 0:
                                vozm_b_d_zabrat_vverh = True
                                vozm_b_d_zabrat = True
                            else:
                                vozm_b_d_zabrat_vverh = False
                        break

            if i < 6 and pole[i][j] == 3:  # для белой дамки вниз
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    if pole[k][j] == 0 and ((k > 2 and pole[k - 2][j] == 2) or (k > 1 and pole[k - 2][j] == 4)):
                        while pole[k][j] != 3:
                            ch_count += 1
                            k -= 2
                            if pole[k][j] == 0:
                                zero_count += 1
                            if zero_count == ch_count - 2 and pole[k][j] == 3:
                                vozm_b_d_zabrat_vniz = True
                                vozm_b_d_zabrat = True
                            else:
                                vozm_b_d_zabrat_vniz = True
                        break

            if j > 3 and pole[i][j] == 3:  # для белой дамки влево
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    count = 0
                    if pole[i][k] == 0 and ((k < 8 and pole[i][k + 2] == 2) or (k < 8 and pole[i][k + 2] == 4)) and (k < 6 and pole[i][k + 4] == 0 or k < 6 and pole[i][k + 4] == 3):
                        while pole[i][k] != 3:
                            if k < 8 and pole[i + 2][j] == 3:
                                vozm_b_d_zabrat_vlevo = True
                                vozm_b_d_zabrat = True
                                break
                            ch_count += 1
                            if k < 8:
                                k += 2
                            else:
                                break
                            if pole[i][k] == 0:
                                zero_count += 1
                            if pole[i][k] == 2 or pole[i][k] == 4:
                                count += 1
                            if count == 2:
                                break
                            if zero_count == ch_count - 2 and pole[i][k] == 3:
                                vozm_b_d_zabrat_vlevo = True
                                vozm_b_d_zabrat = True
                            else:
                                vozm_b_d_zabrat_vlevo = False

            if j < 6 and pole[i][j] == 3:  # для белой дамки вправо
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    if pole[i][k] == 0 and ((k > 2 and pole[i][k - 2] == 2) or (k > 2 and pole[i][k - 2] == 4)):
                        while pole[i][k] != 3:
                            ch_count += 1
                            k -= 2
                            if pole[i][k] == 0:
                                zero_count += 1
                            if zero_count == ch_count - 2 and pole[i][k] == 3:
                                vozm_b_d_zabrat_vpravo = True
                                vozm_b_d_zabrat = True
                            else:
                                vozm_b_zabrat_vpravo = False
                        break
            if j > 1 and i < 8 and pole[j][i] == 3:
                count = 0
                ch_count = 0
                if (pole[j - 1][i + 1] == 2 or pole[j - 1][i + 1] == 4) and pole[j - 2][i + 2] == 0:
                    vozm_b_d_zabrat = True
                    vozm_b_d_zabrat_vpravo_vverh = True
                else:
                    while j > 0 and i < 9:
                        j -= 1
                        i += 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 2 or pole[j][i] == 4:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 2 or pole[j][i] == 4) and pole[j - 1][i + 1] == 0 and count == 1:
                            vozm_b_d_zabrat = True
                            vozm_b_d_zabrat_vpravo_vverh = True
                            break
                        else:
                            vozm_b_d_zabrat_vpravo_vverh = False
            if j > 1 and i > 1 and pole[j][i] == 3:
                ch_count = 0
                count = 0
                if (pole[j - 1][i - 1] == 2 or pole[j - 1][i - 1] == 4) and pole[j - 2][i - 2] == 0:
                    vozm_b_d_zabrat = True
                    vozm_b_d_zabrat_vlevo_vverh = True
                else:
                    while j > 0 and i > 0:
                        j -= 1
                        i -= 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 2 or pole[j][i] == 4:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 2 or pole[j][i] == 4) and pole[j - 1][i - 1] == 0 and count == 1:
                            vozm_b_d_zabrat = True
                            vozm_b_d_zabrat_vlevo_vverh = True
                            break
                        else:
                            vozm_b_d_zabrat_vlevo_vverh = False
            if j < 8 and i > 1 and pole[j][i] == 3:
                ch_count = 0
                count = 0
                if (pole[j + 1][i - 1] == 2 or pole[j + 1][i - 1] == 4) and pole[j + 2][i - 2] == 0:
                    vozm_b_d_zabrat = True
                    vozm_b_d_zabrat_vlevo_vniz = True
                else:
                    while j < 9 and i > 0:
                        j += 1
                        i -= 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 2 or pole[j][i] == 4:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 2 or pole[j][i] == 4) and pole[j + 1][i - 1] == 0 and count == 1:
                            vozm_b_d_zabrat = True
                            vozm_b_d_zabrat_vlevo_vniz = True
                            break
                        else:
                            vozm_b_d_zabrat_vlevo_vniz = False

            if j < 8 and i < 8 and pole[j][i] == 3:
                ch_count = 0
                count = 0
                if (pole[j + 1][i + 1] == 2 or pole[j + 1][i + 1] == 4) and pole[j + 2][i + 2] == 0:
                    vozm_b_d_zabrat = True
                    vozm_b_d_zabrat_vpravo_vniz = True
                else:
                    while j < 9 and i < 9:
                        j += 1
                        i += 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 2 or pole[j][i] == 4:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 2 or pole[j][i] == 4) and pole[j + 1][i + 1] == 0 and count == 1:
                            vozm_b_d_zabrat = True
                            vozm_b_d_zabrat_vpravo_vniz = True
                            break
                        else:
                            vozm_b_d_zabrat_vpravo_vniz = False
def chernie_proverka(): # аналогично с тем что выше
    global vozm_ch_zabrat_vverh
    global vozm_ch_zabrat_vniz
    global vozm_ch_zabrat_vlevo
    global vozm_ch_zabrat_vpravo
    global vozm_ch_zabrat_vpravo_vverh
    global vozm_ch_zabrat_vlevo_vverh
    global vozm_ch_zabrat_vlevo_vniz
    global vozm_ch_zabrat_vpravo_vniz
    global vozm_ch_zabrat
    global vozm_ch_d_zabrat_vverh
    global vozm_ch_d_zabrat_vniz
    global vozm_ch_d_zabrat_vlevo
    global vozm_ch_d_zabrat_vpravo
    global vozm_ch_d_zabrat
    global vozm_ch_d_zabrat_vpravo_vverh
    global vozm_ch_d_zabrat_vlevo_vverh
    global vozm_ch_d_zabrat_vlevo_vniz
    global vozm_ch_d_zabrat_vpravo_vniz

    for i in range(10):
        for j in range(10):
            if (pole[i][j] == 2 and i > 3) and (pole[i - 2][j] == 1 or pole[i - 2][j] == 3) and pole[i - 4][
                j] == 0:  # для белой шашки вверх
                vozm_ch_zabrat_vverh = True
                vozm_ch_zabrat = True

            if (pole[i][j] == 2 and i < 6) and (pole[i + 2][j] == 1 or pole[i + 2][j] == 3) and pole[i + 4][j] == 0:
                vozm_ch_zabrat_vniz = True
                vozm_ch_zabrat = True

            if (pole[i][j] == 2 and j > 3) and (pole[i][j - 2] == 1 or pole[i][j - 2] == 3) and pole[i][
                j - 4] == 0:  # для белой шашки влево
                vozm_ch_zabrat_vlevo = True
                vozm_ch_zabrat = True

            if (pole[i][j] == 2 and j < 6) and (pole[i][j + 2] == 1 or pole[i][j + 2] == 3) and pole[i][
                j + 4] == 0:  # для белой шашки вправо
                vozm_ch_zabrat = True
                vozm_ch_zabrat_vpravo = True

            if (pole[i][j] == 2 and i > 1 and j < 8) and (pole[i - 1][j + 1] == 1 or pole[i - 1][j + 1] == 3) and \
                    pole[i - 2][j + 2] == 0:
                vozm_ch_zabrat = True
                vozm_ch_zabrat_vpravo_vverh = True

            if (pole[i][j] == 2 and i > 1 and j > 1) and (pole[i - 1][j - 1] == 1 or pole[i - 1][j - 1] == 3) and \
                    pole[i - 2][j - 2] == 0:
                vozm_ch_zabrat = True
                vozm_ch_zabrat_vlevo_vverh = True

            if (pole[i][j] == 2 and i < 8 and j < 8) and (pole[i + 1][j + 1] == 1 or pole[i + 1][j + 1] == 3) and \
                    pole[i + 2][j + 2] == 0:
                vozm_ch_zabrat = True
                vozm_ch_zabrat_vpravo_vniz = True

            if (pole[i][j] == 2 and i < 8 and j > 1) and (pole[i + 1][j - 1] == 1 or pole[i + 1][j - 1] == 3) and \
                    pole[i + 2][j - 2] == 0:
                vozm_ch_zabrat = True
                vozm_ch_zabrat_vlevo_vniz = True

            if i > 1 and pole[i][j] == 4:  # для белой дамки вверх
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    count = 0
                    if pole[k][j] == 0 and ((k < 8 and pole[k + 2][j] == 1) or (k < 8 and pole[k + 2][j] == 3)) and (
                            k < 6 and pole[k + 4][j] == 0 or k < 6 and pole[k + 4][j] == 4):
                        while pole[k][j] != 4:
                            if j < 9 and pole[i][j + 2] == 4:
                                vozm_ch_d_zabrat_vverh = True
                                vozm_ch_d_zabrat = True
                                break
                            ch_count += 1
                            if k < 8:
                                k += 2
                            else:
                                break
                            if pole[k][j] == 0:
                                zero_count += 1
                            if pole[k][j] == 1 or pole[k][j] == 3 and j > 0:
                                count += 1
                            if count == 2:
                                break
                            if zero_count == ch_count - 2 and pole[k][j] == 4 and k > 0:
                                vozm_ch_d_zabrat_vverh = True
                                vozm_ch_d_zabrat = True
                            else:
                                vozm_ch_d_zabrat_vverh = False
                        break

            if i < 6 and pole[i][j] == 4:  # для белой дамки вниз
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    if pole[k][j] == 0 and ((k > 2 and pole[k - 2][j] == 1) or (k > 1 and pole[k - 2][j] == 3)):
                        while pole[k][j] != 4:
                            ch_count += 1
                            k -= 2
                            if pole[k][j] == 0:
                                zero_count += 1
                            if zero_count == ch_count - 2 and pole[k][j] == 4:
                                vozm_ch_d_zabrat_vniz = True
                                vozm_ch_d_zabrat = True
                            else:
                                vozm_ch_d_zabrat_vniz = True
                        break

            if j > 3 and pole[i][j] == 4:  # для белой дамки влево
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    count = 0
                    if pole[i][k] == 0 and ((k < 8 and pole[i][k + 2] == 1) or (k < 8 and pole[i][k + 2] == 3)) and (
                            k < 6 and pole[i][k + 4] == 0 or k < 6 and pole[i][k + 4] == 4):
                        while pole[i][k] != 4:
                            if k < 8 and pole[i + 2][j] == 4:
                                vozm_ch_d_zabrat_vlevo = True
                                vozm_ch_d_zabrat = True
                                break
                            ch_count += 1
                            if k < 8:
                                k += 2
                            else:
                                break
                            if pole[i][k] == 0:
                                zero_count += 1
                            if pole[i][k] == 1 or pole[i][k] == 3:
                                count += 1
                            if count == 2:
                                break
                            if zero_count == ch_count - 2 and pole[i][k] == 4:
                                vozm_ch_d_zabrat_vlevo = True
                                vozm_ch_d_zabrat = True
                            else:
                                vozm_ch_d_zabrat_vlevo = False

            if j < 6 and pole[i][j] == 4:  # для белой дамки вправо
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    if pole[i][k] == 0 and ((k > 2 and pole[i][k - 2] == 1) or (k > 2 and pole[i][k - 2] == 3)):
                        while pole[i][k] != 4:
                            ch_count += 1
                            k -= 2
                            if pole[i][k] == 0:
                                zero_count += 1
                            if zero_count == ch_count - 2 and pole[i][k] == 4:
                                vozm_ch_d_zabrat_vpravo = True
                                vozm_ch_d_zabrat = True
                            else:
                                vozm_ch_zabrat_vpravo = False
                        break
            if j > 1 and i < 8 and pole[j][i] == 4:
                count = 0
                ch_count = 0
                if (pole[j - 1][i + 1] == 1 or pole[j - 1][i + 1] == 3) and pole[j - 2][i + 2] == 0:
                    vozm_ch_d_zabrat = True
                    vozm_ch_d_zabrat_vpravo_vverh = True
                else:
                    while j > 0 and i < 9:
                        j -= 1
                        i += 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 1 or pole[j][i] == 3:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 1 or pole[j][i] == 3) and pole[j - 1][i + 1] == 0 and count == 1:
                            vozm_ch_d_zabrat = True
                            vozm_ch_d_zabrat_vpravo_vverh = True
                            break
                        else:
                            vozm_ch_d_zabrat_vpravo_vverh = False
            if j > 1 and i > 1 and pole[j][i] == 4:
                ch_count = 0
                count = 0
                if (pole[j - 1][i - 1] == 1 or pole[j - 1][i - 1] == 3) and pole[j - 2][i - 2] == 0:
                    vozm_ch_d_zabrat = True
                    vozm_ch_d_zabrat_vlevo_vverh = True
                else:
                    while j > 0 and i > 0:
                        j -= 1
                        i -= 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 1 or pole[j][i] == 3:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 1 or pole[j][i] == 3) and pole[j - 1][i - 1] == 0 and count == 1:
                            vozm_ch_d_zabrat = True
                            vozm_ch_d_zabrat_vlevo_vverh = True
                            break
                        else:
                            vozm_ch_d_zabrat_vlevo_vverh = False
            if j < 8 and i > 1 and pole[j][i] == 4:
                ch_count = 0
                count = 0
                if (pole[j + 1][i - 1] == 1 or pole[j + 1][i - 1] == 3) and pole[j + 2][i - 2] == 0:
                    vozm_ch_d_zabrat = True
                    vozm_ch_d_zabrat_vlevo_vniz = True
                else:
                    while j < 9 and i > 0:
                        j += 1
                        i -= 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 1 or pole[j][i] == 3:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 1 or pole[j][i] == 3) and pole[j + 1][i - 1] == 0 and count == 1:
                            vozm_ch_d_zabrat = True
                            vozm_ch_d_zabrat_vlevo_vniz = True
                            break
                        else:
                            vozm_ch_d_zabrat_vlevo_vniz = False

            if j < 8 and i < 8 and pole[j][i] == 4:
                ch_count = 0
                count = 0
                if (pole[j + 1][i + 1] == 1 or pole[j + 1][i + 1] == 3) and pole[j + 2][i + 2] == 0:
                    vozm_ch_d_zabrat = True
                    vozm_ch_d_zabrat_vpravo_vniz = True
                else:
                    while j < 9 and i < 9:
                        j += 1
                        i += 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 1 or pole[j][i] == 3:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 1 or pole[j][i] == 3) and pole[j + 1][i + 1] == 0 and count == 1:
                            vozm_ch_d_zabrat = True
                            vozm_ch_d_zabrat_vpravo_vniz = True
                            break
                        else:
                            vozm_ch_d_zabrat_vpravo_vniz = False

def click_event(event):
    global hod_igroka
    global white_count
    global black_count
    global vozm_b_zabrat
    global vozm_b_zabrat_vverh
    global vozm_b_zabrat_vniz
    global vozm_b_zabrat_vlevo
    global vozm_b_zabrat_vpravo
    global vozm_b_zabrat_vpravo_vverh
    global vozm_b_zabrat_vlevo_vverh
    global vozm_b_zabrat_vlevo_vniz
    global vozm_b_zabrat_vpravo_vniz
    global vozm_b_d_zabrat_vverh
    global vozm_b_d_zabrat_vniz
    global vozm_b_d_zabrat_vlevo
    global vozm_b_d_zabrat_vpravo
    global vozm_b_d_zabrat
    global vozm_ch_zabrat_vverh
    global vozm_ch_zabrat_vniz
    global vozm_ch_zabrat_vlevo
    global vozm_ch_zabrat_vpravo
    global vozm_ch_zabrat_vpravo_vverh
    global vozm_ch_zabrat_vlevo_vverh
    global vozm_ch_zabrat_vlevo_vniz
    global vozm_ch_zabrat_vpravo_vniz
    global vozm_ch_zabrat
    global vozm_ch_d_zabrat_vverh
    global vozm_ch_d_zabrat_vniz
    global vozm_ch_d_zabrat_vlevo
    global vozm_ch_d_zabrat_vpravo
    global vozm_ch_d_zabrat
    global vozm_ch_d_zabrat_vpravo_vverh
    global vozm_ch_d_zabrat_vlevo_vverh
    global vozm_ch_d_zabrat_vlevo_vniz
    global vozm_ch_d_zabrat_vpravo_vniz

    global prev_b_coord_x
    global prev_b_coord_y
    global prev_ch_coord_x
    global prev_ch_coord_y

    if 0 < event.x < 1000 and 0 < event.y < 1000:  # Если кликнули на доске
        x = event.y // 100  # Определяем строку на которую нажали
        y = event.x // 100  # Определяем столбец на который нажали

    if hod_igroka:
        if vozm_b_d_zabrat: # если у белых дамок есть возможность забрать черную шашку
            if vozm_b_d_zabrat_vverh:
                if pole[prev_b_coord_x][prev_b_coord_y] == 3 and prev_b_coord_x > 1 and pole[x][y] == 0 and prev_b_coord_y == y:
                    if x < prev_b_coord_x and x < 9 and pole[x + 1][y] == 2 or x < 9 and pole[x + 1][y] == 4:
                        ch_count = 0
                        not_zero_count = 0
                        prev_x = prev_b_coord_x
                        for k in range(prev_b_coord_x, x, -1): # проверяем все ли клетки на пути пустые
                            ch_count += 1
                            if pole[prev_b_coord_x][y] != 0:
                                not_zero_count += 1
                            prev_b_coord_x -= 1
                        if not_zero_count == 2 and (pole[x + 2][y] == 2 or pole[x + 2][y] == 4): # если на пути ничего не мешает, то едим
                            pole[x][y] = 3
                            pole[prev_x][prev_b_coord_y] = 0
                            pole[x + 2][y] = 0
                            black_count -= 1
                            vivod(-1, -1)

            if vozm_b_d_zabrat_vniz:
                if pole[prev_b_coord_x][prev_b_coord_y] == 3 and prev_b_coord_x < 9 and pole[x][y] == 0 and prev_b_coord_y == y:
                    if x > prev_b_coord_x and pole[x - 1][y] == 2 or pole[x - 1][y] == 4:
                        ch_count = 0
                        not_zero_count = 0
                        prev_x = prev_b_coord_x
                        for k in range(x, prev_b_coord_x, -1):
                            ch_count += 1
                            if pole[prev_b_coord_x][y] != 0:
                                not_zero_count += 1
                            prev_b_coord_x += 1
                        if not_zero_count == 2 and (pole[x - 2][y] == 2 or pole[x - 2][y] == 4):
                            pole[x][y] = 3
                            pole[prev_x][prev_b_coord_y] = 0
                            pole[x - 2][y] = 0
                            black_count -= 1
                            vivod(-1, -1)

            if vozm_b_d_zabrat_vlevo:
                if pole[prev_b_coord_x][prev_b_coord_y] == 3 and prev_b_coord_y > 1 and pole[x][y] == 0 and prev_b_coord_x == x:
                    if y < prev_b_coord_y and y < 9 and pole[x][y + 1] == 2 or y < 9 and pole[x][y + 1] == 4:
                        ch_count = 0
                        not_zero_count = 0
                        prev_y = prev_b_coord_y
                        for k in range(prev_b_coord_y, y, -1):
                            ch_count += 1
                            if pole[x][prev_b_coord_y] != 0:
                                not_zero_count += 1
                            prev_b_coord_y -= 1
                        if not_zero_count == 2 and (pole[x][y+2] == 2 or pole[x][y + 2] == 4):
                            pole[x][y] = 3
                            pole[prev_b_coord_x][prev_y] = 0
                            pole[x][y + 2] = 0
                            black_count -= 1
                            vivod(-1, -1)

            if vozm_b_d_zabrat_vpravo:
                if pole[prev_b_coord_x][prev_b_coord_y] == 3 and prev_b_coord_y < 8 and pole[x][y] == 0 and prev_b_coord_x == x:
                    if y > prev_b_coord_y and pole[x][y - 1] == 2 or pole[x][y - 1] == 4:
                        ch_count = 0
                        not_zero_count = 0
                        prev_y = prev_b_coord_y
                        for k in range(y, prev_b_coord_y, -1):
                            ch_count += 1
                            if pole[x][prev_b_coord_y] != 0:
                                not_zero_count += 1
                            prev_b_coord_y += 1
                        if not_zero_count == 2 and (pole[x][y-2] == 2 or pole[x][y - 2] == 4):
                            pole[x][y] = 3
                            pole[prev_b_coord_x][prev_y] = 0
                            pole[x][y - 2] = 0
                            black_count -= 1
                            vivod(-1, -1)
            if vozm_b_d_zabrat_vlevo_vverh:
                if prev_b_coord_x > x and prev_b_coord_y > y and (prev_b_coord_x - prev_b_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(prev_b_coord_x - x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x -= 1
                        if pole[prev_b_coord_x][prev_b_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x+1][y+1] == 2 or pole[x+1][y+1] == 4):
                        pole[x+1][y+1] = 0
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1, -1)
                        black_count -= 1
            if vozm_b_d_zabrat_vpravo_vverh:
                if prev_b_coord_x > x and prev_b_coord_y < y and (prev_b_coord_x + prev_b_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(prev_b_coord_x - x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x -= 1
                        if pole[prev_b_coord_x][prev_b_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x+1][y-1] == 2 or pole[x+1][y-1] == 4):
                        pole[x+1][y-1] = 0
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1, -1)
                        black_count -= 1
            if vozm_b_d_zabrat_vlevo_vniz:
                if prev_b_coord_x < x and prev_b_coord_y > y and (prev_b_coord_x + prev_b_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(x - prev_b_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x += 1
                        if pole[prev_b_coord_x][prev_b_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x-1][y+1] == 2 or pole[x-1][y+1] == 4):
                        pole[x-1][y+1] = 0
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1, -1)
                        black_count -= 1
            if vozm_b_d_zabrat_vpravo_vniz:
                if prev_b_coord_x < x and prev_b_coord_y < y and (prev_b_coord_x - prev_b_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(x - prev_b_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x += 1
                        if pole[prev_b_coord_x][prev_b_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x-1][y-1] == 2 or pole[x-1][y-1] == 4):
                        pole[x-1][y-1] = 0
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1, -1)
                        black_count -= 1
            vozm_b_d_zabrat = False
            belie_proverka()
            if vozm_b_d_zabrat == False:
                hod_igroka = False
        if vozm_b_zabrat: # если возможность белых не дамок забрать
            if vozm_b_zabrat_vverh:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_x > 3 and (pole[prev_b_coord_x - 2][y] == 2 or pole[prev_b_coord_x - 2][y] == 4) and pole[x][y] == 0 and pole[x + 4][y] == 1 and prev_b_coord_x == x + 4 and prev_b_coord_y == y:
                    if prev_b_coord_x == 4 and x + 2 == 1 and x == 0: # если прыгнули на поле, превращающее в дамку
                        pole[x][y] = 3
                    else:
                        pole[x][y] = 1
                    pole[x + 4][y] = 0
                    pole[x + 2][y] = 0
                    black_count -= 1
                    vivod(-1, -1)
            if vozm_b_zabrat_vniz:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_x < 6 and (pole[prev_b_coord_x + 2][y] == 2 or pole[prev_b_coord_x + 2][y] == 4) and pole[x][y] == 0 and pole[x - 4][y] == 1 and prev_b_coord_x == x - 4 and prev_b_coord_y == y:
                    pole[x][y] = 1
                    pole[x-4][y] = 0
                    pole[x- 2][y] = 0
                    black_count -= 1
                    vivod(-1, -1)
            if vozm_b_zabrat_vlevo:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_y > 3 and (pole[prev_b_coord_x][prev_b_coord_y - 2] == 2 or pole[prev_b_coord_x][prev_b_coord_y - 2] == 4) and pole[x][y] == 0 and pole[prev_b_coord_x][prev_b_coord_y - 4] == 0 and prev_b_coord_x == x and prev_b_coord_y == y + 4:
                    pole[prev_b_coord_x][y + 4] = 0
                    pole[x][y + 2] = 0
                    pole[x][y] = 1
                    black_count -= 1
                    vivod(-1, -1)

            if vozm_b_zabrat_vpravo:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_y < 6 and (pole[prev_b_coord_x][prev_b_coord_y + 2] == 2 or pole[prev_b_coord_x][prev_b_coord_y + 2] == 4) and pole[x][y] == 0 and pole[prev_b_coord_x][prev_b_coord_y + 4] == 0 and prev_b_coord_x == x and prev_b_coord_y == y - 4:
                    pole[prev_b_coord_x][y - 4] = 0
                    pole[x][y - 2] = 0
                    pole[x][y] = 1
                    black_count -= 1
                    vivod(-1, -1)

            if vozm_b_zabrat_vlevo_vverh:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_y > 1 and prev_b_coord_x > 1 and (pole[prev_b_coord_x - 1][prev_b_coord_y - 1] == 2 or pole[prev_b_coord_x - 1][prev_b_coord_y - 1] == 4) and pole[x][y] == 0 and pole[prev_b_coord_x - 2][prev_b_coord_y - 2] == 0 and prev_b_coord_x == x + 2 and prev_b_coord_y == y + 2:
                    pole[prev_b_coord_x][prev_b_coord_y] = 0
                    pole[prev_b_coord_x - 1][prev_b_coord_y - 1] = 0
                    pole[x][y] = 1
                    black_count -= 1
                    vivod(-1, -1)

            if vozm_b_zabrat_vpravo_vverh:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_y < 8 and prev_b_coord_x > 1 and (pole[prev_b_coord_x - 1][prev_b_coord_y + 1] == 2 or pole[prev_b_coord_x - 1][prev_b_coord_y + 1] == 4) and pole[x][y] == 0 and pole[prev_b_coord_x - 2][prev_b_coord_y + 2] == 0 and prev_b_coord_x == x + 2 and prev_b_coord_y == y - 2:
                    pole[prev_b_coord_x][prev_b_coord_y] = 0
                    pole[prev_b_coord_x - 1][prev_b_coord_y + 1] = 0
                    pole[x][y] = 1
                    black_count -= 1
                    vivod(-1, -1)

            if vozm_b_zabrat_vlevo_vniz:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_y > 1 and prev_b_coord_x < 8 and (pole[prev_b_coord_x + 1][prev_b_coord_y - 1] == 2 or pole[prev_b_coord_x + 1][prev_b_coord_y - 1] == 4) and pole[x][y] == 0 and pole[prev_b_coord_x + 2][prev_b_coord_y - 2] == 0 and prev_b_coord_x == x - 2 and prev_b_coord_y == y + 2:
                    pole[prev_b_coord_x][prev_b_coord_y] = 0
                    pole[prev_b_coord_x + 1][prev_b_coord_y - 1] = 0
                    pole[x][y] = 1
                    black_count -= 1
                    vivod(-1, -1)

            if vozm_b_zabrat_vpravo_vniz:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_y < 8 and prev_b_coord_x < 8 and (pole[prev_b_coord_x + 1][prev_b_coord_y + 1] == 2 or pole[prev_b_coord_x + 1][prev_b_coord_y + 1] == 4) and pole[x][y] == 0 and pole[prev_b_coord_x + 2][prev_b_coord_y + 2] == 0 and prev_b_coord_x == x - 2 and prev_b_coord_y == y - 2:
                    pole[prev_b_coord_x][prev_b_coord_y] = 0
                    pole[prev_b_coord_x + 1][prev_b_coord_y + 1] = 0
                    pole[x][y] = 1
                    black_count -= 1
                    vivod(-1, -1)
            vozm_b_zabrat = False

            belie_proverka()
            if vozm_b_d_zabrat == False and vozm_b_zabrat == False:
                hod_igroka = False
        belie_proverka()
        vozmozhnost_belih_hodit(x, y)
        if white_count == 0:
            messagebox.showinfo(title='Победа черных', message='Победили черные.', icon='info')
            hod_igroka = None
            Start_new()
        belie_proverka()
        vivod(-1,-1)
        if vozmozhnost_belih_shodit: # если выбранная шашка может ходить(ей ничего не преграждает путь)
            vivod(-1, -1)
            if pole[x][y] == 1:
                board.create_rectangle(y * 100 + 100, x * 100 + 100, y * 100, x * 100, width=5, outline="Blue")
                if x > 0 and y > 0 and pole[x - 1][y - 1] == 0 and vozm_b_zabrat == False:
                    board.create_rectangle(y * 100 - 100, x * 100 - 100, y * 100, x * 100, width=5, outline="Green")
                if x > 0 and y < 9 and pole[x - 1][y + 1] == 0 and vozm_b_zabrat == False:
                    board.create_rectangle(y * 100 + 100, x * 100 - 100, y * 100 + 200, x * 100, width=5, outline="Green")
                if x > 3 and (pole[x-2][y] == 2 or pole[x-2][y] == 4) and pole[x-4][y] == 0:
                    board.create_rectangle(y * 100 + 100, x * 100 - 300, y * 100, x * 100 - 400, width=5, outline="Red")
                if x < 6 and (pole[x+2][y] == 2 or pole[x+2][y] == 4) and pole[x+4][y] == 0:
                    board.create_rectangle(y * 100 + 100, x * 100 + 500, y * 100, x * 100 + 400, width=5, outline="Red")
                if y < 6 and (pole[x][y + 2] == 2 or pole[x][y + 2] == 4) and pole[x][y + 4] == 0:
                    board.create_rectangle(y * 100 + 500, x * 100 + 100, y * 100 + 400, x * 100, width=5, outline="Red")
                if y > 3 and (pole[x][y - 2] == 2 or pole[x][y - 2] == 4) and pole[x][y - 4] == 0:
                    board.create_rectangle(y * 100 - 300, x * 100 + 100, y * 100 - 400, x * 100, width=5, outline="Red")
                if x > 1 and y > 1 and (pole[x-1][y-1] == 2 or pole[x-1][y-1] == 4) and pole[x-2][y-2] == 0:
                    board.create_rectangle(y * 100 - 200, x * 100 - 200, y * 100 - 100, x * 100 - 100, width=5, outline="Red")
                if x > 1 and y < 8 and (pole[x - 1][y + 1] == 2 or pole[x - 1][y + 1] == 4) and pole[x - 2][y + 2] == 0:
                    board.create_rectangle(y * 100 + 300, x * 100 - 200, y * 100 + 200, x * 100 - 100, width=5,outline="Red")
                if x < 8 and y > 1 and (pole[x + 1][y - 1] == 2 or pole[x + 1][y - 1] == 4) and pole[x + 2][y - 2] == 0:
                    board.create_rectangle(y * 100 - 200, x * 100 + 300, y * 100 - 100, x * 100 + 200, width=5,outline="Red")
                if x < 8 and y < 8 and (pole[x + 1][y + 1] == 2 or pole[x + 1][y + 1] == 4) and pole[x + 2][y + 2] == 0:
                    board.create_rectangle(y * 100 + 300, x * 100 + 300, y * 100 + 200, x * 100 + 200, width=5,outline="Red")

            if pole[prev_b_coord_x][prev_b_coord_y] != 0 and ((prev_b_coord_y == y + 1 and prev_b_coord_x == x + 1) or (prev_b_coord_y == y - 1 and prev_b_coord_x == x + 1)):  # Проверяем, сходили ли мы на одну клетку вертикально или горизонтально
                vivod(-1,-1)
                if pole[x][y] == 0 and vozm_b_zabrat == False and vozm_b_d_zabrat == False: # если эта клетка пустая и нету контроля для забирания(поедания)
                    if pole[prev_b_coord_x][prev_b_coord_y] == 1: # если сходили на поле, превращающее в дамку
                        if x == 0:
                            pole[x][y] = 3
                        else:
                            pole[x][y] = 1
                        pole[prev_b_coord_x][prev_b_coord_y] = 0
                        vivod(-1, -1)  # рисуем игровое поле
                        hod_igroka = False
            if pole[prev_b_coord_x][prev_b_coord_y] == 3 and pole[x][y] == 0 and vozm_b_zabrat == False and vozm_b_d_zabrat == False: # ходы для белой дамки
                if prev_b_coord_x > x and prev_b_coord_y > y and (prev_b_coord_x - prev_b_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(prev_b_coord_x - x): # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x -= 1
                        if pole[prev_b_coord_x][prev_b_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1,-1)
                        hod_igroka = False

                if prev_b_coord_x > x and prev_b_coord_y < y and (prev_b_coord_x + prev_b_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(prev_b_coord_x - x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x -= 1
                        if pole[prev_b_coord_x][prev_b_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1, -1)
                        hod_igroka = False
                if prev_b_coord_x < x and prev_b_coord_y > y and (prev_b_coord_x + prev_b_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(x - prev_b_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x += 1
                        if pole[prev_b_coord_x][prev_b_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1, -1)
                        hod_igroka = False
                if prev_b_coord_x < x and prev_b_coord_y < y and (prev_b_coord_x - prev_b_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(x - prev_b_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x += 1
                        if pole[prev_b_coord_x][prev_b_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1, -1)
                        hod_igroka = False
        else:
            vivod(-1,-1)
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################


    if not hod_igroka:

        if vozm_ch_d_zabrat:
            if vozm_ch_d_zabrat_vverh:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 4 and prev_b_coord_x > 1 and pole[x][
                    y] == 0 and prev_ch_coord_y == y:
                    if x < prev_ch_coord_x and x < 9 and pole[x + 1][y] == 1 or x < 9 and pole[x + 1][y] == 3:
                        ch_count = 0
                        not_zero_count = 0
                        prev_x = prev_ch_coord_x
                        for k in range(prev_ch_coord_x, x, -1):  # проверяем все ли клетки на пути пустые
                            ch_count += 1
                            if pole[prev_ch_coord_x][y] != 0:
                                not_zero_count += 1
                            prev_ch_coord_x -= 1
                        if not_zero_count == 2 and (pole[x + 2][y] == 1 or pole[x + 2][y] == 3):  # если на пути ничего не мешает, то едим
                            pole[x][y] = 4
                            pole[prev_x][prev_ch_coord_y] = 0
                            pole[x + 2][y] = 0
                            white_count -= 1
                            vivod(-1, -1)

            if vozm_ch_d_zabrat_vniz:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 4 and prev_ch_coord_x < 9 and pole[x][
                    y] == 0 and prev_ch_coord_y == y:
                    if x > prev_ch_coord_x and pole[x - 1][y] == 1 or pole[x - 1][y] == 3:
                        ch_count = 0
                        not_zero_count = 0
                        prev_x = prev_ch_coord_x
                        for k in range(x, prev_ch_coord_x, -1):
                            ch_count += 1
                            if pole[prev_ch_coord_x][y] != 0:
                                not_zero_count += 1
                            prev_ch_coord_x += 1
                        if not_zero_count == 2 and (pole[x + 2][y] == 1 or pole[x + 2][y] == 3):
                            pole[x][y] = 4
                            pole[prev_x][prev_ch_coord_y] = 0
                            pole[x - 2][y] = 0
                            white_count -= 1
                            vivod(-1, -1)

            if vozm_ch_d_zabrat_vlevo:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 4 and prev_ch_coord_y > 1 and pole[x][
                    y] == 0 and prev_ch_coord_x == x:
                    if y < prev_ch_coord_y and y < 9 and pole[x][y + 1] == 1 or y < 9 and pole[x][y + 1] == 3:
                        ch_count = 0
                        not_zero_count = 0
                        prev_y = prev_ch_coord_y
                        for k in range(prev_ch_coord_y, y, -1):
                            ch_count += 1
                            if pole[x][prev_ch_coord_y] != 0:
                                not_zero_count += 1
                            prev_ch_coord_y -= 1
                        if not_zero_count == 2 and (pole[x][y + 2] == 1 or pole[x][y + 2] == 3):
                            pole[x][y] = 3
                            pole[prev_ch_coord_x][prev_y] = 0
                            pole[x][y + 2] = 0
                            white_count -= 1
                            vivod(-1, -1)

            if vozm_ch_d_zabrat_vpravo:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 4 and prev_ch_coord_y < 8 and pole[x][
                    y] == 0 and prev_ch_coord_x == x:
                    if y > prev_ch_coord_y and pole[x][y - 1] == 1 or pole[x][y - 1] == 3:
                        ch_count = 0
                        not_zero_count = 0
                        prev_y = prev_ch_coord_y
                        for k in range(y, prev_ch_coord_y, -1):
                            ch_count += 1
                            if pole[x][prev_ch_coord_y] != 0:
                                not_zero_count += 1
                            prev_ch_coord_y += 1
                        if not_zero_count == 2 and (pole[x][y - 2] == 1 or pole[x][y - 2] == 3):
                            pole[x][y] = 3
                            pole[prev_b_coord_x][prev_y] = 0
                            pole[x][y - 2] = 0
                            white_count -= 1
                            vivod(-1, -1)
            if vozm_ch_d_zabrat_vlevo_vverh:
                if prev_ch_coord_x > x and prev_ch_coord_y > y and (prev_ch_coord_x - prev_ch_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(prev_ch_coord_x - x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x -= 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x + 1][y + 1] == 1 or pole[x + 1][y + 1] == 3):
                        pole[x + 1][y + 1] = 0
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        white_count -= 1
            if vozm_ch_d_zabrat_vpravo_vverh:
                if prev_ch_coord_x > x and prev_ch_coord_y < y and (prev_ch_coord_x + prev_ch_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(prev_ch_coord_x - x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x -= 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x + 1][y - 1] == 1 or pole[x + 1][y - 1] == 3):
                        pole[x + 1][y - 1] = 0
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        white_count -= 1
            if vozm_ch_d_zabrat_vlevo_vniz:
                if prev_ch_coord_x < x and prev_ch_coord_y > y and (prev_ch_coord_x + prev_ch_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(x - prev_ch_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x += 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x - 1][y + 1] == 1 or pole[x - 1][y + 1] == 3):
                        pole[x - 1][y + 1] = 0
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        white_count -= 1
            if vozm_ch_d_zabrat_vpravo_vniz:
                if prev_ch_coord_x < x and prev_ch_coord_y < y and (prev_ch_coord_x - prev_ch_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(x - prev_ch_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x += 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x - 1][y - 1] == 1 or pole[x - 1][y - 1] == 3):
                        pole[x - 1][y - 1] = 0
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        white_count -= 1

            vozm_ch_d_zabrat = False
            chernie_proverka()
            if vozm_ch_d_zabrat == False:
                hod_igroka = True
        if vozm_ch_zabrat:  # если возможность белых не дамок забрать
            if vozm_ch_zabrat_vverh:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_x > 3 and (
                        pole[prev_ch_coord_x - 2][y] == 1 or pole[prev_ch_coord_x - 2][y] == 3) and pole[x][y] == 0 and \
                        pole[x + 4][y] == 2 and prev_ch_coord_x == x + 4 and prev_ch_coord_y == y:

                    pole[x][y] = 2
                    pole[x + 4][y] = 0
                    pole[x + 2][y] = 0
                    white_count -= 1
                    vivod(-1, -1)
            if vozm_ch_zabrat_vniz:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_x < 6 and (
                        pole[prev_ch_coord_x + 2][y] == 1 or pole[prev_ch_coord_x + 2][y] == 3) and pole[x][y] == 0 and \
                        pole[x - 4][y] == 2 and prev_ch_coord_x == x - 4 and prev_ch_coord_y == y:
                    if prev_ch_coord_x == 5 and x - 2 == 7 and x == 9:
                        pole[x][y] = 4
                    else:
                        pole[x][y] = 2
                    pole[x - 4][y] = 0
                    pole[x - 2][y] = 0
                    white_count -= 1
                    vivod(-1, -1)
            if vozm_ch_zabrat_vlevo:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_y > 3 and (
                        pole[prev_ch_coord_x][prev_ch_coord_y - 2] == 1 or pole[prev_ch_coord_x][
                    prev_ch_coord_y - 2] == 3) and pole[x][y] == 0 and pole[prev_ch_coord_x][
                    prev_ch_coord_y - 4] == 0 and prev_ch_coord_x == x and prev_ch_coord_y == y + 4:
                    pole[prev_ch_coord_x][y + 4] = 0
                    pole[x][y + 2] = 0
                    pole[x][y] = 2
                    white_count -= 1
                    vivod(-1, -1)

            if vozm_ch_zabrat_vpravo:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_y < 6 and (
                        pole[prev_ch_coord_x][prev_ch_coord_y + 2] == 1 or pole[prev_ch_coord_x][
                    prev_ch_coord_y + 2] == 3) and pole[x][y] == 0 and pole[prev_ch_coord_x][
                    prev_ch_coord_y + 4] == 0 and prev_ch_coord_x == x and prev_ch_coord_y == y - 4:
                    pole[prev_ch_coord_x][y - 4] = 0
                    pole[x][y - 2] = 0
                    pole[x][y] = 2
                    white_count -= 1
                    vivod(-1, -1)

            if vozm_ch_zabrat_vlevo_vverh:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_y > 1 and prev_ch_coord_x > 1 and (
                        pole[prev_ch_coord_x - 1][prev_ch_coord_y - 1] == 1 or pole[prev_ch_coord_x - 1][
                    prev_ch_coord_y - 1] == 3) and pole[x][y] == 0 and pole[prev_ch_coord_x - 2][
                    prev_ch_coord_y - 2] == 0 and prev_ch_coord_x == x + 2 and prev_ch_coord_y == y + 2:
                    pole[prev_ch_coord_x][prev_ch_coord_y] = 0
                    pole[prev_ch_coord_x - 1][prev_ch_coord_y - 1] = 0
                    pole[x][y] = 2
                    white_count -= 1
                    vivod(-1, -1)

            if vozm_ch_zabrat_vpravo_vverh:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_y < 8 and prev_ch_coord_x > 1 and (
                        pole[prev_ch_coord_x - 1][prev_ch_coord_y + 1] == 1 or pole[prev_ch_coord_x - 1][
                    prev_ch_coord_y + 1] == 3) and pole[x][y] == 0 and pole[prev_ch_coord_x - 2][
                    prev_ch_coord_y + 2] == 0 and prev_ch_coord_x == x + 2 and prev_ch_coord_y == y - 2:
                    pole[prev_ch_coord_x][prev_ch_coord_y] = 0
                    pole[prev_ch_coord_x - 1][prev_ch_coord_y + 1] = 0
                    pole[x][y] = 2
                    white_count -= 1
                    vivod(-1, -1)

            if vozm_ch_zabrat_vlevo_vniz:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_y > 1 and prev_ch_coord_x < 8 and (
                        pole[prev_ch_coord_x + 1][prev_ch_coord_y - 1] == 1 or pole[prev_ch_coord_x + 1][
                    prev_ch_coord_y - 1] == 3) and pole[x][y] == 0 and pole[prev_ch_coord_x + 2][
                    prev_ch_coord_y - 2] == 0 and prev_ch_coord_x == x - 2 and prev_ch_coord_y == y + 2:
                    pole[prev_ch_coord_x][prev_ch_coord_y] = 0
                    pole[prev_ch_coord_x + 1][prev_ch_coord_y - 1] = 0
                    pole[x][y] = 2
                    white_count -= 1
                    vivod(-1, -1)

            if vozm_ch_zabrat_vpravo_vniz:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_y < 8 and prev_ch_coord_x < 8 and (
                        pole[prev_ch_coord_x + 1][prev_ch_coord_y + 1] == 1 or pole[prev_ch_coord_x + 1][
                    prev_ch_coord_y + 1] == 3) and pole[x][y] == 0 and pole[prev_ch_coord_x + 2][
                    prev_ch_coord_y + 2] == 0 and prev_ch_coord_x == x - 2 and prev_ch_coord_y == y - 2:
                    pole[prev_ch_coord_x][prev_ch_coord_y] = 0
                    pole[prev_ch_coord_x + 1][prev_ch_coord_y + 1] = 0
                    pole[x][y] = 2
                    white_count -= 1
                    vivod(-1, -1)

            vozm_ch_zabrat = False
            chernie_proverka()
            if vozm_ch_zabrat == False and vozm_ch_d_zabrat == False:
                hod_igroka = True
        chernie_proverka()
        vozmozhnost_chernih_hodit(x, y)
        if black_count == 0:
            messagebox.showinfo(title='Победа белых', message='Победили белые.', icon='info')
            hod_igroka = None
            Start_new()
        if vozmozhnost_chernih_shodit:
            if pole[prev_ch_coord_x][prev_ch_coord_y] != 0 and ((prev_ch_coord_y == y + 1 and prev_ch_coord_x == x - 1) or (prev_ch_coord_y == y - 1 and prev_ch_coord_x == x - 1)):  # Проверяем, сходили ли мы на одну клетку вертикально или горизонтально
                vivod(-1, -1)
                if pole[x][y] == 0 and vozm_ch_zabrat == False and vozm_ch_d_zabrat == False:
                    if pole[prev_ch_coord_x][prev_ch_coord_y] == 2:
                        if x == 8:
                            pole[x][y] = 4
                        else:
                            pole[x][y] = 2
                        pole[prev_ch_coord_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)  # рисуем игровое поле
                        hod_igroka = True
            if pole[prev_ch_coord_x][prev_ch_coord_y] == 4 and pole[x][
                y] == 0 and vozm_ch_zabrat == False and vozm_ch_d_zabrat == False:  # ходы для белой дамки
                if prev_ch_coord_x > x and prev_ch_coord_y > y and (prev_ch_coord_x - prev_ch_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(prev_ch_coord_x - x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x -= 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        hod_igroka = True

                if prev_ch_coord_x > x and prev_ch_coord_y < y and (prev_ch_coord_x + prev_ch_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(prev_ch_coord_x - x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x -= 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        hod_igroka = True
                if prev_ch_coord_x < x and prev_ch_coord_y > y and (prev_ch_coord_x + prev_ch_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(x - prev_ch_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x += 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        hod_igroka = True
                if prev_ch_coord_x < x and prev_ch_coord_y < y and (prev_ch_coord_x - prev_ch_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(x - prev_ch_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x += 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        hod_igroka = True


izobrazheniya_figur()  # здесь загружаем изображения пешек
novaya_igra()  # начинаем новую игру
vivod(-1, -1)  # рисуем игровое поле
board.bind("<Button-1>", click_event)  # нажатие левой кнопки

mainloop()
