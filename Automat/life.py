from tkinter import *

import random
import time

# матрицы для отрисовки клеток (cell); живые и мертвых клетках (live) - живая клетка 1, мертвая 0; 
cell = [[0 for row in range(61)] for col in range(81)]

live = [[0 for row in range(61)] for col in range(81)]
new_generation = [[0 for row in range(61)] for col in range(81)]

# загружаем начальные данные
'''
вариант загрузки НЕ из файла

def load():
    for y in range(-1,61):
        for x in range(-1,81):
            live[x][y] = 0
            new_generation[x][y] = 0
            cell[x][y] = canvas.create_oval((x*10, y*10, x*10+10, y*10+10), outline="gray", fill="black")

    # карабль
    live[11][10] = 1
    live[12][11] = 1
    live[10][12] = 1
    live[11][12] = 1
    live[12][12] = 1

    # осциллятор 
    live[31][30] = 1
    live[32][31] = 0
    live[30][32] = 1
    live[31][32] = 1
    live[32][32] = 1
'''
def load_from_file():
   
    f = open('map.txt', 'r')
    for y in range(60):
        line = f.readline()
        line =line.strip()
        for x in range(80):
              live[x][y] = int(line[x])
              new_generation[x][y] = 0
              cell[x][y] = canvas.create_oval((x*10, y*10, x*10+10, y*10+10), outline="gray", fill="black")  
    f.close()
   
   
            
          
def statystic():
    return live == new_generation

# Правила жизни
def process():
    for y in range(0,60):
        for x in range(0,80):
            lives = live_neighbors(x,y)
            '''Правила игры:
                   * в мёртвой клетке зарождается жизнь, если у этой клетки ровно три живых соседних клетки;
                   * если у живой клетки есть две или три живых соседних клетки, то клетка продолжает жить, в противном случае клетка погибает. '''
            if live[x][y] == 1 and (lives < 2 or lives > 3): new_generation[x][y] = 0
            if live[x][y] == 1 and (lives == 2 or lives == 3): new_generation[x][y] = 1
            if live[x][y] == 0 and lives == 3: new_generation[x][y] = 1
    ''' cмена поколения '''   
    if statystic(): exit()
    for y in range(60):
        for x in range(80):
            live[x][y] = new_generation[x][y]

# Посчитаем кол-во живых соседей :)
def live_neighbors(a,b):
    lives = 0
    for i in range(-1,2):
        for j in range(-1,2):
           if a+i > -1 and a+i < 80 and b+i > -1 and b+i < 60:
            
             if  i==0 and j==0:
                 pass
               
             elif live[a+i][b+j] == 1: lives += 1
    return lives         

# Рисуем живые и мертвые клатки. Живые - зеленые; мертвые - черным. 
def draw():
    for y in range(60):
        for x in range(80):
            if live[x][y]==0:
                canvas.itemconfig(cell[x][y], fill="black")
            if live[x][y]==1:
                canvas.itemconfig(cell[x][y], fill="green")


# process and draw the next frame
def step():
    process()
    draw()
    root.after(10, step)


root = Tk()
root.title("Conway's Game of Life")
canvas = Canvas(root, width=800, height=600, highlightthickness=0, bd=10, bg='black') # создаем холст
canvas.pack() # отображаем его на экране
#load() # загружаем начальные данные 
load_from_file()
step()  # вызываем step, вызывающий сам себя ;) 
root.mainloop()
