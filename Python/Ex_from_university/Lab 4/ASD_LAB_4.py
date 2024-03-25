from copy import deepcopy
class Element:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
    
    def __str__(self) -> str:
        return "{{{0}:{1}}}".format(self.key,self.value)

class MixTable:
    def __init__(self, size : int, c1 = 1, c2 = 0) -> None:
        self.table = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2
    
    def __str__(self) -> str:
        text = ""
        for el in self.table:
            text += " {0} ".format(el)
        return text


    def search(self, key : int) -> Element:
        index = self.transform(key)
        if self.table[index] is not None and self.table[index].key == key:
            return self.table[index].value
        else:
            for i in range(0, self.size):
                new_index = (index + self.c1*i + self.c2 * i**2) % self.size
                if self.table[new_index] is not None and self.table[new_index].key == key:
                    return self.table[new_index].value
            return None

        
    def insert(self, key, value) -> None:
        object = Element(key, value)

        index = self.transform(object.key) % self.size
     
        i = 0
        new_index = index
        while self.table[new_index] is not None and self.table[new_index].key != key:
            i += 1
            new_index = (index + self.c1*i + self.c2 * i**2) % self.size

            if i>0 and index == new_index:
                raise KeyError("Brak miejsca")
            
        self.table[new_index] = object
            
            
    
        
    def remove(self,key) -> None:
        index = self.transform(key)
        
        if self.table[index] is not None and self.table[index].key == key:
            self.table[index] = None
        else:
            for i in range(0, self.size):
                new_index = (index + self.c1*i + self.c2 * i**2) % self.size
                if self.table[new_index] is not None and self.table[new_index].key == key:
                    self.table[new_index] = None
                 
            raise KeyError('Brak danej')

                
        

    def transform(self, key) -> int:
        if isinstance(key,str):   
            result = (sum([ord(el) for el in key])) % self.size
        else:
            result = key % self.size
        return result

def main() -> None:

    def PIERWSZA_FUNKCJA(size,c1 = None, c2 = None) -> None:
        if c1 is None and c2 is None:
            tablica = MixTable(size)
        else:
            tablica = MixTable(size,c1,c2)
            
        litera = ord('A')
        for idx in range(1,16):
            if idx == 6:
                try:
                    tablica.insert(18,chr(litera))
                except KeyError as er:
                    print(er)
            elif idx == 7:
                try:
                    tablica.insert(31,chr(litera))
                except KeyError as er:
                    print(er)
            else:
                try:
                    tablica.insert(idx,chr(litera))
                except KeyError as er:
                    print(er)
            litera += 1

        print(tablica,"\n")

        for el in [5,14]:
            print(tablica.search(el))
        try:
            tablica.insert(5,'Z')
        except KeyError as err:
            print(err)
        print(tablica.search(5))
        
        try:
            tablica.remove(5)
        except KeyError as err:
            print(err)

        print(tablica)
        print(tablica.search(31))

        try:
            tablica.insert("test",'W')
        except KeyError as err:
            print(err)

        print(tablica)


    def DRUGA_FUNKCJA(size,c1 = None, c2 = None) -> None:
        if c1 is None and c2 is None:
            tablica1 = MixTable(size)
        else:
            tablica1 = MixTable(size,c1,c2)
        litera1 = ord('A')
        
        for idx in range(1,16):
            try:
                tablica1.insert(idx*13,chr(litera1))
            except KeyError as er:
                print(er)
            litera1 += 1
        
        print(tablica1)


    PIERWSZA_FUNKCJA(13)
    print("\n")
    DRUGA_FUNKCJA(13)
    print("\n")
    DRUGA_FUNKCJA(13,0,1)
    print("\n")
    PIERWSZA_FUNKCJA(13,0,1)

main()

  
# **************DODATKOWE****************#
# from random import random

# class Element:
#     def __init__(self, level, key = None, value = None ) -> None:
#         if key is not None and value is not None:
#             self.key = key
#             self.value = value
#         self.level = level
#         self.next = [None for i in range(self.level)]

    
#     def __str__(self) -> str:
#         return "({0}:{1})".format(self.key,self.value)


# class SkipList:
#     def __init__(self, MaxLevel = None) -> None:
#         if MaxLevel is None:
#             self.maxlevel = 100
#             self.maxlevel = self.RandomLevel(p = 0.9)
#         else:
#             self.maxlevel = MaxLevel
#         self.head = Element(self.maxlevel)

#     def RandomLevel(self, p = 0.5, Mlevel = None):
#         lvl = 1   
#         while random() < p and lvl < self.maxlevel:
#             lvl = lvl + 1
#         return lvl
    
#     def __str__(self) -> str:
#         node = self.head.next[0]      
#         text = ""                      
#         while(node != None):
#             text += "{0} ".format(node)
#             node = node.next[0]

#         return text

#     def search(self,key):
#         node = self.head.next[0]
#         while node.key != key:
#             node = node.next[0]
#             if node is None:
#                 return None
#         return node.value


#     def  insert(self, key , value):
        
#         nodes = []  
#         nodes.append(self.head)
#         for lvl in range(self.maxlevel - 1, -1,-1):
#             node = nodes[-1].next[lvl]
#             while node is not None and node.key <= key:
#                 nodes.append(node)
#                 node = node.next[lvl]
        
#         if nodes[-1] != self.head and nodes[-1].key == key:
#             nodes[-1].value = value
#         else:
#             new_node = Element(self.RandomLevel(),key,value)
#             self.connectNode(new_node,nodes)
    
#     def connectNode(self, new_node : Element,nodes : list[Element]):
#         index = -1
#         for idx, el in enumerate(new_node.next):
#             while nodes[index].level - 1 < idx:
#                 index = index - 1
#             if nodes[index].level - 1 >= idx:
#                 new_node.next[idx], nodes[index].next[idx] = nodes[index].next[idx] ,new_node
            

#     def remove(self,key):
#         nodes = []  
#         nodes.append(self.head)
#         for lvl in range(self.maxlevel - 1, -1,-1):
#             node = nodes[-1].next[lvl]
#             while node is not None and node.key < key:
#                 nodes.append(node)
#                 node = node.next[lvl]
        
#         index = -1
#         for idx, el in enumerate(node.next):
#             while nodes[index].level - 1 < idx:
#                 index = index - 1
#             if nodes[index].level - 1 >= idx:
#                 nodes[index].next[idx] = node.next[idx]



#     def displayList_(self):
#         node = self.head.next[0]            # pierwszy element na poziomie 0
#         keys = []                           # lista kluczy na tym poziomie
#         while(node != None):
#             keys.append(node.key)
#             node = node.next[0]

#         for lvl in range(self.maxlevel-1, -1, -1):
#             print("{}: ".format(lvl), end=" ")
#             node = self.head.next[lvl]
#             idx = 0
#             while(node != None):                
#                 while node.key>keys[idx]:
#                     print("  ", end=" ")
#                     idx+=1
#                 idx+=1
#                 print("{:2d}".format(node.key), end=" ")     
#                 node = node.next[lvl]    
#             print("")

# def main():
#     lista  = SkipList(6)
#     litera = ord('A')
#     for idx in range(1,16):
#         lista.insert(idx,chr(litera))
#         litera += 1

#     lista.displayList_()
#     print(lista.search(2))
#     lista.insert(2,"Z")
#     print(lista.search(2),"\n")
    
#     for el in [5,6,7]:
#         lista.remove(5)
        
#     print(lista)
#     print()
#     lista.insert(6,"W")
#     print(lista)
#     print("\n\n")

#     lista1  = SkipList(6)
#     litera = ord('A')
#     for idx in range(15,0,-1):
#         lista1.insert(idx,chr(litera))
#         litera += 1

#     lista1.displayList_()
    
#     print(lista1.search(2))
#     lista1.insert(2,"Z")
#     print(lista1.search(2),"\n")

#     for el in [5,6,7]:
#         lista1.remove(5)
    
#     print(lista1)
#     print()
#     lista1.insert(6,"W")
#     print(lista1)

# main()