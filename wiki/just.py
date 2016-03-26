#!/usr/bin/python3

import os
import sys
import math

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
            (n, _nlinks) = (map(int, f.readline().split()))
            
            self._titles = []  # список названий статей
            self._sizes = array.array('L', [0]*n) # список с размерами i-ой статьи
            self._links = array.array('L', [0]*_nlinks) # список список ссылок на статьи - метод Compressed Sparse Row
            self._redirect = array.array('B', [0]*n) # флаг перенаправления 
            self._offset = array.array('L', [0]*(n+1)) #  в i-ой ячейке содержится информация с какого номера начинаются ссылки в self._links  для i-й статьи
            current_link = 0
            for i in range(n):
                __title = f.readline()
                self._titles.append(__title.rstrip())
                (size, redirect, amout_links) = (map(int, f.readline().split()))
                self._sizes[i] = size
                self._redirect[i] = redirect
                for j in range(current_link, current_link + amout_links):
                    self._links[j] = int(f.readline())
                current_link += amout_links
                if n > 0:
                    self._offset[i+1] = self._offset[i] + amout_links

        print('Граф загружен')
        

  

    def get_id(self, title):
        _id = 0
        for name in self._titles:
            if name == title:
                return int(_id)
                 
            else:
                 _id += 1
    def get_number_of_links(self, _id):
        return int(self._offset[_id+1] - self._offset[_id]) 
                    
    def get_links_from(self, _id):
        return [ self._titles[i]for i in range(self._offset[_id],self._offset[_id+1]) ]
    def get_number_of_pages(self):
        return len(self._titles)

    def is_redirect(self, _id):
        if self._redirect[_id]:
            return True
        else:
            return False
            
    def get_title(self, _id):
        return self.title[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]
              
G=WikiGraph()    
G.load_from_file('wiki_small.txt')        


print(G.get_number_of_pages())

