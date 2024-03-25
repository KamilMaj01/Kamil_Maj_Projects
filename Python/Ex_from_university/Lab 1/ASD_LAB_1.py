from typing import List, Tuple, Union

class macierz:
    def __init__(self, param :Union[List,Tuple], value = 0 ) -> None:
        if isinstance(param, List):
            self.__matrix = param
            
        elif isinstance(param, Tuple):
            self.__matrix = [ [value for el1 in range(0,param[1])] for el2 in range(0,param[0])]

    
    

    
    def __str__(self) -> str:
        text = ""
        for i in self.__matrix:
            text += "| "
            for j in i:
                text += "{0} ".format(j)
            text += "|\n"
        return text

    def __getitem__(self, item):
        return self.__matrix[item]

    def __len__(self):
        return len(self.__matrix)


    def __add__(self, other):

        (row, col)= self.size()
        if (row, col) != other.size():
            return None
        
        submatrix = macierz((row,col))
        for idx_i, el_i in enumerate(self.__matrix, start=0):
            for idx_j, el_j in enumerate(el_i, start=0):
                submatrix[idx_i][idx_j] = el_j+other[idx_i][idx_j]
        return submatrix
    
    def __mul__(self,other):
        (row1, col1) = self.size()
        (row2, col2) = other.size()

        if col1 != row2:
            return None
        
        submatrix = transpose(other)
        exitmatrix = macierz((row1,col2))


        for idx_i, el_i in enumerate(self.__matrix):
            for idx_j, el_j in enumerate(submatrix):
                exitmatrix[idx_i][idx_j] = sum([el_j * el_i[idx_j] for idx_j, el_j in enumerate(el_j) ])
        return exitmatrix


    def size(self) -> Tuple:
        return (len(self.__matrix),len(self.__matrix[0]))
    
    def Chio(self,iloczyn = 1) -> float:
        if self.size()[0] != self.size()[1]:
            return None
        if self.size() == (2,2):
            return (self.__matrix[0][0]*self.__matrix[1][1] - self.__matrix[0][1]*self.__matrix[1][0])*iloczyn

        n = len(self.__matrix)
        submatrix = macierz((n-1,n-1))
        iloczyn *=  1/self.__matrix[0][0]**(n-2)

        for idx_i in range(n-1):
            for idx_j in range(n-1):
                submatrix[idx_i][idx_j] = (self.__matrix[0][0] * self.__matrix[idx_i+1][idx_j+1] - self.__matrix[idx_i+1][0]*self.__matrix[0][idx_j+1] )
   
        return submatrix.Chio(iloczyn)

def transpose(matrix :macierz) -> macierz:
    (row, col) = matrix.size()
    submatrix = macierz((col,row))
    for idx_i, el_i in enumerate(matrix):
        for idx_j, el_j in enumerate(el_i):
            submatrix[idx_j][idx_i] = el_j
    return submatrix



m1 = macierz(

 [
     [0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ]

)
print(m1.Chio())



# (1/self.__matrix[0][0]**(n-2))*self.__matrix[0][0] * self.__matrix[idx_i+1][idx_j+1] -