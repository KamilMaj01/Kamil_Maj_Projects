
from typing import Union
# #****************************** CZĘŚĆ PODSTAWOWA***************************************#
# class Node:
#     def __init__(self, data, next = None) -> None:
#         self.data = data
#         self.next = next


# class LinkedList:

#     def __init__(self) -> None:
#         self.head = None

#     def __str__(self) -> str:
#         text = ""
#         if self.head is None:
#             return "brak elementów"
#         else:
#             SubNode = self.head
#             text += "-> {0}\n".format(SubNode.data)
#             while SubNode.next is not None:
#                 SubNode = SubNode.next
#                 text += "-> {0}\n".format(SubNode.data)
    
                
            
#         return text

#     def destroy(self) -> None:
#         self.head = None

#     def add(self, node: tuple) -> None:
#         if self.head is None:
#             self.head = Node(node)
#         else:
#             SubNode = Node(node)
#             self.head, SubNode.next = SubNode, self.head
    

#     def append(self, node : Node) -> None:

#         if self.head is None:
#             self.head = Node(node)
#         else:
#             SubNode = self.head
#             while SubNode.next is not None:
#                 SubNode = SubNode.next
            
#             SubNode.next = Node(node)


#     def remove(self) -> None:
#         if self.head is None:
#             raise AttributeError("Error: Lista jest pusta <- nie da się usunąć pierwszego elementu elementu")
#         else:
#             self.head = self.head.next

#     def remove_end(self) -> None:
#         if self.head is None:
#             raise AttributeError("Error: Lista jest pusta <- nie da się usunąć oststaniego elementu")
#         else:
#             SubNode = self.head
#             while SubNode.next is not None:
#                 PrevNode = SubNode
#                 SubNode = SubNode.next
#             PrevNode.next = None

#     def is_empty(self) -> bool:
#         if self.head is None:
#             return True
#         else:
#             return False
        
#     def lenght(self) -> int:
#         if self.head is None:
#             return 0
#         else:
#             count = 1
#             SubNode = self.head
#             while SubNode.next is not None:
#                 count += 1
#                 SubNode = SubNode.next
#         return count

#     def get(self) -> Node:
#         return self.head.data
    


# def main() ->None :
#     list = [('AGH', 'Kraków', 1919),
#             ('UJ', 'Kraków', 1364),
#             ('PW', 'Warszawa', 1915),
#             ('UW', 'Warszawa', 1915),
#             ('UP', 'Poznań', 1919),
#             ('PG', 'Gdańsk', 1945)] 
    
#     uczelnie  = LinkedList()

#     for idx, el in enumerate(list):
#         if idx < 3:
#             uczelnie.add(list[idx])
#         if idx == 3:
#             print(uczelnie,"\n\n")
#         if idx >= 3:
#             uczelnie.append(list[idx])
#     print(uczelnie)
#     print(uczelnie.lenght())
#     uczelnie.remove()
#     print(uczelnie.head.data,"\n")
#     uczelnie.remove_end()
#     print(uczelnie)

#     uczelnie.destroy()
#     print(uczelnie.is_empty())
#     try:
#         uczelnie.remove()
#     except AttributeError as err:
#         print(err)
#     try:
#         uczelnie.remove_end()
#     except AttributeError as err:
#         print(err)        
    
# main()


#****************************** CZĘŚĆ DODATKOWA***************************************#
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __str__(self, direction : str = "ehead") -> str:
        text = ""
        if self.head is None and self.tail is None:
            return None
        elif direction == "ehead":
            SubNode = self.head
            text += "-> {0}\n".format(SubNode.data)
            while SubNode.next is not None:
                SubNode = SubNode.next
                text += "-> {0}\n".format(SubNode.data)
        elif direction == "reverse":
            SubNode = self.tail
            text += "-> {0}\n".format(SubNode.data)
            while SubNode.prev is not None:
                SubNode = SubNode.prev
                text += "-> {0}\n".format(SubNode.data)
                   
        return text

    def destroy(self) -> None:
        self.head = None
        self.tail = None

    def add(self, node: tuple) -> None:
        NextNode = Node(node)
        if self.head is None and self.tail is None:
            self.head = NextNode
            self.tail = NextNode
        else:
            NextNode.next, self.head= self.head, NextNode
            SubNode = self.tail
            while SubNode.prev is not None:
                SubNode = SubNode.prev
            SubNode.prev = NextNode
    

    def append(self, node : Node) -> None:
        NextNode = Node(node)
        if self.head is None and self.tail is None:
            self.head = NextNode
            self.tail = NextNode
        else:
            NextNode.prev, self.tail= self.tail, NextNode
            SubNode = self.head
            while SubNode.next is not None:
                SubNode = SubNode.next
            SubNode.next = NextNode



    def remove(self) -> None:
        if self.head is None and self.tail is None:
            raise AttributeError("Error: Lista jest pusta <- nie da się usunąć pierwszego elementu elementu")
        else:
            self.head = self.head.next

            SubNode = self.tail
            while SubNode.prev is not None:
                NextNode = SubNode
                SubNode = SubNode.prev
            NextNode.prev = None


    def remove_end(self) -> None:
        if self.head is None and self.tail is None:
            raise AttributeError("Error: Lista jest pusta <- nie da się usunąć oststaniego elementu")
        else:
            self.tail = self.tail.prev

            SubNode = self.head
            while SubNode.next is not None:
                PrevNode = SubNode
                SubNode = SubNode.next
            PrevNode.next = None

    def is_empty(self) -> bool:
        if self.head is None and self.tail is None:
            return True
        else:
            return False
        
    def lenght(self) -> int:
        if self.head is None:
            return 0
        else:
            count = 1
            SubNode = self.head
            while SubNode.next is not None:
                count += 1
                SubNode = SubNode.next
        return count

    def get(self, idx : str = "first"):
        if idx == "first":
            return self.head.data
        elif idx == "end":
            return self.tail.data
        else:
            return None
    
    


def main() ->None :
    
    list = [('AGH', 'Kraków', 1919),
            ('UJ', 'Kraków', 1364),
            ('PW', 'Warszawa', 1915),
            ('UW', 'Warszawa', 1915),
            ('UP', 'Poznań', 1919),
            ('PG', 'Gdańsk', 1945)] 
    
    uczelnie = LinkedList()

    for idx, el in enumerate(list):
        if idx < 3:
            uczelnie.add(list[idx])
        if idx == 3:
            print(uczelnie,"\n\n")
        if idx >= 3:
            uczelnie.append(list[idx])
    print(uczelnie)
    print(uczelnie.lenght())
    uczelnie.remove()
    print(uczelnie.head.data,"\n")
    uczelnie.remove_end()
    print(uczelnie)

    uczelnie.destroy()
    print(uczelnie.is_empty())
    try:
        uczelnie.remove()
    except AttributeError as err:
        print(err)
    try:
        uczelnie.remove_end()
    except AttributeError as err:
        print(err)    
      
    
main()