import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
import math

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
    
    def set_key(self, new_key):
        self.__key = new_key
    
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


    def deleteVertex(self, vertex):
        if self.is_empty():
            return None

        idx_vertex = self.help_dict.pop(vertex)
        self.help_list.pop(idx_vertex)
        self.graf_list.pop(idx_vertex)

        for idx, el in enumerate(self.help_list):
            self.help_dict[el] = idx

        for idx_el, el in enumerate(self.graf_list):
            if idx_vertex in el.keys():
                self.graf_list[idx_el].pop(idx_vertex)
            self.graf_list[idx_el] = {(index - 1) if index > idx_vertex else index : value for index, value in el.items()}

    
    
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
                graf.append((self.help_list[idx_i],self.help_list[j], i[j]))
        return graf
    
    def getEdge(self, vertex1_idx, vertex2_idx):
        return self.graf_list[vertex1_idx][vertex2_idx]
    
    def plot_graph(self, v_color, e_color):
      for idx, v in enumerate(self.help_list):
            y, x = v.get_key()
            plt.scatter(x, y, c=v_color)
            for n_idx in self.neighboursIdx(idx):
                yn, xn = self.getVertex(n_idx).get_key()
                plt.plot([x, xn], [y, yn], color=e_color)

    def set_key_graph(self,node : Node, new_key):
        node.set_key(new_key)
        self.help_dict = {key : value for value, key in enumerate(self.help_list)}



    def rotation(self, vector_t,angle):
        x_t = vector_t[1]
        y_t = vector_t[0]

        for idx, el in enumerate(self.help_list):
            y, x = el.get_key()
            x_prim = ((x+x_t)*math.cos(angle) + (y+y_t)*math.sin(angle))
            if x_prim == 0:
                x_prim = 0.00000001
            y_prim = (-(x+x_t)*math.sin(angle) + (y + y_t)*math.cos(angle))
            if y_prim == 0:
                y_prim = 0.00000001
            self.set_key_graph(self.help_list[idx],(y_prim,x_prim))
        for i in range(self.order()):
            vertex = self.getVertex(i)
            y1, x1 = vertex.get_key()
            for node in self.neighbours(i):
                y2, x2 = node[0].get_key()
                iloczyn_skalarny = x2*x1 + y2*y1
                angle = np.arccos(iloczyn_skalarny/(np.sqrt(y1**2 + x1**2) * np.sqrt(y2**2 + x2**2)))
                distance = np.sqrt(np.power(y1 - y2, 2) + np.power(x1 - x2, 2))
                self.insertEdge(vertex, node[0], (distance, angle))

    

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

def fill_biometric_graph(img_bin : np.ndarray, graph : Graf_list):
    (Y,X) = img_bin.shape
    white = 255
    for i in range(Y):
        for j in range(X):
            if img_bin[i,j] == white:
                vertex = Node((i,j))
                graph.insertVertex(vertex)
                window = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1)]
                for el in window:
                    i_el, j_el = el
                    if img_bin[i_el,j_el] == white:
                        node = Node((i_el,j_el))
                        l = int(((j - j_el)**2 + (i-i_el)**2)**(1/2))
                        graph.insertEdge(vertex,node,(l,None))
                        graph.insertEdge(node,vertex,(l,None))


def unclutter_biometric_graph(graph : Graf_list):
    list_deletes = []
    list_adds = []
    n = graph.order()
    for idx_vertex in range(n):
        neigbours = graph.neighbours(idx_vertex)
        if len(neigbours) != 2:
            current_idx = idx_vertex
            for neighbour in neigbours:
                if neighbour[0] not in list_deletes:
                    prev_neighbour = current_idx
                    idx_neighbour = graph.getVertexIdx(neighbour[0])
                    list_neigbours = graph.neighbours(idx_neighbour)
                    
                    while len(list_neigbours) == 2:
                        list_deletes.append(graph.getVertex(idx_neighbour))
    
                        for el in list_neigbours:
                            next_neighbour = graph.getVertexIdx(el[0])
                            if next_neighbour != prev_neighbour:
                                prev_neighbour = idx_neighbour
                                idx_neighbour = next_neighbour
                                break
                        list_neigbours = graph.neighbours(idx_neighbour)
                    list_adds.append((graph.getVertex(current_idx), graph.getVertex(idx_neighbour)))

    for vertex in list_deletes:
        graph.deleteVertex(vertex)
        
    for nodes in list_adds:
        vertex1 , vertex2  = nodes
        y1,x1 = vertex1.get_key()
        y2,x2 = vertex2.get_key()
        l = int(((y1 - y2)**2 + (x1-x2)**2)**(1/2))
        iloczyn_skalarny = x2*x1 + y2*y1
        l1 = np.sqrt(x2**2 + y2**2)
        l2 = np.sqrt(x1**2 +  y1**2)
        angle = np.arccos(iloczyn_skalarny/( l1* l2))
        graph.insertEdge(vertex1,vertex2,(l,angle))
        graph.insertEdge(vertex2,vertex1,(l,angle))


def merge_near_vertices(graph : Graf_list, thr=5):
    list_list =[]
    n = graph.order()
    for i in range(n):
        current_verex : Node= graph.getVertex(i)
        add_list = [current_verex]
        Y,X = current_verex.get_key()
        for idx_vertex in range(i+1,n):
            vertex : Node = graph.getVertex(idx_vertex)
            Y1,X1 = vertex.get_key()
            l = int(((Y - Y1)**2 + (X-X1)**2)**(1/2))
            
            if l < thr:
                if len(list_list) == 0:
                    add_list.append(vertex)
                else:
                    flag = True
                    for el in list_list:
                        if vertex  in el:
                            flag = False

                    if flag == True:     
                        add_list.append(vertex)
        
        if len(add_list) != 1:
            list_list.append(add_list)



    deleted = []
    for el_list in list_list:
        x = [el.get_key()[1] for el in el_list ]
        x = int(sum(x)/len(x))
        y = [el.get_key()[0] for el in el_list]
        y = int(sum(y)/len(y))
        neighbours_list = []
        for el in el_list:      
            if el not in deleted:
                neighbours = graph.neighbours(graph.getVertexIdx(el))
                for neighbour in neighbours:
                    if neighbour not in neighbours_list and neighbour[0] not in el_list:
                        neighbours_list.append(neighbour)

        for toDelete in el_list:
            if toDelete not in deleted:
                graph.deleteVertex(toDelete)
                deleted.append(toDelete)
        centre_vertex = Node((y,x))
        for el_n in neighbours_list:
            y1, x1 = el_n[0].get_key()
            l = int(((y1 - y)**2 + (x1-x)**2)**(1/2))
            iloczyn_skalarny = x*x1 + y*y1
            l1 = np.sqrt(x**2 + y**2)
            l2 = np.sqrt(x1**2 +  y1**2)
            angle = np.arccos(iloczyn_skalarny/( l1* l2))
            graph.insertEdge(centre_vertex,el_n[0],(l,angle))
            graph.insertEdge(el_n[0],centre_vertex,(l,angle))



def biometric_graph_registration(graph1_input : Graf_list, graph2_input : Graf_list, Ni, eps):
    
    edges_graph1 = graph1_input.edges()
    edges_graph2 = graph2_input.edges()

    Sab_list = []
    for node1 in edges_graph1:
        for node2 in edges_graph2:
            la,lb_prim = node1[2]
            phia,phib_prim = node2[2]
            Sab =  1/(0.5*(la+lb_prim)) *math.sqrt((la - lb_prim)**2 + (phia - phib_prim)**2)
            Sab_list.append((node1, node2, Sab))
    
    Sab_list.sort(key=lambda el: el[2])

    Ni_Sab = Sab_list[:Ni]

    result = []
    for node1, node2, _ in Ni_Sab:
        vertex1 = node1[0]
        y1, x1 = vertex1.get_key()

        iloczyn_skalarny = x1
        l1 = np.sqrt(x1**2 + y1**2)
        l2 = 1
        angle = np.arccos(iloczyn_skalarny/( l1* l2))
        
        graph1_input.rotation((-y1, -x1), -angle)
        
        vertex2 = node2[0]
        y2, x2 = vertex2.get_key()

        iloczyn_skalarny = x2
        l1 = np.sqrt(x2**2 + y2**2)
        l2 = 1
        angle = np.arccos(iloczyn_skalarny/( l1* l2))
        
        graph2_input.rotation((-y2, -x2), -angle)

        c = 0
        used1 = []
        uset2 = []
        for i in range(graph1_input.order()):
            V1 = graph1_input.getVertex(i)
            y1, x1 = V1.get_key()
            d = float('inf')
            Vec = None
            for j in range(graph2_input.order()):
                V2 = graph2_input.getVertex(j)
                y2, x2 = V2.get_key()
                distance = np.sqrt((y2-y1)**2 + (x2-x1)**2)
                if distance < d:
                    d = distance
                    Vec = V2
            if V1 not in used1 and  Vec not in uset2 and d < eps:
                c += 1  
                used1.append(V1)
                uset2.append(Vec)
        result.append((node1, node2, 1 - c/np.sqrt(graph1_input.order()*graph2_input.order())))

    result.sort(key=lambda el: el[2])
    node1, node2, _ = result[0]
    vertex1 = node1[0]

    y1, x1 = vertex1.get_key()

    iloczyn_skalarny = x1
    l1 = np.sqrt(x1**2 + y1**2)
    l2 = 1
    angle = np.arccos(iloczyn_skalarny/( l1* l2))

    graph1_input.rotation((-y1, -x1), -angle)
    vertex2 = node2[0]

    y2, x2 = vertex2.get_key()
    iloczyn_skalarny = x2
    l1 = np.sqrt(x2**2 + y2**2)
    l2 = 1
    angle = np.arccos(iloczyn_skalarny/( l1* l2))

    graph2_input.rotation((-y2, -x2), -angle)
    return graph1_input, graph2_input





            

        
