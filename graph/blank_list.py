'''считывает кол-во ребер и список ребер. Граф ненаправленный'''


'''this function transform coh_list (list of edges) to adjacency list called (adj_list in function) '''
def transform(coh_list, adj_list = {}):
   for elem in coh_list:
      if elem[0] not in adj_list:
         adj_list[elem[0]] = {elem[1]}
         adj_list[elem[0]] = {elem[1]}
      else:
         adj_list[elem[0]].add(elem[1])
      if elem[1] not in adj_list:
         adj_list[elem[1]] = {elem[0]}
         adj_list[elem[1]] = {elem[0]}
      else:
         adj_list[elem[1]].add(elem[0])
   return adj_list
   

       
         
