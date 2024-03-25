import random
import time
from copy import deepcopy

class Element:

    def __init__(self, priorytet, value) -> None:
        self.__dane = value
        self.__priorytet = priorytet
    
    def __repr__(self) -> str:
        return "{0}:{1}".format(self.__priorytet, self.__dane)
    

    def __lt__(self, other):
        if self.__priorytet < other.__priorytet:
            return True
        return False
    
    def __gt__(self, other):
        if self.__priorytet > other.__priorytet:
            return True
        return False

class Queue:
    def __init__(self, list_to_sort = None) -> None:
        if list_to_sort is None:
            self.size = 0
            self.table = []
        else:
            self.table = list_to_sort
            self.size = len(self.table)
            idx_parent = self.parent(self.size - 1)
            for idx in range(idx_parent, -1,-1):
                self.hepify_dequeue(idx)

        


    def is_empty(self):
        if self.size == 0:
            return True
        return False


    def peek(self):
        if self.is_empty():
            return None
        
        return self.table[0]

    def dequeue(self):
        if self.is_empty():
            return None
        el_max_priorytet = self.table[0]
        self.table[0], self.table[self.size-1] = self.table[self.size -1], self.table[0]
        self.size -= 1
        self.hepify_dequeue()
        return el_max_priorytet
    
    def hepify_dequeue(self, index = 0):
        idx_par = index
        if self.left(idx_par) <= self.size -1:
            idx_left = self.left(idx_par)
        else:
            idx_left = None

        if self.right(idx_par) <= self.size-1:
            idx_right = self.right(idx_par)
        else:
            idx_right = None

        while (idx_left is not None and self.table[idx_par] < self.table[idx_left]) or (idx_right is not None and self.table[idx_par] < self.table[idx_right]):
            if idx_left is not None and self.table[idx_par] < self.table[idx_left] and (idx_right is None or self.table[idx_left] > self.table[idx_right]):
                self.table[idx_par], self.table[idx_left] = self.table[idx_left], self.table[idx_par]
                idx_par = idx_left
            elif idx_right is not None and self.table[idx_par] < self.table[idx_right]:
                self.table[idx_par], self.table[idx_right] = self.table[idx_right], self.table[idx_par]
                idx_par = idx_right
            
            if self.left(idx_par) <= self.size -1:
                idx_left = self.left(idx_par)
            else:
                idx_left = None

            if self.right(idx_par) <= self.size-1:
                idx_right = self.right(idx_par)
            else:
                idx_right = None


    def enqueue(self, elem):
        if self.size == len(self.table):
            self.table.append(elem)
        else:
            self.table[self.size] = elem
        self.size += 1
        self.heapify_enqueue(self.size -1)

    def heapify_enqueue(self, idx_el):
        idx_par = self.parent(idx_el)
        while self.table[idx_par] < self.table[idx_el]:
            self.table[idx_par], self.table[idx_el] = self.table[idx_el], self.table[idx_par]
            idx_el = idx_par
            idx_par = self.parent(idx_el)

    def sort(self):   
        while not self.is_empty():
            self.dequeue()


    def left(self,index):
        return 2*index +1
    
    def right(self, index):
        return 2*index+2

    def parent(self,index):
        return abs((index -1))//2

    def print_tab(self):
        print ('{', end=' ')
        print(*self.table[:self.size], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx<self.size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.table[idx] if self.table[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)

#******************DRUGA_CZĘŚĆ*************************#

def selection_sort(lista):
    for idx in range(len(lista)-1):
        min_value = min(lista[idx:])
        idx_min_value = lista[idx:].index(min_value) + idx
        lista[idx], lista[idx_min_value] = lista[idx_min_value], lista[idx]
    return lista





def main():
    elementy = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    lista_el = [Element(el[0], el[1]) for el in elementy]
    Copy_list_el = deepcopy(lista_el)
    Kopiec = Queue(Copy_list_el)
    Kopiec.print_tab()
    Kopiec.print_tree(0,0)
    Kopiec.sort()
    print(Copy_list_el)
    
    lista_randomowa = [int(random.random() * 100) for _ in range(10000)]
    Copy_lista_randomowa = deepcopy(lista_randomowa)
    t_start = time.perf_counter()
    Kopiec_v2 = Queue(Copy_lista_randomowa)
    Kopiec_v2.sort()
    t_stop = time.perf_counter()

    print("Czas obliczeń przy użyciu sortowania kopcowego:", "{:.7f}\n\n".format(t_stop - t_start))

    print(selection_sort(deepcopy(lista_el)))


    t_start = time.perf_counter()
    selection_sort(deepcopy(lista_randomowa))
    t_stop = time.perf_counter()
    print("Czas obliczeń z użyciem 'Selection sort':", "{:.7f}".format(t_stop - t_start))

main()



#******************DODATKOWE**************************#
# from copy import deepcopy
# import random
# import time

# class Element:

#     def __init__(self, priorytet, value) -> None:
#         self.__dane = value
#         self.__priorytet = priorytet
    
#     def __repr__(self) -> str:
#         return "{0}:{1}".format(self.__priorytet, self.__dane)
    

#     def __lt__(self, other):
#         if self.__priorytet < other.__priorytet:
#             return True
#         return False
    
#     def __gt__(self, other):
#         if self.__priorytet > other.__priorytet:
#             return True
#         return False

# def Insertion_sort(lista):
#     for i in range(1,len(lista),1):
#         j = i - 1
#         idx_item = i
#         while lista[j] > lista[idx_item] and j >= 0:
#             lista[idx_item], lista[j] = lista[j], lista[idx_item]
#             idx_item -= 1
#             j -= 1

#     return lista


# def Shella_sort(lista, fun):
#     h = fun(len(lista))
#     while h > 0:
#         for zbior in range(h):
#             for i in range(zbior,len(lista),h):
#                 j = i - h
#                 idx_item = i
#                 while lista[j] > lista[idx_item] and j >= 0:
#                     lista[idx_item], lista[j] = lista[j], lista[idx_item]
#                     idx_item -= h
#                     j -= h
#         h = fun(h = h)  

#     return lista

# first_select_h = lambda h: h//2

# def second_select_h(N = None, h = None):
#     if h is None:
#         new_h = 0
#         k = 0
#         while new_h < N/3:
#             prev_new_h = new_h
#             new_h = (3**k-1)/2
#             k +=1
#             if new_h >= N/3:
#                 return int(prev_new_h)
#     else:
#         return h//3



# def main():
#     elementy = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
#     lista_el = [Element(el[0], el[1]) for el in elementy]
    
#     print(Insertion_sort(deepcopy(lista_el)))
#     print(Shella_sort(deepcopy(lista_el), second_select_h),"\n\n")

#     lista_randomowa = [int(random.random() * 100) for _ in range(10000)]
#     t_start = time.perf_counter()
#     Insertion_sort(deepcopy(lista_randomowa))
#     t_stop = time.perf_counter()
#     print("Czas obliczeń z użyciem 'Insertion sort':", "{:.7f}".format(t_stop - t_start))

#     t_start = time.perf_counter()
#     Shella_sort(deepcopy(lista_randomowa), first_select_h)
#     t_stop = time.perf_counter()
#     print("Czas obliczeń z użyciem metody Shella dla h = N//2:", "{:.7f}".format(t_stop - t_start))

#     t_start = time.perf_counter()
#     Shella_sort(deepcopy(lista_randomowa), second_select_h)
#     t_stop = time.perf_counter()
#     print("Czas obliczeń z użyciem metody Shella dla h obliczonego przy pomocy (3**k-1)/2:", "{:.7f}".format(t_stop - t_start))

#     print("Czas obliczeń w przypadku sortowania kopcowego z pierwszej cześci zadania: ", 0.1133636)

# main()







