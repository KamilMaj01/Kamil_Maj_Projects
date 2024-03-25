import numpy as np


class Node:
    def __init__(self, key, color = None) -> None:
        self.__key = key
        self.__color = color

    def __eq__(self, other) -> bool:
        return self.__key == other.__key

    def __hash__(self):
        return hash(self.__key)
    
    def __repr__(self):
        return f'{self.__key}'
    
    def get_key(self):
        return self.__key
    
    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

class Graf_list:
    def __init__(self) -> None:
        self.graf_list = None
        self.help_list = []
        self.help_dict = {}


    def is_empty(self):
        return len(self.help_list) == 0

    def insertVertex(self, vertex):
        if vertex in self.help_list:
            return None
        if self.is_empty():
            self.help_list.append(vertex)
            self.help_dict[vertex] = 0
            self.graf_list = [{}]
        
        else:
            self.help_list.append(vertex)
            self.help_dict[vertex] = len(self.help_list) -1
            self.graf_list.append({})




    def insertEdge(self,vertex1, vertex2, weight):
        self.insertVertex(vertex1)
        self.insertVertex(vertex2)

        if self.is_empty():
            return None
        idxa = self.getVertexIdx(vertex1)
        idxb = self.getVertexIdx(vertex2)

        if idxb in self.graf_list[idxa].keys():
            weight = [self.graf_list[idxa][idxb], weight]
        (self.graf_list[idxa])[idxb] = weight

       

    def deleteVertex(self, vertex):
        if self.is_empty():
            return None
        idx = self.help_dict.pop(vertex)
        self.help_list.pop(idx)
        self.graf_list.pop(idx)

        for idx, el in enumerate(self.help_list):
            self.help_dict[el] = idx
        
        for idx_el, el in enumerate(self.graf_list):
            if idx in el:
                el.pop(idx)
            self.graf_list[idx_el] = {(index - 1) if index > idx else index : value for index, value in el.items()}
    
    
    def deleteEdge(self, vertex1, vertex2):
        if self.is_empty():
            return None
        
        idxa = self.getVertexIdx(vertex1)
        idxb = self.getVertexIdx(vertex2)

        (self.graf_list[idxa]).pop(idxb)
        (self.graf_list[idxb]).pop(idxa)
        


    def getVertexIdx(self, vertex):
        if self.is_empty():
            return None
        return self.help_dict[vertex]

    def getVertex(self, vertex_idx):
        return self.help_list[vertex_idx]

    def neighboursIdx(self, vertex_idx):
        return list((self.graf_list[vertex_idx]).keys())

    def neighbours(self, vertex_idx):
        obj = []
        for key, edge in self.graf_list[vertex_idx].items():
            if isinstance(edge,list):
                for el in edge:
                    obj.append((self.getVertex(key),el))
            else:
                obj.append((self.getVertex(key),edge))
        return obj
    

    def order(self):
        return len(self.help_list)

    def size(self):
        if self.is_empty():
            return 0
        size = sum([len(node) for node in self.graf_list])
        return size

    def edges(self):
        graf = []
        for idx_i, i in enumerate(self.graf_list):
            for j in i.keys():
                graf.append((self.help_list[idx_i].get_key(),self.help_list[j].get_key()))
        return graf
    
    def getEdge(self, vertex1_idx, vertex2_idx):
        return self.graf_list[vertex1_idx][vertex2_idx]
    

def printGraph(g: Graf_list):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(j, w, end=";")
        print()
    print("-------------------")


class Edge:
    def __init__(self, capacity, isResidual = "rzeczywista") -> None:
        self.isResidual = isResidual
        self.capacity = capacity
        if isResidual == "rzeczywista":
            self.Residual = capacity
            self.flow = 0
        elif isResidual == "resztowy":
            self.Residual = 0
            self.flow = None
    
    def getIsResidual(self):
        return True if self.isResidual == "resztowy" else False
    
    def getResidual(self):
        return self.Residual

    def __repr__(self) -> str:
        return f'{self.capacity}, {self.Residual}, True' if self.isResidual == "resztowy" else f'{self.capacity}, {self.flow}, {self.Residual}, False'



def insertEdgeForda(g:Graf_list,vertex1,vertex2,weight):
    weight_first = Edge(weight)
    weight_second = Edge(weight,isResidual= "resztowy")

    g.insertEdge(vertex1,vertex2,weight_first)
    g.insertEdge(vertex2,vertex1,weight_second)

def BFS(G :Graf_list, idx_first = 0):
    n = G.order()
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    kolejka = []

    idx = idx_first

    kolejka.append(idx)
    visited[idx] = True
    while len(kolejka) != 0:
        elem = kolejka.pop()
        neighbours = G.neighbours(elem)
        neighbours = sorted(neighbours, key = lambda el: el[1].Residual)
        for neighbour, weight in neighbours:
            idx_neighbour = G.getVertexIdx(neighbour)
            if not visited[idx_neighbour] and weight.Residual > 0 :
                if not weight.getIsResidual():
                    kolejka.append(idx_neighbour)
                    visited[idx_neighbour] = True
                    parent[idx_neighbour] = elem

    return parent


def analyse_path(G : Graf_list, start_vertex_idx, end_vertex_idx, parent_list : list ):
    current_idx =  end_vertex_idx
    min_capacity = float('inf')

    if parent_list[end_vertex_idx] is None:
        return 0
    
    while current_idx != start_vertex_idx:
        parent_idx = parent_list[current_idx]
        edge : Edge = G.getEdge(parent_idx, current_idx)
        if isinstance(edge, list):
            for el in edge:
                if not el.getIsResidual():
                    edge = el
        else:
            if edge.getIsResidual():
                edge : Edge = G.getEdge(current_idx, parent_idx)

        residual = edge.getResidual()
        if residual < min_capacity:
            min_capacity = residual

        current_idx = parent_idx
        

    return min_capacity


def augmente_path(G: Graf_list, start_vertex_idx, end_vertex_idx, parent_list : list, min_capacity ):
    current_idx =  end_vertex_idx

    if parent_list[end_vertex_idx] is None:
        return 0

    while current_idx != start_vertex_idx:
        parent_idx = parent_list[current_idx]

        edge : Edge = G.getEdge(current_idx, parent_idx)
        if isinstance(edge, list):
            for el in edge:
                if el.getIsResidual():
                    edge = el
        if edge.getIsResidual():
            edge.Residual += min_capacity
        edge : Edge = G.getEdge(parent_idx,current_idx)

        if isinstance(edge, list):
            for el in edge:
                if not el.getIsResidual():
                    edge = el
        if not edge.getIsResidual():
            edge.flow += min_capacity
            edge.Residual -= min_capacity
      
        current_idx = parent_idx



def Ford_Fulkerson(G : Graf_list, start_vertex, stop_vertex):
    s_idx :Node = G.getVertexIdx(start_vertex)
    t_idx :Node= G.getVertexIdx(stop_vertex)
    parent = BFS(G,s_idx)

    
    min_flow = analyse_path(G,s_idx,t_idx,parent)
    total_sum_flow = min_flow
    while min_flow > 0:
        augmente_path(G,s_idx,t_idx,parent,min_flow)
        parent = BFS(G,s_idx)
        min_flow = analyse_path(G,s_idx,t_idx,parent)
        total_sum_flow += min_flow
    return total_sum_flow


def Creation_garf(graf : list[tuple], start_key : str, stop_key : str):
    Graf = Graf_list()
    start_vertex = Node(start_key)
    stop_vertex = Node(stop_key)
    for key1, key2, weight in graf:
        if key1 == start_key:
            vertex1 = start_vertex
            vertex2 = Node(key2)
        elif key2 == start_key:
            vertex2 = start_vertex
            vertex1 = Node(key1)
        elif key1 == stop_key:
            vertex1 = stop_vertex
            vertex2 = Node(key2)
        elif key2 == stop_key:
            vertex2 = stop_vertex
            vertex1 = Node(key1)
        else:
            vertex1 = Node(key1)
            vertex2 = Node(key2)
        
        insertEdgeForda(Graf,vertex1, vertex2,weight)

    sum_flow = Ford_Fulkerson(Graf,start_vertex,stop_vertex)
    return Graf, sum_flow



def main():
    graf = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), ('d', 'c', 4)]

    Graf, sum_flow = Creation_garf(graf,'s','t')
    print(sum_flow)
    printGraph(Graf)

    Graf_1 , sum_flow_1 = Creation_garf(graf_1,'s','t')
    print(sum_flow_1)
    printGraph(Graf_1)

    Graf_2, sum_flow_2 = Creation_garf(graf_2,'s','t')
    print(sum_flow_2)
    printGraph(Graf_2)

    Graf_3, sum_flow_3 = Creation_garf(graf_3,'s','t')
    print(sum_flow_3)
    printGraph(Graf_3)

main()