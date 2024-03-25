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



def color_graph(graf, type_grpah):
    if type_grpah == 0:
        return DFS(graf)
    elif type_grpah == 1:
        return BFS(graf)

def DFS(graf):
    visited = [graf.help_list[0]]
    stos = [graf.help_list[0]]
    colors = []
    colors_help_list = [None for _ in graf.help_list]

    while len(stos) !=  0:
        node = stos.pop()
        select_color = [None for _ in graf.help_list]
        for neighbour in graf.neighbours(graf.getVertexIdx(node)):
            if neighbour not in visited:
                stos.append(neighbour)
                visited.append(neighbour)
            index_neighbour = graf.getVertexIdx(neighbour)
            
            if colors_help_list[index_neighbour] is not None:
                select_color[colors_help_list[index_neighbour]] = 1
            
        new_color = 0
        while select_color[new_color] is not None:
            new_color += 1

        colors_help_list[graf.getVertexIdx(node)] = new_color
        colors.append((node.get_key(), new_color))
    
    return colors
                
        
def BFS(graf):
    visited = [graf.help_list[0]]
    kolejka = [graf.help_list[0]]
    colors = []
    colors_help_list = [None for _ in graf.help_list]

    while len(kolejka) !=  0:
        node = kolejka.pop(0)
        select_color = [None for _ in graf.help_list]
        for neighbour in graf.neighbours(graf.getVertexIdx(node)):
            if neighbour not in visited:
                kolejka.append(neighbour)
                visited.append(neighbour)
            index_neighbour = graf.getVertexIdx(neighbour)
            
            if colors_help_list[index_neighbour] is not None:
                select_color[colors_help_list[index_neighbour]] = 1
            
        new_color = 0
        while select_color[new_color] is not None:
            new_color += 1

        colors_help_list[graf.getVertexIdx(node)] = new_color
        colors.append((node.get_key(), new_color))
    
    return colors


def main():
    
    
    miasta = Graf_list()

    litery = [polska.graf[0][0]]
    litera = polska.graf[0][0]
    for el in polska.graf:
        if el[0] != litera:
            litery.append(el[0])
            litera = el[0]

    dictionary_cities = {el : Node(el) for el in litery }
 
    for el in dictionary_cities.values():
        miasta.insertVertex(el)
 
    for el in polska.graf:
        miasta.insertEdge(dictionary_cities[el[0]], dictionary_cities[el[1]])

    edge_matrix = miasta.edges()

    # DFS: type_graph = 0, BFS: type_graph = 1
    colors_DFS = color_graph(miasta, 0)
    colors_BFS = color_graph(miasta, 1)

    # polska.draw_map(edge_matrix, colors_DFS)
    polska.draw_map(edge_matrix, colors_BFS)
    
main()
