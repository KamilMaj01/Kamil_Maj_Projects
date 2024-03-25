
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
                graf.append((self.help_list[idx_i].get_key(),self.help_list[j].get_key(),i[j]))
        return graf
    

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

class Find_union:
    def __init__(self, Graf : Graf_list) -> None:

        self.n = Graf.order()
        self.p = [el for el in range(self.n)]
        self.size = [-1 for el in range(self.n)]

    

    def find(self, v):
        if self.p[v] == v:
            return v
        
        return self.find(self.p[v])
    
    def union_sets(self, S1, S2):
        root1 = self.find(S1)
        root2 = self.find(S2)

        if root1 != root2:
            if self.size[root1] > self.size[root2]:
                self.p[root2] = root1
                self.size[root2] += 1
            else:
                self.p[root1] = root2
                self.size[root1] += 1

    def same_componenst(self,S1,S2):
        root1 = self.find(S1)
        root2 = self.find(S2)
        if root1 == root2:
            return True
        return False
    
def Graf_kruskal(g : Graf_list):
    find_union = Find_union(g)
    n = g.order()
    edges = g.edges()
    edges_sorted = sorted(edges,key= lambda edge: edge[2])
    result_edges = []
    for vertex1, vertex2, weight in edges_sorted:
        if not find_union.same_componenst(vertex1,vertex2):
            find_union.union_sets(vertex1,vertex2)
            result_edges.append((vertex1,vertex2,weight))
        if len(result_edges) == n-1:
            break
    return result_edges, sum([weight for _,_,weight in result_edges])
    



graf = [('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 4),
        ('B', 'E', 9), ('B', 'F', 9), ('B', 'G', 7), ('B', 'C', 5),
        ('C', 'G', 9), ('C', 'D', 3),
        ('D', 'G', 10), ('D', 'J', 18),
        ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
        ('F', 'H', 2), ('F', 'G', 8),
        ('G', 'H', 9), ('G', 'J', 8),
        ('H', 'I', 3), ('H', 'J', 9),
        ('I', 'J', 9)
        ]


def main():
    Graf = Graf_list()
    for el in graf:
        Graf.insertEdge(Node(ord(el[0])- ord('A')),Node(ord(el[1])- ord('A')),el[2])

    edges = Graf_kruskal(Graf)

    Result_Graf = Graf_list()
    for key1, key2, weight in edges[0]:
        Result_Graf.insertEdge(Node(chr(key1+ ord('A'))),Node(chr(key2+ ord('A'))),weight)

    printGraph(Result_Graf)
       

main()