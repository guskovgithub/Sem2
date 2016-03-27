import networkx as nx
import matplotlib.pyplot as plt
from blank_list import *




f = open('conn_coh', 'r')
'''ввод графа в виде списка ребер'''
coh_list = []
coh_list = [ line.split() for line in f ]
adj_list = transform(coh_list)


tree = []
'''cписок посещенных вершнин'''
visited = {}
for elem in coh_list:
     visited[elem[0]] = False
     visited[elem[1]] = False
     
'''обход в глубину
функция принимает в качестве начальных параметров список смжености и начальную вершину'''      
def dfs(vertex):
    visited[vertex] = True
    tree.append(vertex)
    
    for w_vertex in adj_list[vertex]:
       
        if not visited[w_vertex]:
            
           listik.append((vertex, w_vertex))
           dfs(w_vertex) 

listik =[]
start_vertex = input('введите начальную вершину ')
dfs(start_vertex)

print('Дерево в глубину:', tree)

'''создаем граф  через networkx'''
G = nx.Graph()
G.add_nodes_from(tree)
G.add_edges_from(coh_list)

pos=nx.spring_layout(G,iterations=10)
nx.draw_networkx_edges(G, pos, width=1,alpha=1,edge_color='black')

nx.draw_networkx_edges(G,pos,
                       edgelist=listik,
                       width=10,alpha=0.5,edge_color='r')

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_nodes(G,pos,
                       nodelist=[start_vertex],
                       node_color='green',
                       node_size=500,
                   alpha=0.8, label = 'start')
labels = {}
for elem in adj_list:
    labels[elem] = elem
nx.draw_networkx_labels(G, pos,labels)

plt.show()

