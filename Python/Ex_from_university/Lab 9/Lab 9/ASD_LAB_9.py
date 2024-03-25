from graf_mst import graf

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
                graf.append((self.help_list[idx_i].get_key(),self.help_list[j].get_key()))
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

    graf_sorted = sorted(graf,key = lambda el: el[2])
    for key1, key2, edge in graf_sorted:
        Graf.insertEdge(Node(key1),Node(key2),edge)

    Graf_MST = primMST(Graf)
    printGraph(Graf_MST[0])
    print("'długość' drzewa rozpinającego: ",Graf_MST[1])
main()
