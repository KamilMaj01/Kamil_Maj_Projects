# class Node:
#     def __init__(self, key, value) -> None:
#         self.key = key
#         self.value = value
#         self.left = None
#         self.right = None

# class Tree:
#     def __init__(self) -> None:
#         self.root = None

#     def __str__(self) -> str:
#         result = self.str(self.root,"")
#         return result
#     def str(self, node : Node, text : str):
#         if node is not None:
#             text = self.str(node.left, text)
#             text += "{0} {1},".format(node.key,node.value)
#             text = self.str(node.right, text)
#             return text
#         return text

#     def search(self,key):
#         return self.Subsearch(self.root,key)
    
#     def Subsearch(self,node : Node,key):
#         if node == None:
#             return None
#         if key < node.key:
#             return self.Subsearch(node.left,key) 
#         elif key > node.key:
#             return self.Subsearch(node.right,key)
#         else:
#             return node.value


#     def insert(self, key,value):
#         if self.root is None:
#             self.root = Node(key,value)
#         else:
#             self.Subinsert(self.root,key, value)
            
#     def Subinsert(self,node : Node, key, value):
#         if node is None:
#             return Node(key,value)
#         if key < node.key:
#             node.left = self.Subinsert(node.left,key,value)
#             return node
#         elif key > node.key:
#             node.right = self.Subinsert(node.right,key,value)
#             return node
#         else:
#             node.value = value
#             return node

#     def delete(self,key):
#         self.Subdelete(self.root,key)
           
#     def Subdelete(self,node : Node, key):
#         if key < node.key:
#             node.left = self.Subdelete(node.left,key)
#             return node
#         elif key > node.key:
#             node.right = self.Subdelete(node.right,key)
#             return node
#         else:
#             if node.right is None and node.left is None:
#                 return None
#             elif node.right is None and node.left is not None:
#                 return node.left
#             elif node.right is not None and node.left is None:
#                 return node.right
#             else:
#                 PrevSubnode = node
#                 Subnode = node.right
#                 while Subnode.left is not None:
#                     PrevSubnode = Subnode
#                     Subnode = Subnode.left
#                 node.value = Subnode.value
#                 node.key = Subnode.key
#                 if PrevSubnode == node:
#                     PrevSubnode.right = Subnode.right
#                 elif PrevSubnode != node and Subnode.right is None:  
#                     PrevSubnode.left = None
#                 else:
#                     PrevSubnode.left = Subnode.right
#                 return node

            

#     def print(self):
#         print("==============")
#         self._print_tree(self.root, 0)
#         print("==============")

#     def _print_tree(self, node : Node, lvl):
#         if node!=None:
#             self._print_tree(node.right, lvl+5)

#             print()
#             print(lvl*" ", node.key, node.value)
     
#             self._print_tree(node.left, lvl+5)

#     def height(self):
#         return self.Subheight(self.root, 0, 0)

#     def Subheight(self, node : Node, lvl, maxlevel):
#         if node is not None:
#             lvl += 1
#             maxlevel = self.Subheight(node.left, lvl, maxlevel)
#             if lvl > maxlevel:
#                 maxlevel = lvl
#             maxlevel = self.Subheight(node.right, lvl, maxlevel)
#             if lvl > maxlevel:
#                 maxlevel = lvl
#             return maxlevel
#         return maxlevel


# def main():
#     drzewo  = Tree()
#     litera = ord('A')
#     for idx in [50,15,62,5,20,58,91,3,8,37,60,24]:
#         drzewo.insert(idx,chr(litera))
#         litera += 1

#     drzewo.print()
#     print(drzewo)
#     print(drzewo.search(24))
#     drzewo.insert(20,"AA")
#     drzewo.insert(6,"M")
#     drzewo.delete(62)
#     drzewo.insert(59,"N")
#     drzewo.insert(100,"P")
#     drzewo.delete(8)
#     drzewo.delete(15)
#     drzewo.insert(55,"R")
#     drzewo.delete(50)
#     drzewo.delete(5)
#     drzewo.delete(24)
    
#     print(drzewo)
#     drzewo.print()
 
# main()



#**********************DODATKOWE*******************#

class Node:
    def __init__(self, key, value, alig = 0) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.alig = alig
        self.height = 0

class Tree:
    def __init__(self, *args, **kwargs) -> None:
        self.root = None

    def __str__(self) -> str:
        result = self.str(self.root,"")
        return result
    def str(self, node : Node, text : str):
        if node is not None:
            text = self.str(node.left, text)
            text += "{0} {1},".format(node.key,node.value)
            text = self.str(node.right, text)
            return text
        return text

    def search(self,key):
        return self.Subsearch(self.root,key)
    
    def Subsearch(self,node : Node,key):
        if node == None:
            return None
        if key < node.key:
            return self.Subsearch(node.left,key) 
        elif key > node.key:
            return self.Subsearch(node.right,key)
        else:
            return node.value


    def insert(self, key,value):
        if self.root is None:
            self.root = Node(key,value)
        else:
            self.root = self.Subinsert(self.root,key, value)

            
    def Subinsert(self,node : Node, key, value):
        if node is None:
            return Node(key,value)
        if key < node.key:
            node.left = self.Subinsert(node.left,key,value)
            self.SetAligment(node)
            next_node = AVL.rotation(self,node)
            return next_node
        elif key > node.key:
            node.right = self.Subinsert(node.right,key,value)
            self.SetAligment(node)
            next_node = AVL.rotation(self,node)
            return next_node
        else:
            node.value = value
            return node

    def SetAligment(self, node : Node):
        if node.right is None and node.left is not None:
            node.height = node.left.height + 1
            node.alig =  node.height
        elif node.left is None and node.right is not None:
            node.height = node.right.height + 1
            node.alig =  - node.height
        elif node.right is None and node.left is None:
            node.height = 0
            node.alig = 0
        else:
            if node.right.height < node.left.height:
                node.height = node.left.height + 1
        
            elif node.right.height > node.left.height:
                node.height = node.right.height + 1
            else:
                node.height = node.left.height + 1
            node.alig = node.left.height - node.right.height


    def delete(self,key):
        self.root = self.Subdelete(self.root,key)
           
    def Subdelete(self,node : Node, key):
        if key < node.key:
            node.left = self.Subdelete(node.left,key)
            self.SetAligment(node)
            next_node = AVL.rotation(self,node)
            return next_node
        elif key > node.key:
            node.right = self.Subdelete(node.right,key)
            self.SetAligment(node)
            next_node = AVL.rotation(self,node)
            return next_node
        else:
            if node.right is None and node.left is None:
                return None
            elif node.right is None and node.left is not None:
                return node.left
            elif node.right is not None and node.left is None:
                return node.right
            else:
                PrevSubnode = node
                Subnode = node.right
                while Subnode.left is not None:
                    PrevSubnode = Subnode
                    Subnode = Subnode.left
                node.value = Subnode.value
                node.key = Subnode.key
                if PrevSubnode == node:
                    PrevSubnode.right = Subnode.right
                elif PrevSubnode != node and Subnode.right is None:  
                    PrevSubnode.left = None
                else:
                    PrevSubnode.left = Subnode.right

                self.SetAligment(PrevSubnode)
                self.SetAligment(node)
                next_node = AVL.rotation(self,node)
                
                return next_node
           
    def print(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node : Node, lvl):
        if node!=None:
            self._print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self._print_tree(node.left, lvl+5)

    def height(self):
        return self.Subheight(self.root, 0, 0)

    def Subheight(self, node : Node, lvl, maxlevel):
        if node is not None:
            lvl += 1
            maxlevel = self.Subheight(node.left, lvl, maxlevel)
            if lvl > maxlevel:
                maxlevel = lvl
            maxlevel = self.Subheight(node.right, lvl, maxlevel)
            if lvl > maxlevel:
                maxlevel = lvl
            return maxlevel
        return maxlevel


class AVL(Tree):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(self, *args, **kwargs)
        

    def rotation(self, node:Node):
        if node.alig < -1:
            if node.right.alig < 0:
                node = self.RR(node)
            elif node.right.alig > 0:
                node = self.RL(node)
        elif node.alig > 1:
            if node.left.alig > 0:
                node = self.LL(node)
            elif node.left.alig < 0:
                node = self.LR(node)
        return node

    def LL(self,node : Node):
        Subnode = node.left
        node.left = Subnode.right
        Subnode.right = node
        self.SetAligment(Subnode.right)
        self.SetAligment(Subnode)
        
        return Subnode


    def RR(self, node : Node):
        Subnode = node.right
        node.right = Subnode.left
        Subnode.left = node
        self.SetAligment(Subnode.left)
        self.SetAligment(Subnode)

        return Subnode

    def RL(self, node : Node):
        new_node = self.LL(node.right)
        node.right = new_node
        new_node = self.RR(node)
        return new_node
        
    def LR(self, node : Node):
        new_node = self.RR(node.left)
        node.left = new_node
        new_node = self.LL(node)
        return new_node
        

def main():
    drzewo  = AVL()
    for key, value in {50:'A', 15:'B', 62:'C', 5:'D', 2:'E', 1:'F', 11:'G', 100:'H', 7:'I', 6:'J', 55:'K', 52:'L', 51:'M', 57:'N', 8:'O', 9:'P', 10:'R', 99:'S', 12:'T'}.items():
        drzewo.insert(key, value)
   
    drzewo.print()
    print(drzewo)
    print(drzewo.search(10))

    drzewo.delete(50)
    drzewo.delete(52)
    drzewo.delete(11)
    drzewo.delete(57)
    drzewo.delete(1)
    drzewo.delete(12)
    drzewo.insert(3, "AA")
    drzewo.insert(4, "BB")
    drzewo.delete(7)
    drzewo.delete(8)
    drzewo.print()
    print(drzewo)
 
main()
