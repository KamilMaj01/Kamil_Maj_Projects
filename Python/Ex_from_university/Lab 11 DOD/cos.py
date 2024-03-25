import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

class Vertex:

    def __init__(self, key):
        self.__key = key

    def __str__(self):
        return f'{self.__key}'

    def __repr__(self):
        return f'{self.__key}'

    def __eq__(self, other):
        return self.__key == other.__key

    def __hash__(self):
        return hash(self.__key)

    def get_key(self):
        return self.__key
    
    def set_key(self, key):
        self.__key = key

class Edge:

    def __init__(self, length, orientation):
        self.length = length
        self.orientation = orientation

    def __eq__(self, other):
        return  self.length == other.length \
                and self.orientation == other.orientation
    
    def __repr__(self):
        return f'L{self.length};O{self.orientation}'

    def __hash__(self) -> int:
        return hash((self.length, self.orientation))

class BiometricGraph:

    def __init__(self, fill_value=0):
        self.list_of_neighbours = []
        self.fill_value = fill_value
        self.indexes = []
        self.objects_to_indexes = {}

    def is_empty(self):
        return len(self.indexes) == 0

    def insert_vertex(self, vertex):
        if vertex in self.indexes:
            return
        self.list_of_neighbours.append({})
        self.objects_to_indexes[vertex] = len(self.indexes)
        self.indexes.append(vertex)

    def insert_edge(self, vertex1, vertex2, edge=0.0):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        i = self.objects_to_indexes[vertex1]
        j = self.objects_to_indexes[vertex2]
        self.list_of_neighbours[i][vertex2] = edge
        self.list_of_neighbours[j][vertex1] = edge

    def delete_vertex(self, vertex):
        if self.is_empty():
            return
        for dct in self.list_of_neighbours:
            if vertex in dct.keys():
                del dct[vertex]
        i = self.objects_to_indexes[vertex]
        self.list_of_neighbours.pop(i)
        self.indexes.remove(vertex)
        del self.objects_to_indexes[vertex]
        for index, vertex in enumerate(self.indexes):
            self.objects_to_indexes[vertex] = index

    # def delete_vertex(self, vertex):


    #     idx_vertex = self.objects_to_indexes.pop(vertex)
    #     self.indexes.pop(idx_vertex)
    #     self.list_of_neighbours.pop(idx_vertex)

    #     for idx, el in enumerate(self.indexes):
    #         self.objects_to_indexes[el] = idx

    #     for idx_el, el in enumerate(self.list_of_neighbours):
    #         if idx_vertex in el.keys():
    #             self.list_of_neighbours[idx_el].pop(idx_vertex)
    #         self.list_of_neighbours[idx_el] = {(index - 1) if index > idx_vertex else index : value for index, value in el.items()}

    def delete_edge(self, vertex1, vertex2):
        i = self.objects_to_indexes[vertex1]
        j = self.objects_to_indexes[vertex2]
        del self.list_of_neighbours[i][vertex2]
        del self.list_of_neighbours[j][vertex1]

    def get_vertex_idx(self, vertex):
        return self.indexes.index(vertex)

    def get_vertex(self, vertex_idx):
        return self.indexes[vertex_idx]

    def neighbours_idx(self, vertex_idx):
        neighbours_indexes = []
        for key, value in self.list_of_neighbours[vertex_idx].items():
            neighbours_indexes.append(self.objects_to_indexes[key])
        return neighbours_indexes

    def neighbours(self, vertex_idx):
        neighbours_objects = []
        for key, value in self.list_of_neighbours[vertex_idx].items():
            neighbours_objects.append(key)
        return neighbours_objects

    def order(self):
        return len(self.indexes)

    def size(self):
        sum_of_edges = 0
        for dct in self.list_of_neighbours:
            sum_of_edges += len(dct)
        return sum_of_edges // 2

    def edges(self):
        result_set = set()
        for i in range(len(self.list_of_neighbours)):
            for key, value in self.list_of_neighbours[i].items():
                vertex1 = self.indexes[i]
                vertex2 = key
                vertex1_key = vertex1.get_key()
                vertex2_key = vertex2.get_key()
                if (vertex1_key, vertex2_key, value) not in result_set and (vertex2_key, vertex1_key, value) not in result_set:
                    result_set.add((vertex1_key, vertex2_key, value))
        return list(result_set)
    
    def rotation(self, translation, angle):
        y_t = translation[0]
        x_t = translation[1]

        for vertex in self.indexes:
            y, x = vertex.get_key()
            y_prim = -(x + x_t)*np.sin(angle) + (y + y_t)*np.cos(angle)
            x_prim = (x + x_t)*np.cos(angle) + (y + y_t)*np.sin(angle)
            vertex.set_key((y_prim, x_prim))
        for i in range(self.order()):
            y_med, x_med = self.get_vertex(i).get_key()
            for vertex in self.neighbours(i):
                y_cur, x_cur = vertex.get_key()
                len_of_mean = np.sqrt(np.power(y_med, 2) + np.power(x_med, 2))
                len_of_current = np.sqrt(np.power(y_cur, 2) + np.power(x_cur, 2))
                iloczyn_skalarny = x_cur*x_med + y_cur*y_med
                angle = np.arccos(iloczyn_skalarny/(len_of_mean * len_of_current))
                distance = np.sqrt(np.power(y_med - y_cur, 2) + np.power(x_med - x_cur, 2))
                self.insert_edge(self.get_vertex(i), vertex, Edge(distance, angle))


    def plot_graph(self, v_color, e_color):
      for idx, v in enumerate(self.indexes):
            y, x = v.get_key()
            plt.scatter(x, y, c=v_color)
            for n_idx in self.neighbours_idx(idx):
                yn, xn = self.get_vertex(n_idx).get_key()
                plt.plot([x, xn], [y, yn], color=e_color)

def print_graph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.get_vertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours_idx(i)
        for j in nbrs:
            print(str(g.get_vertex(j)), end=";")
        print()
    print("-------------------")

def fill_biometric_graph_from_image(img, graph: BiometricGraph):
    Y, X = img.shape
    for i in range(Y):
        for j in range(X):
            if img[i, j] == 255:
                graph.insert_vertex(Vertex((i, j)))
                neighbours = [(i, j-1), (i-1, j-1), (i-1, j), (i-1, j+1)] # wycinam sąsiedztwo
                for y, x in neighbours:
                    if img[y, x] == 255:
                        distance = distance = np.sqrt(np.power(y - i, 2) + np.power(x - j, 2))
                        len_of_mean = np.sqrt(np.power(y, 2) + np.power(x, 2))
                        len_of_current = np.sqrt(np.power(i, 2) + np.power(j, 2))
                        iloczyn_skalarny = x*j + y*i
                        angle = np.arccos(iloczyn_skalarny/(len_of_mean * len_of_current))
                        graph.insert_edge(Vertex((y, x)), Vertex((i, j)), Edge(distance, angle))


def unclutter_biometric_graph(graph: BiometricGraph):
    to_delete = []
    to_add = []
    n = graph.order()
    for i in range(n):
        neighbours = graph.neighbours_idx(i)
        if len(neighbours) != 2:
            for current in neighbours:
                prev = i
                while len(graph.neighbours_idx(current)) == 2:
                    if current not in to_delete:
                        to_delete.append(current)
                    nbrs = graph.neighbours_idx(current)
                    next = nbrs[0] if nbrs[0] != prev else nbrs[1]
                    prev = current
                    current = next
                to_add.append((graph.get_vertex(i), graph.get_vertex(current)))
    for u, v in to_add:
        y, x = u.get_key()
        i, j = v.get_key()
        distance = distance = np.sqrt(np.power(y - i, 2) + np.power(x - j, 2))
        len_of_mean = np.sqrt(np.power(y, 2) + np.power(x, 2))
        len_of_current = np.sqrt(np.power(i, 2) + np.power(j, 2))
        iloczyn_skalarny = x*j + y*i
        angle = np.arccos(iloczyn_skalarny/(len_of_mean * len_of_current))
        graph.insert_edge(u, v, Edge(distance, angle))
    to_delete.sort(key=lambda x: x)
    to_delete.reverse()
    for v in to_delete:
        graph.delete_vertex(graph.get_vertex(v))


def merge_near_vertices(graph: BiometricGraph, thr):
    to_add = []
    n = graph.order()
    for i in range(n):
        current = graph.get_vertex(i)
        row = []
        row.append(current)
        y, x = current.get_key()
        for j in range(i + 1, n):
            neighbour = graph.get_vertex(j)
            yj, xj = neighbour.get_key()
            distance = int(((y-yj)**2 + (x-xj)**2)**0.5)
            if distance < thr:
                is_present = False
                for entry in to_add:
                    if neighbour in entry:
                        is_present = True
                        break
                if not is_present:
                    row.append(neighbour)
        if len(row) > 1:
            to_add.append(row)

    for row in to_add:
        x = [v.get_key()[1] for v in row]
        y = [v.get_key()[0] for v in row]
        y_med = np.median(y)
        x_med = np.median(x)
        print(y_med)
        to_connect = []
        for vertex in row:
            if vertex == Vertex((y_med, x_med)):
                mean_vertex = vertex
            neighbours = graph.neighbours(graph.get_vertex_idx(vertex))
            for v in neighbours:
                if v not in neighbours and v not in row:
                    to_connect.append(v)
        for vertex in row:
            if vertex != mean_vertex:
                graph.delete_vertex(vertex) 
        for vertex in to_connect:
            y_cur, x_cur = vertex.get_key()
            
            len_of_mean = np.sqrt(np.power(y_med, 2) + np.power(x_med, 2))
            len_of_current = np.sqrt(np.power(y_cur, 2), np.power(x_cur, 2))
            iloczyn_skalarny = x_cur*x_med + y_cur*y_med
            angle = np.arccos(iloczyn_skalarny/(len_of_mean * len_of_current))
            distance = np.sqrt(np.power(y_med - y_cur, 2) + np.power(x_med - x_cur, 2))
            graph.insert_edge(mean_vertex, vertex, Edge(distance, angle))
         

def biometric_graph_registration(graph1: BiometricGraph, graph2: BiometricGraph, Ni, eps):
    edges1 = graph1.edges()
    edges2 = graph2.edges()
    Sab_list = []
    for tup1 in edges1:
        for tup2 in edges2:
            edge1 = tup1[2]
            print(tup1)
            edge2 = tup2[2]
            value = 2/(edge1.length*edge2.length)* \
                    np.sqrt(np.power(edge1.length-edge2.length, 2) 
                            + np.power(edge1.orientation-edge2.orientation, 2))
            Sab_list.append((tup1, tup2, value))
    Sab_list.sort(key=lambda x: x[2])
    left = Sab_list[Ni:]
    result = []
    for tup1, tup2, _ in left:
        vertex1 = tup1[0]
        y1, x1 = vertex1
        graph1.rotation((-y1, -x1), -tup1[2].orientation)
        vertex2 = tup2[0]
        y2, x2 = vertex2
        graph2.rotation((-y2, -x2), -tup2[2].orientation)
        c = 0
        for i in range(min(graph1.order(), graph2.order())):
            y1, x1 = graph1.get_vertex(i).get_key()
            y2, x2 = graph2.get_vertex(i).get_key()
            distance = np.sqrt(np.power(y2-y1, 2) + np.power(x2-x1, 2))
            if distance < eps:
                c += 1
        result.append((tup1, tup2, 1 - c/np.sqrt(graph1.order()*graph2.order())))
    result.sort(key=lambda x: x[2])
    tup1, tup2, _ = result[0]
    vertex1 = tup1[0]
    y1, x1 = vertex1.get_key()
    graph1.rotation((-y1, -x1), -tup1[2].orientation)
    vertex2 = tup2[0]
    y2, x2 = vertex2.get_key()
    graph2.rotation((-y2, -x2), -tup2[2].orientation)
    return graph1, graph2

# img = cv2.imread('C:/studia/asd/lab11/Retina_graph_easy_1.png')
# img_1ch = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# _, img = cv2.threshold(img_1ch, 127, 255, cv2.THRESH_BINARY)
# graph = BiometricGraph()
# fill_biometric_graph_from_image(img, graph)
# unclutter_biometric_graph(graph)
# merge_near_vertices(graph, thr=5)
# a = graph.indexes
# for el in a:
#     y, x = el.get_key()
#     img[y, x] = 150
# plt.imshow(img, 'gray')
# plt.show()

def main():
    data_path = "./Images/"
    img_level = "easy"
    img_list = ["Retina_graph_easy_1.png", "Retina_graph_easy_2.png"]#, "Retina_graph_easy_3.png"]

    input_data = []
    for img_name in img_list:
        if img_name[-3:] == "png":
            if img_name.split('_')[-2] == img_level:
                print("Processing ", img_name, "...")
                img = cv2.imread(data_path + img_name)
                img_1ch = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                _, img_bin = cv2.threshold(img_1ch, 127, 255, cv2.THRESH_BINARY)
               
                graph = BiometricGraph()
                fill_biometric_graph_from_image(img_bin, graph)                
                unclutter_biometric_graph(graph)    
                merge_near_vertices(graph, thr=5)

                input_data.append((img_name, graph))
                print("Saved!")

    for i in range(len(input_data)):
        for j in range(len(input_data)):
            graph1_input = input_data[i][1]
            graph2_input = input_data[j][1]

            graph1, graph2 = biometric_graph_registration(graph1_input, graph2_input, Ni=3, eps=10)

            plt.figure()
            graph1.plot_graph(v_color='red', e_color='green')

            graph2.plot_graph(v_color='gold', e_color='blue')
            plt.title('Graph comparison')
            plt.show()

if __name__ == "__main__":
    main()