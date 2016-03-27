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

     
     
     
     
start_vertex = input('введите начальную вершину ') 
finish_vertex = input('введите конечную вершину ')                 
shortest_path = dejkstra(adj_list, start_vertex)

way  = [finish_vertex]    
current = finish_vertex
while current != start_vertex:
       for vertex in adj_list[current]:
         if current != start_vertex:
    
             if shortest_path[current] - adj_list[current][vertex] == shortest_path[vertex]:
                current = vertex
                way.append(current) 
         else:
             break  
                       
edges_way = [(way[i],way[i+1]) for i  in range(len(way)-1) ]
coh_list_without_weight = [(elem[0],elem[1]) for elem in coh_list]

'''создаем граф  через networkx'''
G = nx.Graph()
G.add_nodes_from(adj_list)
G.add_edges_from(coh_list_without_weight)

pos=nx.spring_layout(G,iterations=5)
nx.draw_networkx_edges(G, pos, width=1,alpha=1,edge_color='black')

nx.draw_networkx_edges(G,pos,
                       edgelist=edges_way,
                       width=10,alpha=0.8,edge_color='blue')

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_nodes(G,pos,
                       nodelist=[start_vertex, finish_vertex],
                       node_color='green',
                       node_size=500,
                   alpha=1, label = 'start')
nx.draw_networkx_nodes(G,pos,
                       nodelist=way,
                       node_color='pink',
                       node_size=500,
                   alpha=0.5, label = 'start')                   
labels = {}
for elem in adj_list:
    labels[elem] = elem
nx.draw_networkx_labels(G, pos,labels)
                       
nx.draw_networkx_edge_labels(G, pos)

plt.show()
