from tkinter import *
import random
from pygame import mixer

def play(sound_file):
    mysound = tkSnack.Sound()
    mysound.read(sound_file)
    mysound.play()

# матрицы для отрисовки клеток (cell); живые и мертвых клетках (live) - живая клетка 1, мертвая 0; 
cell = [[0 for row in range(61)] for col in range(81)]
live = [[0 for row in range(61)] for col in range(81)]
new_generation = [[0 for row in range(61)] for col in range(81)]


# загружаем начальные данные
def load_from_file():
   
    f = open('map.txt', 'r')
    for y in range(60):
        line = f.readline()
        line =line.strip()
        for x in range(80):
              live[x][y] = int(line[x])
              cell[x][y] = canvas.create_oval((x*10, y*10, x*10+10, y*10+10), outline="gray", fill="black")  
    f.close()
   
   
            
          
def statystic():
    return live == new_generation

''' функция создает новое поколение клеток исходя из расположения старых в live. После чего проверяет на статичность (произошли какие либо изменения или нет - если нет, то выходит из программы). После live превращается в новое поколение '''
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

''' функция считает кол-во живых соседей :) '''
def live_neighbors(a,b):
    lives = 0
    for i in range(-1,2):
        for j in range(-1,2):
           if a+i > -1 and a+i < 80 and b+j > -1 and b+j < 60:
            
             if  i==0 and j==0:
                 pass
               
             elif live[a+i][b+j] == 1: lives += 1
    return lives         

'''функция рисует живые и мертвые клатки. Живые - зеленые; мертвые - черным. ''' 
def draw():
    for y in range(60):
        for x in range(80):
            if live[x][y]==0:
                canvas.itemconfig(cell[x][y], fill="black")
            if live[x][y]==1:
                canvas.itemconfig(cell[x][y], fill="green")



def step():
    process()
    draw()
    root.after(10, step)

def music():
     mixer.init(10000)
     m = mixer.Sound('sound.wav')
     m.play()
     
root = Tk()
root.title("Conway's Game of Life")
music()
canvas = Canvas(root, width=800, height=600, highlightthickness=0, bd=10, bg='black') # создаем холст
canvas.pack() # отображаем его на экране
load_from_file() # загружаем начальные данные 
step()  # вызываем step, вызывающий сам себя ;) 
root.mainloop()
