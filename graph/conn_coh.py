import networkx as nx
import matplotlib.pyplot as plt
from blank_list import *

'''кол-во компонет связанности в графе'''

f = open('conn_coh', 'r')
'''ввод графа в виде списка ребер'''
coh_list = []
coh_list = [ line.split() for line in f ] 

    
adj_list = transform(coh_list)


connected_coh = 0

'''cписок посещенных вершнин'''
tree = []
visited = {}
for elem in coh_list:
     visited[elem[0]] = False
     visited[elem[1]] = False
     
'''обход в глубину
функция принимает в качестве начальных параметров список смжености и начальную вершину''' 
     
def dfs(vertex):
    visited[vertex] = True
    connected_component_dict[vertex] = key
    for w_vertex in adj_list[vertex]:
        
         if not visited[w_vertex]:
              
              dfs(w_vertex) 
           

connected_component_dict = { vertex: None for vertex in adj_list}

key = 0 #используется для присваивания номера компаненте связанности
for vertex in connected_component_dict:
  
   if not connected_component_dict[vertex]:
       key += 1
       dfs(vertex)  

color = { 1: 'red',
           2:'green',
           3: 'yellow',
           4: 'blue', 
           5:'pink' }    


f.close()

'''создаем граф  через networkx'''

G = nx.Graph()
G.add_nodes_from(tree)
G.add_edges_from(coh_list)
pos=nx.spring_layout(G,iterations=10)


nx.draw_networkx_edges(G, pos, width=1,alpha=1, edge_color='black')

for vertex in connected_component_dict:
     nx.draw_networkx_nodes(G,pos,
                       nodelist=[vertex],
                       node_color=color[connected_component_dict[vertex]],
                       node_size=400,
                       alpha=0.8)

labels = {}
for elem in adj_list:
    labels[elem] = elem
nx.draw_networkx_labels(G, pos,labels)

plt.show()

