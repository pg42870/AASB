# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:03:16 2021

@author: joana
"""

## Graph represented as adjacency list using a dictionary
## keys are vertices
## values of the dictionary represent the list of adjacent vertices of the key node
import numpy as np

class MyGraph_ex:
    
    def __init__(self, g = {}):
        ''' Constructor - takes dictionary to fill the graph as input; default is empty dictionary '''
        self.graph = g    

    def print_graph(self):
        ''' Prints the content of the graph as adjacency list '''
        for v in self.graph.keys():
            print (v, " -> ", self.graph[v])

    ## get basic info

    def get_nodes(self):
        ''' Returns list of nodes in the graph '''
        return list(self.graph.keys())
        
    def get_edges(self): 
        ''' Returns edges in the graph as a list of tuples (origin, destination) '''
        edges = []
        for v in self.graph.keys():
            for d in self.graph[v]:
                edges.append((v,d[0])) #porque d tem dois elementos o primeiro e' o destino e o segundo o peso
        return edges
      
    def size(self):
        ''' Returns size of the graph : number of nodes, number of edges '''
        return len(self.get_nodes()), len(self.get_edges())
      
    ## add nodes and edges    
    
    def add_vertex(self, v):
        ''' Add a vertex to the graph; tests if vertex exists not adding if it does '''
        if v not in self.graph.keys():
            self.graph[v]=[]
        return
            
        
    def add_peso(self, o, d,peso):
        ''' Add edge to the graph; if vertices do not exist, they are added to the graph ''' 
        if o not in self.graph.keys():
            self.add_vertex(o)
        if d not in self.graph.keys():
            self.add_vertex(d)
        if d not in self.graph[o]:
            self.graph[o].append((d,peso))
        pass



    ## successors, predecessors, adjacent nodes
        
    def get_successors(self, v):
        l= list(self.graph[v])     # needed to avoid list being overwritten of result of the function is used
        res= []
        for i in l:
            res.append(i[0]) #para aparecer apenas o destino e nao o destino e o peso
        return res
        
        
    def get_predecessors(self, v):
        pre = []
        for i in self.graph.keys():
            if v in self.graph[i][0]:
                pre.append(i)
        return pre
    
    def get_adjacents(self, v):
        suc = self.get_successors(v)
        pre = self.get_predecessors(v)
        res = pre
        for p in suc:
            if p not in res:
                res.append(p)
        return res
        
    ## degrees    
    
    def out_degree(self, v):
        return len(self.get_successors(v))
    
    
    def in_degree(self, v):
        return len(self.get_predecessors(v))
        
        
    def degree(self, v):
        return len(self.get_adjacents(v))
        
    
    ## BFS and DFS searches    
    
    def reachable_bfs(self, v):
        l = [v]
        res = []
        while len(l) > 0:
            node = l.pop(0)
            if node != v: res.append(node)
            for elem in self.graph[node]:
                if elem not in res and elem not in l and elem != node:
                    l.append(elem)
        return res
        
    def reachable_dfs(self, v):
        l = [v]
        res = []
        while len(l) > 0:
            node = l.pop(0)
            if node != v: res.append(node)
            s = 0
            for elem in self.graph[node]:
                if elem not in res and elem not in l:
                    l.insert(s, elem)
                    s += 1
        return res    
    
    def distance(self, s, d): #s 'e como se fosse o v
        if s == d: return 0
        l = [(s,0)]
        visited = [s]
        while len(l) > 0:
            node, dist = l.pop(0)
            for elem in self.graph[node]:
                if elem[0] == d:
                    return dist+elem[1]
                elif elem[0] not in visited:
                    l.append((elem[0],dist+elem[1]))
                    visited.append(elem[0])
        return None
        
    def shortest_path(self, s, d):
        if s == d: return [s,d]
        l = [(s,[],np.inf)]
        visited = [s]
        while len(l)>0:
            node, preds ,dist = l.pop(0)
            for elem in self.graph[node]:
                if elem[0] == d:
                    return preds+[node,elem[0]]
                elif elem not in visited:
                    l.append((elem[0],preds+[node],dist))
                    visited.append(elem[0])
        return None
        
    def reachable_with_dist(self, s):
        res = []
        l = [(s,0)]
        while len(l) > 0:
            node, dist = l.pop(0)
            if node != s: res.append((node,dist))
            for elem in self.graph[node]:
                if not is_in_tuple_list(l,elem[0]) and not is_in_tuple_list(res,elem[0]): 
                    l.append((elem[0],dist+1))
        return res

## cycles
    def node_has_cycle (self, v):
        l = [v]
        res = False
        visited = [v]
        while len(l) > 0:
            node = l.pop(0)
            for elem in self.graph[node]:
                if elem == v: return True
                elif elem not in visited:
                    l.append(elem)
                    visited.append(elem)
        return res

    def has_cycle(self):
        res = False
        for v in self.graph.keys():
            if self.node_has_cycle(v): return True
        return res


def is_in_tuple_list (tl, val):
    res = False
    for (x,y) in tl:
        if val == x: return True
    return res


def test1():
    gr = MyGraph_ex( {1:[(2,12)], 2:[(3,12)], 3:[(2,12),(4,15)], 4:[(2,9)]} )
    gr.print_graph()
    print (gr.get_nodes())
    print (gr.get_edges())
    

def test2():
    gr2 = MyGraph_ex()
    gr2.add_vertex(1)
    gr2.add_vertex(2)
    gr2.add_vertex(3)
    gr2.add_vertex(4)

    
    gr2.add_peso(1,2,12)
    gr2.add_peso(2,3,12)
    gr2.add_peso(3,2,4)
    gr2.add_peso(3,4,15)
    gr2.add_peso(4,2,9)
    
    gr2.print_graph()
  
def test3():
    gr = MyGraph_ex( {1:[(2,12)], 2:[(3,12)], 3:[(2,12),(4,15)], 4:[(2,9)]} )
    gr.print_graph()

    print (gr.get_successors(2))
    print (gr.get_predecessors(2))
    print (gr.get_adjacents(2))
    print (gr.in_degree(2))
    print (gr.out_degree(2))
    print (gr.degree(2))

def test4():
    gr = MyGraph_ex( {1:[(2,12)], 2:[(3,12)], 3:[(2,12),(4,15)], 4:[(2,9)]} )
    
    print (gr.distance(1,4))
    print (gr.distance(4,3))

    print (gr.shortest_path(1,4))
    print (gr.shortest_path(4,3))

    print (gr.reachable_with_dist(1))
    print (gr.reachable_with_dist(3))

    # gr2 = MyGraph_ex( {1:[2,3], 2:[4], 3:[5], 4:[], 5:[]} )
    
    # print (gr2.distance(2,1))
    # print (gr2.distance(1,5))
    
    # print (gr2.shortest_path(1,5))
    # print (gr2.shortest_path(2,1))

    # print (gr2.reachable_with_dist(1))
    # print (gr2.reachable_with_dist(5))

def test5():
    gr = MyGraph_ex( {1:[2], 2:[3], 3:[2,4], 4:[2]} )
    print (gr.node_has_cycle(2))
    print (gr. node_has_cycle(1))
    print (gr.has_cycle())

    gr2 = MyGraph_ex( {1:[2,3], 2:[4], 3:[5], 4:[], 5:[]} )
    print (gr2. node_has_cycle(1))
    print (gr2.has_cycle())


if __name__ == "__main__":
    
    #test1()
    #test2()
    #test3()
    test4()
    #test5()
