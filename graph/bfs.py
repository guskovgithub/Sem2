import networkx as nx
import matplotlib.pyplot as plt
from blank_list import *





f = open('conn_coh', 'r')
'''ввод графа в виде списка ребер'''
coh_list = []
coh_list = [ line.split() for line in f ]
adj_list = transform(coh_list)


tree = []
edges_of_tree = []
'''cписок посещенных вершнин'''
visited = {}
for elem in coh_list:
     visited[elem[0]] = False
     visited[elem[1]] = False
     
'''обход в глубину'''      
def bfs(vertex, queue = {} ):
   visited[vertex] = True
   tree.append(vertex)
   queue = [vertex]
   while queue:
        current = queue.pop(0)
        
        for neighbour in adj_list[current]:
          
           if not visited[neighbour]:
              edges_of_tree.append((current, neighbour))
              visited[neighbour] = True
              queue.append(neighbour)
              tree.append(neighbour)
              



start_vertex = input('введите начальную вершину ')
bfs(start_vertex)
print('Дерево в ширину:', tree)

'''создаем граф  через networkx'''


'''создаем граф  через networkx'''
G = nx.Graph()
G.add_nodes_from(tree)
G.add_edges_from(coh_list)


pos = nx.spring_layout(G) 
nx.draw_networkx_edges(G, pos, width=1,alpha=1,edge_color='black')

nx.draw_networkx_edges(G,pos,
                       edgelist=edges_of_tree,
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
