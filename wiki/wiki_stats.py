#!/usr/bin/python3

import os
import sys
import math
import numpy as np
import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt
 

class WikiGraph:
    '''функция load_from_file загружает граф из файла'''
    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            (self.n, self._nlinks) = (map(int, f.readline().split()))
            
            self._titles = []  # список названий статей
            self._sizes = array.array('L', [0]*self.n) # список с размерами i-ой статьи
            self._links = array.array('L', [0]*self._nlinks) #список ссылок на статьи - метод Compressed Sparse Row
            self._redirect = array.array('B', [0]*self.n) # флаг перенаправления 
            self._offset = array.array('L', [0]*(self.n+1)) #  в i-ой ячейке содержится информация с какого номера начинаются ссылки в self._links  для i-й статьи
            current_link = 0
            for i in range(self.n):
                __title = f.readline()
                self._titles.append(__title.rstrip())
                (size, redirect, amout_links) = (map(int, f.readline().split()))
                self._sizes[i] = size
                self._redirect[i] = redirect
                for j in range(current_link, current_link + amout_links):
                    self._links[j] = int(f.readline())
                current_link += amout_links
                if self.n > 0:
                    self._offset[i+1] = self._offset[i] + amout_links

        print('Граф загружен')
        

  

    def get_id(self, title):
        _id = 0
        for name in self._titles:
            if name == title:
                return int(_id)
                 
            else:
                 _id += 1
    def get_number_of_links_from(self, _id):
        return int(self._offset[_id+1] - self._offset[_id]) 
                    
    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]
        
    def get_number_of_pages(self):
        return len(self._titles)

    def is_redirect(self, _id):
        if self._redirect[_id]:
            return True
        else:
            return False
            
    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]
        
'''третье упражнение из задания на judje_mipt'''
def task_3_from_Hiryanov(self):
      f = open('task_3_from_Hiryanov.txt', 'w')
      
      '''внутренний анализ статей'''
      '''зададим необходимые переменные'''
      redirected_titels = 0
      min_number_of_links = self.get_number_of_links_from(1)
      max_number_of_links = 0
      amount_of_pages_with_min_number_of_links = 0   
      amount_of_pages_with_max_number_of_links = 0 
      list_of_articels_with_max_links = ''
      
      '''циклы'''   
      for i in range(self.get_number_of_pages()):
           if self.is_redirect(i):
               redirected_titels += 1
           if  self.get_number_of_links_from(i) < min_number_of_links:
               min_number_of_links =  self.get_number_of_links_from(i)
           if  self.get_number_of_links_from(i) > max_number_of_links:
               max_number_of_links = self.get_number_of_links_from(i)
               
               
      for i in  range(self.get_number_of_pages()):
           if self.get_number_of_links_from(i) == min_number_of_links:
                amount_of_pages_with_min_number_of_links  += 1
           if self.get_number_of_links_from(i) == max_number_of_links:
                amount_of_pages_with_max_number_of_links +=1
                list_of_articels_with_max_links += str(self._titles[i])     
      
      '''внешний анализ статей'''
      num_of_links_to_page = [0 for i in range(G.get_number_of_pages())]
      for i in range(G.get_number_of_pages()): # пробегаемся по каждой статье
          for elem in G.get_links_from(i): # смотрим на какие статьи ссылается i-я статья, и к этим статьям добавляем +1 к количеству ссылок на них
                      
             num_of_links_to_page[int(elem)] += 1
             if G.is_redirect(i):
                  num_of_links_to_page[int(elem)] -= 1
                  
      pages_with_max_num_of_to_links = [G.get_title(i) for i in range(G.get_number_of_pages()) if num_of_links_to_page[i] == max(num_of_links_to_page)]  
      
      ''' анализ перенаправлений'''
      redirects_to_page = [0 for i in range(G.get_number_of_pages())]
      for i in range(G.get_number_of_pages()):
          for elem in G.get_links_from(i):
               if G.is_redirect(i) == 1:
                   redirects_to_page[elem] += 1
      pages_with_max_num_of_redirects  = [G.get_title(i) for i in range(G.get_number_of_pages()) if redirects_to_page[i] == max(redirects_to_page) ]
      
      '''путь '''
      way = bfs(G, 'Python','Список_файловых_систем')
      way = [G.get_title(way[i]) for i in range(len(way)) ]
    
      
              
                 
      f.write('количество статей с перенаправлением: ' + str(redirected_titels) + '\n' +
              'минимальное количество ссылок из статьи: ' + str(min_number_of_links) + '\n' +
              'количество статей с минимальным количеством ссылок: ' + str(amount_of_pages_with_min_number_of_links) + '\n' + 
              'максимальное количество ссылок из статьи: ' + str(max_number_of_links) + '\n' +
               'количество статей с максимальным количеством ссылок: ' + str(amount_of_pages_with_max_number_of_links) + '\n' +
               'cтатьи с наибольшим количеством ссылок: '+ list_of_articels_with_max_links + '\n' + 
               'среднее количество ссылок в статье: ' + str(round(self._nlinks / self.n)) + '\n'  +
               'Минимальное количество ссылок на статью: ' + str(min(num_of_links_to_page)) + '\n'  +
                'Количество статей с минимальным количеством внешних ссылок: ' + str(sum(elem == min(num_of_links_to_page) for elem in num_of_links_to_page )) + '\n' + 
                'Максимальное количество ссылок на статью: ' + str(max(num_of_links_to_page)) + '\n'  +
                'Количество статей с максимальным количеством внешних ссылок: ' + str(sum(elem == max(num_of_links_to_page) for elem in num_of_links_to_page )) + '\n' +
                'Статья с наибольшим количеством внешних ссылок' + str(pages_with_max_num_of_to_links) + '\n' + 
                "Среднее количество внешних ссылок на статью: %0.2f  (ср. откл. : %0.2f)" %(statistics.mean(num_of_links_to_page), statistics.stdev(num_of_links_to_page)) + '\n' + 
                'Минимальное количество перенаправлений на статью: ' + str(min(redirects_to_page)) + '\n' +
                'Количество статей с минимальным количеством внешних перенаправлений: ' + str(sum(elem == min(redirects_to_page) for elem in redirects_to_page)) + '\n' + 
                'Максимальное количество перенаправлений на статью: ' + str(max(redirects_to_page)) + '\n'  +
                'Количество статей с максимальным количеством внешних перенаправлений: ' + str(sum(elem == max(redirects_to_page) for elem in redirects_to_page)) + '\n' + 
                'Статья с наибольшим количеством внешних перенаправлений:' + str(pages_with_max_num_of_redirects)  + '\n' + 
                "Среднее количество внешних перенаправлений на статью: %0.2f  (ср. откл. : %0.2f)" %(statistics.mean(redirects_to_page), statistics.stdev(redirects_to_page)) + '\n' + 
                'путь, по которому можно добраться от статьи Python до статьи Список_файловых_систем: ' + str(way) )


#отдельно оформим функицию обхода в ширину
def bfs(G, start, finish):  
    start, finish = G.get_id(start), G.get_id(finish)          
    path = []
    queue = [start]
    while queue:
          current = queue.pop(0)
          if current == finish:
                   break
          if current not in path:
               path.append(current)
               queue = queue + list(G.get_links_from(current))
              
    return path       
    

                   
         

def hist(objects, data,  xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    
    y_pos = np.arange(len(objects))
    plt.bar(y_pos, data, align='center', alpha=0.5)
    plt.xticks(y_pos, [i for i in range(G.get_number_of_pages())])
    plt.ylabel(ylabel)
    
    plt.xlabel(xlabel)
    plt.title(title)
    plt.plot()
    

'''создадим граф под названием G '''         
G=WikiGraph()    
G.load_from_file('wiki_small.txt')        
'''запустим функцию 3-го задания'''
task_3_from_Hiryanov(G)
'''задание 4 - гистограммы'''
dict_amount_of_links_from_page = {}
for i in range (G.get_number_of_pages()):
   if not G.get_number_of_links_from(i) in dict_amount_of_links_from_page:
         dict_amount_of_links_from_page[G.get_number_of_links_from(i)] = 1
   else:
         dict_amount_of_links_from_page[G.get_number_of_links_from(i)] += 1
plt.figure(1)
plt.subplot(211)
#hist(dict_amount_of_links_from_page,[i for i in dict_amount_of_links_from_page ], 'кол-во ссылок', 'кол-во статей ','распределение количества ссылок из статьи')  # распределение количества ссылок из статьи
plt.subplot(212)
#hist(G._titles, [G.get_page_size(i) for  i in range(G.get_number_of_pages()) ], 'статьи', 'размер  ','распределение размеров статей')  # распределение размеров статей
#hist(G._titles, [math.log(G.get_page_size(i)) for  i in range(G.get_number_of_pages()) ], 'статьи', 'ln(размер)  ','распределение размеров статей в логарифмческом масштабе')  # распределение размеров статей в логарифмческом масштабе
plt.show()
if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)
    hist(G._titles, [get_numer_of_links_from(i) for  i in range(self.get_number_of_pages()) ], 'статьи', 'кол-во ссылок ','распределение количества ссылок из статьи')     
        

    # TODO: статистика и гистограммы
