import networkx as nx
import matplotlib.pyplot as plt
from blank_list import *

G = nx.Graph()


'''ввод графа в виде списка ребер'''
N = int(input()) # number of edges
coh_list = [ input().split() for i in range(N) ] #takes edge and its  weight
adj_list = transform(coh_list)


tree = []
'''cписок посещенных вершнин'''
visited = {}
for elem in coh_list:
     visited[elem[0]] = False
     visited[elem[1]] = False
     
'''обход в глубину'''      
def dfs(vertex):
    visited[vertex] = True
    tree.append(vertex)
    print(visited)
    for w_vertex in adj_list[vertex]:
        if not visited[w_vertex]:
           dfs(w_vertex) 



dfs(coh_list[0][0])
print('Дерево в глубину:', tree)

'''создаем граф  через networkx'''
G.add_nodes_from(tree)
G.add_edges_from(coh_list)
nx.draw_circular(G)
plt.savefig('circular_tree.png')
plt.show()

