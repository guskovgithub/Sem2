import networkx as nx
import matplotlib.pyplot as plt
from blank_list import *

G = nx.Graph()


'''ввод графа в виде списка ребер'''
f = open('vertex_with_wight', 'r')
'''ввод графа в виде списка ребер'''
coh_list = []
coh_list = [ line.split() for line in f ]
adj_list = transform_with_wight(coh_list)


def dejkstra(adj_list, start_vertex):
     shortest_path = {vertex: float('inf') for vertex in adj_list}
     shortest_path[start_vertex] = 0
     queue = [start_vertex]
     while queue:
            current = queue.pop(0)
            for neighbour in adj_list[current]:
               if  shortest_path[current] + adj_list[current][neighbour] < shortest_path[neighbour]:
                   shortest_path[neighbour] = shortest_path[current] + adj_list[current][neighbour]
                   queue.append(neighbour)
     return shortest_path       
     
     
     
start_vertex = input('кратчайшее введите начальную вершину  ')                 
shortest_path = dejkstra(adj_list, start_vertex)
for vertex in adj_list:
    print('растояние от', start_vertex,' до ', vertex,' равно ', shortest_path[vertex] )

