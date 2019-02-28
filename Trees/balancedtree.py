from tree import Node

class RB_Node(Node):
    def __init__(self,data=None,parent=None,color=1):
        Node.__init__(self,data,parent)
        self.color = color

    def insert(self,data):
        if self.data == None:
            self.data = data
            self.color = 0
            return 
        self.breadth_first_print()
        print('\n')
        inserted = self._insert(data)
        case = inserted._check()
        inserted._fixer(case)

    
    def _insert(self,data):
        if data<self.data:
            if self.left:
                inserted = self.left._insert(data)
            else:
                inserted = self.left = RB_Node(data,self)
            return inserted
        elif data>self.data:
            if self.right:
                inserted = self.right._insert(data)
            else:
                inserted = self.right = RB_Node(data,self)
            return inserted
        else:
            return self.find(data)
    
    def _check(self):
        parent = self.parent
        grandparent = parent.parent
        if grandparent:
            if parent == grandparent.left:
                uncle = grandparent.right
            else:
                uncle = grandparent.left
        else:
            return -1
            # uncle = None
        if parent == None:
            return 0
        if uncle and uncle.color == 1:
            return 1
        if (uncle and uncle.color == 0) or uncle==None:
            #isline
            if (self == parent.left and parent == grandparent.left) or (self == parent.right and parent == grandparent.right):
                return 3
            #istriangle
            else:
                return 2

    def _fixer(self,case):   
        parent = self.parent
        grandparent = parent.parent
        if grandparent:
            if parent == grandparent.left:
                uncle = grandparent.right
            else:
                uncle = grandparent.left
        else:
            uncle = None
        if case == -1:
            return
            
        if case == 0:
            self.color = 0
            return
        if case == 1:
            parent.color = 1-parent.color
            grandparent.color = 1-grandparent.color
            uncle.color = 1-uncle.color
            return
        if case == 2:
            if self == parent.right:
                parent.leftrotate()
                return
            else:
                parent.rightrotate
                return
        if case == 3:
            if parent == grandparent.right:
                parent.color = 1-parent.color
                grandparent.color = 1-grandparent.color
                grandparent.leftrotate()
                return
            else:
                grandparent.rightrotate()
                return
        
    def _replace(self,node):
        self.data = node.data
        self.left = node.left
        self.right = node.right
        self.parent = node.parent
        self.color = node.color
    
    def _copy(self):
        return RB_Node(data = self.data,parent = self.parent,color = self.color)
if __name__ == "__main__":
    tree = RB_Node()
    arr = [0,1,2,3,4,5]
    for el in arr:
        tree.insert(el)
    # tree.right.right.leftrotate()
    print('~~~~~~~BreadthFirst~~~~~~~')
    # tree.in_order_print()
    tree.breadth_first_print()