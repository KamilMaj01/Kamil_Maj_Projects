# Skończone
import numpy as np

class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.point = (self.x,self.y)

    def __repr__(self) -> str:
        return f'({self.x},{self.y})'

    def get_point(self):
        return self.point
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def check_position(self, Q, R):
        L_PQ = self.length(Q)
        L_PR = self.length(R)
        if L_PQ < L_PR:
            return R
        else:
            return Q

    def length(self, other):
        x,y = self.point
        x1,y1 = other.point
        return np.sqrt(((x1 - x)**2 + (y1 - y)**2))
    
    def cost(self,Q,R):
        L_PQ = self.length(Q)
        L_PR = self.length(R)
        L_QR = Q.length(R)
        return L_PQ + L_PR + L_QR



def triangularyzacja_R(point_list : list[Point],start_idx,  stop_idx, min_cost = None):
    if len(point_list) < 3:
        return None

    i = point_list[start_idx]
    j = point_list[stop_idx]

    if len(list(range(start_idx,stop_idx +1))) < 3:
        return 0
    elif len(list(range(start_idx,stop_idx +1))) == 3:
        return i.cost(point_list[start_idx + 1], j)
    
    if min_cost is None:
        min_cost = float('inf')

    for k_idx in range(start_idx, stop_idx + 1):
        cost = 0
        k = point_list[k_idx]
        if k == i:
            continue
        elif k == j:
            continue
        cost += i.cost(k,j)
        cost += triangularyzacja_R(point_list,start_idx,k_idx, min_cost)
        cost += triangularyzacja_R(point_list,k_idx,stop_idx, min_cost)

                
        if cost < min_cost:
            min_cost = cost

    return min_cost



def triangularyzacja_PD(point_list : list[Point]):
    size = len(point_list)
    P = np.zeros((size,size))
    for idx in range(size):
        idx_I = 0
        for idx_J in range(idx_I+ idx,size):
            I = point_list[idx_I]
            J = point_list[idx_J]       
            if len(list(range(idx_I,idx_J +1))) == 3:
                P[idx_I,idx_J] = I.cost(point_list[idx_I + 1],J)
            elif len(list(range(idx_I,idx_J +1))) > 3:
                P[idx_I,idx_J] = float('inf')
                for idx_k in range(idx_I+1,idx_J):
                    k = point_list[idx_k]
                    I = point_list[idx_I]
                    J = point_list[idx_J]
                    cost = P[idx_I][idx_k] + P[idx_k][idx_J] + I.cost(k, J)
                    if P[idx_I][idx_J] > cost:
                        P[idx_I][idx_J] = cost
            idx_I += 1


    return P[0,-1]



def main():
    lista = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]]
    lista2 =[[0, 0], [4, 0], [5, 4], [4, 5], [2, 5], [1, 4], [0, 3], [0, 2]]

    to_fun_lista = []
    for x, y  in lista:
        to_fun_lista.append(Point(x, y))

    print('Pierwszy zestaw punktów:')
    print('Medota rekurencyjna: {0:.4f}'.format(triangularyzacja_R(to_fun_lista, 0 , len(to_fun_lista)-1)))
    print('Medota z programowaniem dynamicznym: {0:.4f}'.format(triangularyzacja_PD(to_fun_lista)))

    to_fun_lista = []
    for x, y  in lista2:
        to_fun_lista.append(Point(x, y))

    print('\nDrugi zestaw punktów:')
    print('Medota rekurencyjna: {0:.4f}'.format(triangularyzacja_R(to_fun_lista, 0 , len(to_fun_lista)-1)))
    print('Medota z programowaniem dynamicznym: {0:.4f}'.format(triangularyzacja_PD(to_fun_lista)))


main()

