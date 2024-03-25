# Skończone
import numpy as np

class Node:
    def __init__(self, key) -> None:
        self.__key = key

    def __eq__(self, other) -> bool:
        return self.__key == other.__key

    def __hash__(self):
        return hash(self.__key)
    
    def get_key(self):
        return self.__key
    
    def __repr__(self) -> str:
        return f'{self.__key}'

class Graf_matrix:
    def __init__(self, param_matrix = 0) -> None:
        self.graf_matrix = None
        self.param_matrix = param_matrix
        self.help_list = []
        self.help_dict = {}
        

    def is_empty(self):
        return len(self.help_list) == 0

    def insertVertex(self, vertex):
        if vertex in self.help_list:
            return None
      
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
        self.insertVertex(vertex1)
        self.insertVertex(vertex2)

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
        for idx, i in enumerate(self.graf_matrix[vertex_idx]):
            if i > 0 :
                neighboursIdx_list.append(idx)
        return neighboursIdx_list

    def neighbours(self, vertex_idx):
        neighbours_list = []
        for idx, i in enumerate(self.graf_matrix[vertex_idx]):
            if i > 0 :
                neighbours_list.append((self.help_list[idx],i))
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

    def getMatrix(self):
        return self.graf_matrix
    
def printGraph(g: Graf_matrix):
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

def ullman(current_row, M : np.ndarray,P : np.ndarray, G : np.ndarray, Graf_G, Graf_P, M0 : np.ndarray = None, no_recursion = 0, result: list = None, metoda = None, ColList = None):
    if ColList is None:
        ColList = [False for _ in range(M.shape[1])]
    if current_row == M.shape[0]:
        if (P == M@np.transpose((M@G))).all():
            if result is None:
                result = [M.copy()]
            else:
                result.append(M.copy())
        return result, no_recursion
    
    if metoda == 3:
        M_3 = M.copy()
        Outcome_prune = True
        if current_row == M.shape[0] - 1:
            Outcome_prune = prune(M_3,Graf_G,Graf_P)

    for idx_col in range(len(ColList)):
        if metoda == 3:
            if Outcome_prune == False and current_row != 0:
                break
        if ColList[idx_col] == False:
            ColList[idx_col] = True
            if M0 is None:
                M[current_row,:] = 0
                M[current_row, idx_col] = 1
                result, no_recursion = ullman(current_row +1, M,P,G,Graf_G,Graf_P,None, no_recursion, result,ColList= ColList)
                no_recursion += 1
                ColList[idx_col] = False
            elif M0 is not None:
                if metoda == 3:
                    M_3[current_row,:] = 0
                    if M0[current_row, idx_col] == 1:
                        M_3[current_row, idx_col] = 1
                        result, no_recursion = ullman(current_row +1, M_3,P,G,Graf_G,Graf_P,M0, no_recursion, result,metoda = 3,ColList= ColList)
                        no_recursion += 1
                        ColList[idx_col] = False
                else:
                    M[current_row,:] = 0
                    if M0[current_row, idx_col] == 1:
                        M[current_row, idx_col] = 1
                        result, no_recursion = ullman(current_row +1, M,P,G,Graf_G,Graf_P,M0, no_recursion, result,ColList= ColList)
                        no_recursion += 1
                        ColList[idx_col] = False

    return result, no_recursion

def prune(M : np.ndarray, Graf_G : Graf_matrix, Graf_P : Graf_matrix):
    (Y,X) = M.shape
    test = True
    while test:
        test = False
        for i in range(Y):
            for j in range(X):
                if M[i,j] == 1:
                    neighours_i = Graf_P.neighboursIdx(i)
                    neighours_j = Graf_G.neighboursIdx(j)
                    list_test = [False for _ in range(len(neighours_i))]
                    for n, idx_neighbour_i in enumerate(neighours_i):
                        for idx_neighbour_j in neighours_j:
                            if M[idx_neighbour_i,idx_neighbour_j] == 1:
                                list_test[n] = True
                                break
                    if not any(list_test):
                        M[i,j] = 0
                        test = True
                        
    if any(list_test):
        return True
    else:
        return False
    
                        
def createGraf(graf):
    Graf = Graf_matrix()
    for key1, key2, weight in graf:
        Graf.insertEdge(Node(key1), Node(key2),weight)
    return Graf

def metoda1(M,matrix_Graf_P,matrix_Graf_G, Graf_G, Graf_P):
    return ullman(0,M.copy(),matrix_Graf_P,matrix_Graf_G, Graf_G, Graf_P)

def metoda2(Graf_P,Graf_G,matrix_Graf_P,matrix_Graf_G, M):
    M0 = createM0(Graf_P,Graf_G,matrix_Graf_P,matrix_Graf_G)
    return ullman(0,M.copy(),matrix_Graf_P,matrix_Graf_G,Graf_G,Graf_P,M0.copy())

def createM0(Graf_P,Graf_G,matrix_Graf_P,matrix_Graf_G):
    M0 = np.zeros((Graf_P.order(),Graf_G.order()))
    (Y_M0, X_M0) = M0.shape
    for i in range(Y_M0):
        for j in range(X_M0):
            sum_P_i = np.sum(matrix_Graf_P[i])
            if np.sum(matrix_Graf_G[j]) >= sum_P_i:
                M0[i,j] = 1
    return M0

def metoda3(Graf_P,Graf_G,matrix_Graf_P,matrix_Graf_G, M):
    M0 = createM0(Graf_P,Graf_G,matrix_Graf_P,matrix_Graf_G)
    return ullman(0,M.copy(),matrix_Graf_P,matrix_Graf_G,Graf_G,Graf_P,M0.copy(),metoda=3)

def main():
    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]

    Graf_P = createGraf(graph_P)
    Graf_G = createGraf(graph_G)

    matrix_Graf_G = np.array(Graf_G.getMatrix())
    matrix_Graf_P = np.array(Graf_P.getMatrix())

    M = np.zeros((Graf_P.order(),Graf_G.order()))

    result, no_recursion = metoda1(M,matrix_Graf_P,matrix_Graf_G, Graf_G, Graf_P)
    print(f'algorytm 1.0: ({len(result)}, {no_recursion})')

    result20, no_recursion20 = metoda2(Graf_P,Graf_G,matrix_Graf_P,matrix_Graf_G, M)
    print(f'algorytm 2.0: ({len(result20)}, {no_recursion20})')

    result30, no_recursion30 = metoda3(Graf_P,Graf_G,matrix_Graf_P,matrix_Graf_G, M)
    print(f'algorytm 3.0: ({len(result30)}, {no_recursion30})')

main()

