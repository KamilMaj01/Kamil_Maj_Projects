import cv2

from graf_mst import graf
import numpy as np
import matplotlib.pyplot as plt

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

        (self.graf_list[idxa])[idxb] = weight
        (self.graf_list[idxb])[idxa] = weight


       

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
        obj = [ (self.getVertex(key),edge)for key, edge in self.graf_list[vertex_idx].items()]
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
                graf.append((self.help_list[idx_i],self.help_list[j], i[j]))
        return graf
    

def primMST(g: Graf_list):
    intree = [0 for _ in range(g.order())]
    distance = [float('inf') for _ in range(g.order())]
    parents = [-1 for _ in range(g.order())]

    Sub_ListGraf = Graf_list()
    for i in range(g.order()):
        Sub_ListGraf.insertVertex(g.getVertex(i))

    v = 0
    while intree[v] == 0:
        intree[v] = 1     
        neighbours  = g.neighbours(v)
        for el_node, weight in neighbours:  
            index_neighbour = g.getVertexIdx(el_node)
            if intree[index_neighbour] == 0 and distance[index_neighbour] > weight:
                distance[index_neighbour] = weight
                parents[index_neighbour] = v
        
        min_value = float('inf')
        for idx_node, new_value in enumerate(distance):
            if intree[idx_node] == 0 and new_value < min_value:
                min_value = new_value
                idx_new_node = idx_node

        if idx_new_node == v:
            min_value = distance[v]
        parent_node = g.getVertex(parents[idx_new_node])
        
        current_node = g.getVertex(idx_new_node)
        Sub_ListGraf.insertEdge(current_node, parent_node, min_value)
        v = idx_new_node
    total_sum = sum(distance[1:])
    return Sub_ListGraf, total_sum
        
def DFS(G : Graf_list, Vertex: Node, color):
    visited = [Vertex]
    visited[-1].set_color(color)
    stos = [Vertex]
    while len(stos) !=  0:
        node = stos.pop()
        for neighbour, _ in G.neighbours(G.getVertexIdx(node)):
            if neighbour not in visited:
                stos.append(neighbour)
                visited.append(neighbour)
                visited[-1].set_color(color)
    
    return visited



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


def main():
    Graf = Graf_list()
    
    I = cv2.imread('sample.png',cv2.IMREAD_GRAYSCALE)

    (Y,X) = I.shape

    
    for i in range(1,Y-1):
        for j in range(1,X-1):
            window = I[i-1:i+2,j-1:j+2]
            gray_scale = I[i,j]
            for idx_i, i_window in enumerate(window):
                for idx_j, j_window in enumerate(i_window):
                    if idx_i != 1 or idx_j !=1:
                        Graf.insertEdge(Node(X*(j+(idx_j-1)) + (i+(idx_i-1))),Node(X*j+i),weight = abs(int(j_window) - int(gray_scale)))

    MST_Graf = primMST(Graf)
    edges = MST_Graf[0].edges()

    sorted_edge = sorted(edges,reverse= True,key=lambda el: el[2])

    MST_Graf[0].deleteEdge(sorted_edge[0][0], sorted_edge[0][1])

    IS = np.zeros((Y,X), dtype= np.uint8)

    first = DFS(MST_Graf[0],sorted_edge[0][0], 100)
    second = DFS(MST_Graf[0],sorted_edge[0][1], 200)

    for node in first:
        y = node.get_key()//X
        x = node.get_key()%X
        IS[x,y] = node.get_color()

    for node in second:
        y = node.get_key()//X
        x = node.get_key()%X
        IS[x,y] = node.get_color()


    cv2.imshow("wynik", IS)
    cv2.waitKey()   

    # plt.imshow(IS,'gray',vmin = 0, vmax= 255)
    # plt.show()


main()

