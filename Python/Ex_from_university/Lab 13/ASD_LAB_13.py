# Skończone

import numpy as np
import time



def string_compare(P : str, T : str, i : int, j : int):
    if i == 0:
        return j
    if j == 0:
        return i
    
    zamian = string_compare(P,T,i-1,j-1) + int((P[i] != T[j]))
    wstawien = string_compare(P,T,i,j-1) + 1
    usuniec = string_compare(P,T,i-1,j) + 1

    min_cost = min([zamian,wstawien,usuniec])
    
    return min_cost


def string_compare_PD(P : str, T : str, type = 'd'):

    if P is None:
        P = sorted(T)

    D = np.zeros((len(P), len(T)))
    D[0,:] = [idx for idx, _ in enumerate(T)]
    D[:,0] = [idx for idx, _ in enumerate(P)]
    
    parent = ['X' for _ in T]
    parent = np.array([parent for _ in P])
    parent[0,1:] = 'I'
    parent[1:,0] = 'D'
    
    for i in range(1,len(P)):
        for j in range(1,len(T)):
            if type == 'd':
                zamian = D[i-1][j-1] + int((P[i] != T[j]))
            elif type == "e":
                zamian = D[i-1][j-1] + float('inf') if (P[i]!=T[j]) else 0
            wstawien = D[i][j-1] + 1
            usuniec = D[i-1][j] + 1
            

            min_cost = min([zamian,wstawien,usuniec])
            D[i][j] = min_cost
            if zamian == min_cost:
                if P[i] != T[j]:
                    parent[i][j] = 'S'
                else:
                    parent[i][j] = 'M'
            elif wstawien == min_cost:
                parent[i][j] = 'I'
            elif usuniec == min_cost:
                parent[i][j] = 'D'
            
    return int(D[-1][-1]), parent


def recontstrucion_path(P, T, parent, type = 'd'):

    if P is None:
        P = sorted(T)
    i = len(P) - 1
    j = len(T) - 1
    result = []

    if type == 'e':
        indexes = []

    while parent[i,j] != 'X':
        letter = parent[i,j]
        result.append(letter)
        if letter == "M":
            if type == 'e':
                indexes.append((i,j))
            i -= 1
            j -= 1
        elif letter == 'S':
            i -= 1
            j -= 1
            
        elif letter == 'D':
            i -= 1
            
        elif letter == 'I':
            j -= 1


    str_result = "".join(result)

    if type == 'e':
        return str_result[::-1], indexes[::-1]
    else:
        return str_result[::-1]




def string_compare_PD_extended(P : str, T : str):

    D = np.zeros((len(P), len(T)))
    D[:,0] = [idx for idx, _ in enumerate(P)]
    
    parent = ['X' for _ in T]
    parent = np.array([parent for _ in P])
    parent[1:,0] = 'D'
    
    for i in range(1,len(P)):
        for j in range(1,len(T)):

            zamian = D[i-1][j-1] + int((P[i] != T[j]))
            wstawien = D[i][j-1] + 1
            usuniec = D[i-1][j] + 1


            min_cost = min([zamian,wstawien,usuniec])
            D[i][j] = min_cost
            if zamian == min_cost:
                if P[i] != T[j]:
                    parent[i][j] = 'S'
                else:
                    parent[i][j] = 'M'
            elif wstawien == min_cost:
                parent[i][j] = 'I'
            elif usuniec == min_cost:
                parent[i][j] = 'D'
    
    i = len(P) - 1
    j = 0
    for k in range(1, len(T)):
        if D[i][k] < D[i][j]:
            j = k

    return int(D[-1][-1]), j



def main():


    P = ' kot'
    T = ' pies'
    min_cost = string_compare(P,T,len(P)-1, len(T)-1)
    print(min_cost)

    P = ' biały autobus'
    T = ' Czarny autokar'
    min_cost,_ = string_compare_PD(P,T)
    print(min_cost)


    P = ' thou shalt not'
    T = ' you should not'
    min_cost, parent = string_compare_PD(P,T)
    result = recontstrucion_path(P,T,parent)
    print(result)


    P = ' ban'
    T = ' mokeyssbanana'
    _, j = string_compare_PD_extended(P,T)
    print( j-len(P)+2)


    P = ' democrat'
    T = ' republican'
    _, parent = string_compare_PD(P,T,'e')
    _, indexes = recontstrucion_path(P,T,parent,'e')
    txt_result = ""
    for i, _ in indexes:
        txt_result += P[i]
    print(txt_result)

    T = ' 243517698'
    _, parent = string_compare_PD(None,T,'e')
    _, indexes = recontstrucion_path(None,T,parent,'e')
    txt_result = ""
    for _, j in indexes:
        txt_result += T[j]
    print(txt_result)
    
        
main()