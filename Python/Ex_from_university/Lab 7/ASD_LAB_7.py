# skończone
import polska

class Node:
    def __init__(self, key) -> None:
        self.__key = key

    def __eq__(self, other) -> bool:
        return self.__key == other.__key

    def __hash__(self):
        return hash(self.__key)
    
    def get_key(self):
        return self.__key

class Graf_matrix:
    def __init__(self, param_matrix = 0) -> None:
        self.graf_matrix = None
        self.param_matrix = param_matrix
        self.help_list = []
        self.help_dict = {}
        

    def is_empty(self):
        return len(self.help_list) == 0

    def insertVertex(self, vertex):
      
        if self.is_empty():
            self.help_list.append(vertex)
            self.help_dict[vertex] = self.param_matrix
            self.graf_matrix = [[self.param_matrix]]
        
        else:
            self.help_list.append(vertex)
            self.help_dict[vertex] = len(self.help_list) -1
            for row in self.graf_matrix:
                row.append(self.param_matrix)
            self.graf_matrix.append([self.param_matrix for el in range(len(self.graf_matrix[0]))])


        

    def insertEdge(self,vertex1, vertex2, egde = 1):
        if self.is_empty():
            return None
        idxa = self.getVertexIdx(vertex1)
        idxb = self.getVertexIdx(vertex2)

        self.graf_matrix[idxa][idxb] = egde
        self.graf_matrix[idxb][idxa] = egde

    def deleteVertex(self, vertex):
        if self.is_empty():
            return None
        idx = self.help_dict.pop(vertex)
        self.help_list.pop(idx)

        for i in self.graf_matrix:
            i.pop(idx)
        self.graf_matrix.pop(idx)

    
    def deleteEdge(self, vertex1, vertex2):
        if self.is_empty():
            return None
        
        idxa = self.getVertexIdx(vertex1)
        idxb = self.getVertexIdx(vertex2)

        self.graf_matrix[idxa][idxb] = self.param_matrix
        self.graf_matrix[idxb][idxa] = self.param_matrix

    def getVertexIdx(self, vertex):
        if self.is_empty():
            return None
        return self.help_dict[vertex]

    def getVertex(self, vertex_idx):
        return self.help_list[vertex_idx]

    def neighboursIdx(self, vertex_idx):
        neighboursIdx_list = []
        for i in self.graf_matrix[vertex_idx]:
            if i > 0 :
                neighboursIdx_list.append(i)
        return neighboursIdx_list

    def neighbours(self, vertex_idx):
        neighbours_list = []
        for idx, i in enumerate(self.graf_matrix[vertex_idx]):
            if i > 0 :
                neighbours_list.append(self.help_list[idx])
        return neighbours_list

    def order(self):
        return len(self.help_list)

    def size(self):
        size = 0
        for i in self.graf_matrix:
            for j in i:
                size += j
        return int(size/2)


    def edges(self):
        graf = []
        for idx_i, i in enumerate(self.graf_matrix):
            for idx_j, j in enumerate(i):
                if j > 0:
                    graf.append((self.help_list[idx_i].get_key(),self.help_list[idx_j].get_key()))
        return graf

class Graf_list:
    def __init__(self) -> None:
        self.graf_list = None
        self.help_list = []
        self.help_dict = {}


    def is_empty(self):
        return len(self.help_list) == 0

    def insertVertex(self, vertex):
        if self.is_empty():
            self.help_list.append(vertex)
            self.help_dict[vertex] = 0
            self.graf_list = [{}]
        
        else:
            self.help_list.append(vertex)
            self.help_dict[vertex] = len(self.help_list) -1
            self.graf_list.append({})




    def insertEdge(self,vertex1, vertex2, weight = None):
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
        return (self.graf_list[vertex_idx]).keys()

    def neighbours(self, vertex_idx):
        idxes = (self.graf_list[vertex_idx]).keys()
        obj = [self.getVertex(idx) for idx in idxes]
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


def main():
    
    
    miasta_matrix = Graf_matrix()

    litery = [polska.graf[0][0]]
    litera = polska.graf[0][0]
    for el in polska.graf:
        if el[0] != litera:
            litery.append(el[0])
            litera = el[0]

    dictionary_cities = {el : Node(el) for el in litery }
 
    for el in dictionary_cities.values():
        miasta_matrix.insertVertex(el)
 
    for el in polska.graf:
        miasta_matrix.insertEdge(dictionary_cities[el[0]], dictionary_cities[el[1]])

    
    miasta_matrix.deleteVertex(dictionary_cities['K'])
    miasta_matrix.deleteEdge(dictionary_cities['W'],dictionary_cities['E'])
    edge_matrix = miasta_matrix.edges()

    miasta_lista = Graf_list()

    for el in dictionary_cities.values():
        miasta_lista.insertVertex(el)
 
    for el in polska.graf:
        miasta_lista.insertEdge(dictionary_cities[el[0]], dictionary_cities[el[1]])

    
    miasta_lista.deleteVertex(dictionary_cities['K'])
    miasta_lista.deleteEdge(dictionary_cities['W'],dictionary_cities['E'])
    edge_lista = miasta_lista.edges()

    polska.draw_map(edge_matrix)
    polska.draw_map(edge_lista)

main()




