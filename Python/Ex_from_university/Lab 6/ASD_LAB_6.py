# class Element:
#     def __init__(self, priorytet, value) -> None:
#         self.__dane = value
#         self.__priorytet = priorytet
    
#     def __str__(self) -> str:
#         return "{0}:{1}".format(self.__priorytet, self.__dane)
    

#     def __lt__(self, other):
#         if self.__priorytet < other.__priorytet:
#             return True
#         return False
    
#     def __gt__(self, other):
#         if self.__priorytet > other.__priorytet:
#             return True
#         return False

# class Queue:
#     def __init__(self) -> None:
#         self.size = 0
#         self.table = []


#     def is_empty(self):
#         if self.size == 0:
#             return True
#         return False


#     def peek(self):
#         if self.is_empty():
#             return None
        
#         return self.table[0]

#     def dequeue(self):
#         if self.is_empty():
#             return None
#         el_max_priorytet = self.table[0]
#         self.table[0], self.table[self.size-1] = self.table[self.size -1], self.table[0]
#         self.size -= 1
#         self.hepify_dequeue()
#         return el_max_priorytet
    
#     def hepify_dequeue(self):
#         idx_par = 0
#         if self.left(idx_par) <= self.size -1:
#             idx_left = self.left(idx_par)
#         else:
#             idx_left = None

#         if self.right(idx_par) <= self.size-1:
#             idx_right = self.right(idx_par)
#         else:
#             idx_right = None

#         while (idx_left is not None and self.table[idx_par] < self.table[idx_left]) or (idx_right is not None and self.table[idx_par] < self.table[idx_right]):
#             if idx_left is not None and self.table[idx_par] < self.table[idx_left] and self.table[idx_left] > self.table[idx_right]:
#                 self.table[idx_par], self.table[idx_left] = self.table[idx_left], self.table[idx_par]
#                 idx_par = idx_left
#             elif idx_right is not None and self.table[idx_par] < self.table[idx_right]:
#                 self.table[idx_par], self.table[idx_right] = self.table[idx_right], self.table[idx_par]
#                 idx_par = idx_right
            
#             if self.left(idx_par) <= self.size -1:
#                 idx_left = self.left(idx_par)
#             else:
#                 idx_left = None

#             if self.right(idx_par) <= self.size-1:
#                 idx_right = self.right(idx_par)
#             else:
#                 idx_right = None


#     def enqueue(self, elem):
#         if self.size == len(self.table):
#             self.table.append(elem)
#         else:
#             self.table[self.size] = elem
#         self.size += 1
#         self.heapify_enqueue(self.size -1)

#     def heapify_enqueue(self, idx_el):
#         idx_par = self.parent(idx_el)
#         while self.table[idx_par] < self.table[idx_el]:
#             self.table[idx_par], self.table[idx_el] = self.table[idx_el], self.table[idx_par]
#             idx_el = idx_par
#             idx_par = self.parent(idx_el)




#     def left(self,index):
#         return 2*index +1
    
#     def right(self, index):
#         return 2*index+2

#     def parent(self,index):
#         return abs((index -1))//2

#     def print_tab(self):
#         print ('{', end=' ')
#         print(*self.table[:self.size], sep=', ', end = ' ')
#         print( '}')

#     def print_tree(self, idx, lvl):
#         if idx<self.size:           
#             self.print_tree(self.right(idx), lvl+1)
#             print(2*lvl*'  ', self.table[idx] if self.table[idx] else None)           
#             self.print_tree(self.left(idx), lvl+1)


# def main():
#     kolejka  = Queue()
#     kolejka.enqueue(Element(7,'G'))
#     kolejka.enqueue(Element(5,'R'))
#     kolejka.enqueue(Element(1,'Y'))
#     kolejka.enqueue(Element(2,'M'))
#     kolejka.enqueue(Element(5,'O'))
#     kolejka.enqueue(Element(3,'T'))
#     kolejka.enqueue(Element(4,'Y'))
#     kolejka.enqueue(Element(8,'L'))
#     kolejka.enqueue(Element(9,'A'))
#     kolejka.print_tab()
#     kolejka.print_tree(0,0)
#     first = kolejka.dequeue()
#     print(kolejka.peek())
#     kolejka.print_tab()
#     print(first)
#     while not kolejka.is_empty():
#         print(kolejka.dequeue())
#     kolejka.print_tab()
    
# main()

# ***************DODATKOWE****************#

class Node:
    def __init__(self,number_of_children) -> None:
        self.size = number_of_children -1
        self.keys = [None for el in range(number_of_children -1)]
        self.children = [None for el in range(number_of_children)]

class B_tree:
    def __init__(self, number_of_children) -> None:
        self.number_of_children = number_of_children
        self.size = number_of_children -1
        self.root = None

    def insert(self,key, node = None):
        if self.root is None:
            self.root = Node(self.number_of_children)
            self.root.keys[0] = key
            return None
        
        if node is None:
            node = self.root
        i = 0
        while i<=self.size:
            if node.keys[i] is None or key < node.keys[i]:
                if node.children[i] is None:
                    Subkey = self._add(node, key, i)
                    return node, Subkey
                elif node.children[i] is not None:
                    node.children[i], Subkey = self.insert(node.children[i])
                    if Subkey is not None:
                        Subkey = self._add(node,Subkey,i)
                    return node,Subkey
                
            elif node.keys[-1] is not None and key > node.keys[-1]:
                if node.children[-1] is None:
                    Subkey = self._add(node, key, -1)
                    return node, Subkey
                else:
                    node.children[-1], Subkey = self.insert(node.children[-1])
                    if Subkey is not None:
                        Subkey = self._add(node,Subkey,i)
                    return node,Subkey
            i += 1

        

    def _add(self, node : Node, key, i):
        if node.keys[i] is None:
            node.keys[i] = key
            return None
        elif node.keys[i] is not None:
            if None in node.keys[i:]:
                node.keys[i+1:] = node.keys[i:-1]
                node.keys[i] = key
                return None
            else:
                Subkey = node.keys[self.size//2]
                if i < self.size//2:
                    node.keys[i+1:self.size//2+1] = node.keys[i:self.size//2]
                    node.children[i+1:self.size//2+1] = node.children[i:self.size//2]
                    node.keys[i - 1] = key
                elif i > self.size//2:
                    print(node.keys)
                    Subnode = Node(self.number_of_children)
                    node.keys[self.size//2:i] = node.keys[self.size//2+1:]
                    node.children[self.size//2:i] = node.children[self.size//2:]
                    node.keys[i - 1] = key
                    if key > node.keys[self.size//2]:
                        Sublist = node[self.size//2 :]
                        Subnode[:len(Sublist)] = Sublist
                    



                print(node.keys)
                
                return Subkey




    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node!=None:
            for i in range(node.size+1): 	                	
                self._print_tree(node.children[i], lvl+1)
                if i<node.size:
                    print(lvl*'  ', node.keys[i])	


    
def main():
    lita = [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]
    drzewo = B_tree(4)
    drzewo.insert(5)
    drzewo.insert(17)
    drzewo.insert(2)
    drzewo.insert(14)
    drzewo.print_tree()

main()
