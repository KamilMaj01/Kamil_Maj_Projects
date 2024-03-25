
#******************************PODSTAWOWE******************************#
# class Queue:
#     def __init__(self, size = 5) -> None:
#         self.table = [None for i in range(size)]
#         self.size = size
#         self.write = 0
#         self.read = 0

#     def __str__(self) -> str:
#         text = "["
#         idx = self.read
#         while idx != self.write:
#             if idx < self.size -1:
#                 text += " {0} ".format(self.table[idx])
#                 idx += 1
#             else:
#                 text += " {0} ".format(self.table[idx])
#                 idx = 0
#         text += "]"
#         return text
    
#     def is_empty(self) -> bool:
#         if self.read == self.write:
#             return True
#         else:
#             return False
        
#     def peek(self):
#         if self.is_empty():
#             return None
#         else:
#             return self.table[self.read]
        
#     def dequeue(self):
#         if self.is_empty():
#             return None
#         else:
#             result = self.table[self.read]
#             self.table[self.read] = None
#             if self.read != self.size - 1:
#                 self.read += 1
#             else:
#                 self.read = 0
#             return result
        

#     def enqueue(self, element) -> None:
#         self.table[self.write] = element
#         self.write = (self.write + 1) % self.size
#         if self.write == self.read:
#             self.realloc()

  


#     def realloc(self) -> None:
#         NewSize = 2*self.size
#         self.table = [self.table[i] if i < self.write else self.table[i-self.size] if i>=self.write +self.size else None for i in range(NewSize)]
#         self.read = self.size + self.write
#         self.size = NewSize

#     def get_table(self) -> list:
#         return self.table
    
# def main() -> None:
#     Lista = Queue()

#     for i in range(1,5):
#         Lista.enqueue(i)

#     print(Lista.dequeue())
#     print(Lista.peek())
#     print(Lista)

#     for i in range(5,9):
#         Lista.enqueue(i)
#     print(Lista.get_table())

#     while not Lista.is_empty():
#         Lista.dequeue()

#     print(Lista)
# main()
#**********************************************************************#



#******************************DODATKOWE******************************#

size = 6

class Element:
    def __init__(self) -> None:
        self.table = [None for i in range(size)]
        self.filling = 0
        self.next = None
    
    def add(self, element, index:int) -> None:

        if self.filling != size:
            self.table = [self.table[i] if i<index else element if i == index else self.table[i-1] for i in range(size)]
            self.filling += 1
            
        else:
            if self.next is None:
                self.next = Element()
            else:
                SubNodes = self.next
                self.next = Element()
                self.next.next = SubNodes
            
            self.next.table[0:int(size/2)] = self.table[int(-size/2):]
            self.filling -= 3
            self.next.filling += 2
        
            for idx in range(int(size/2),size):
                self.table[idx] = None
     
            if index >= self.filling:
                index -= self.filling
                self.next.add(element,index)
                self.next.filling += 1
            else:
                print(index)
                self.add(element,index)
                self.filling += 1

    def dele(self, index:int) -> None:
        if self.filling == 0:
            return None
        else:
            self.table[index] = None
            self.table[index:-1] = self.table[index+1:]
            self.filling -= 1
        
        if self.filling < size/2:
            i = 0
            while self.table[i] is not None:
                i+=1
            self.table[i] = self.next.table[0]
            self.next.table[:-1]  = self.next.table[1:]
            self.next.table[-1] = None
            self.next.filling -= 1
            self.filling += 1
            if self.next.filling < size/2:
                self.table[i+1:i+3] = self.next.table[0:2]
                self.filling += self.next.filling
                SubNode = self.next
                self.next = SubNode.next



class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        text = "["
        SubNode = self.head
        for el in SubNode.table:
                if el is not None:
                    text += " {0} ".format(el)

        while SubNode.next is not None:
            SubNode = SubNode.next
            for el in SubNode.table:
                if el is not None:
                    text += " {0} ".format(el)
            
        text += "]"
        return text
    
    def get(self,index :int):
        if self.head is None:
            return None
        
        SubElement = self.head
        while index >= SubElement.filling:
            index -= SubElement.filling
            if SubElement.next is None:
                return None
            SubElement = SubElement.next
        
        return SubElement.table[index]

    def insert(self, element, index : int) -> None:

        if self.head is None:
            self.head = Element()
            self.head.add(element,0)
        else:
            SubNode = self.head
            amount_elements = 0
            while SubNode.next is not None:
                amount_elements += SubNode.filling
                SubNode = SubNode.next

            
            if index >= amount_elements:
                SubNode = self.head
                while SubNode.next is not None:
                    SubNode = SubNode.next
                
                SubNode.add(element,index - amount_elements)
                
            else:
                SubNode = self.head
                while index > SubNode.filling:
                    index -= SubNode.filling
                    SubNode = SubNode.next
                    
                SubNode.add(element, index)

                
    def delete(self,index : int) -> None:
        if self.head is None:
            return None
        SubNode = self.head
        while index > SubNode.filling:
            index -= SubNode.filling
            SubNode = SubNode.next
        SubNode.dele(index)


def main():
    Lista = LinkedList()

    for i in range(1,10):
        Lista.insert(i,i-1)

    print(Lista.get(4))

    Lista.insert(10,1)
    Lista.insert(11,8)

    print(Lista)

    Lista.delete(1)
    Lista.delete(2)
   
    print()
    print(Lista)

main()
