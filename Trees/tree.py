from collections import deque
class Node:

    def __init__(self,data,parent=None):
        self.data = data
        self.left = self.right = None
        self.parent = parent

    def insert(self,data):
        if data<self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data,self)
        elif data>self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data,self)
        else:
            return
    
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.data)
        if self.right:
            self.right.in_order_print()

    def pre_order_print(self):
        print(self.data)
        if self.left:
            self.left.pre_order_print()
        if self.right:
            self.right.pre_order_print()
    
    def post_order_print(self):
        if self.left:
            self.left.post_order_print()
        if self.right:
            self.right.post_order_print()
        print(self.data)

    def breadth_first_print(self):
        q = deque()
        q.append(self)
        while(len(q)>0):
            popped = q.popleft()
            print(popped.data)
            if popped.left:
                q.append(popped.left)
            if popped.right:
                q.append(popped.right)
    def find(self,data):
        if data==self.data:
            return self
        elif data<self.data:
            if self.left:
                return self.left.find(data)
            else:
                print('Not Found')
        elif data>self.data:
            if self.right:
                return self.right.find(data)
            else:
                print('Not Found')

    def minimum(self):
        if self.left:
            return self.left.minimum()
        else:
            return self

    def maximum(self):
        if self.right:
            return self.right.maximum()
        else:
            return self

    def sucessor(self,data):
        node = self.find(data)
        if node is None:
            return 'Not Found'
        if node.right:
            return node.right.minimum()
        parent = node.parent
        while parent and parent.right is node:
            node = parent
            parent = parent.parent
        return parent

    def _sucessor(self,node):
        if node is None:
            return 'Not Found'
        if node.right:
            return node.right.minimum()
        parent = node.parent
        while parent and parent.right is node:
            node = parent
            parent = parent.parent
        return parent

    def predecessor(self,data):
        node = self.find(data)
        if node is None:
            return 'Not Found'
        if node.left:
            return node.left.maximum()
        parent = node.parent
        while parent and parent.left is node:
            node = parent
            parent = parent.parent
        return parent

    def _transplant(self,node,rnode):
        if node.parent:
            if node==node.parent.left:
                node.parent.left = rnode
            else:
                node.parent.right = rnode
        else:
            node.data = rnode.data
        if rnode:
            rnode.parent = node.parent

    def delete(self,data):
        node = self.find(data)
        if node is None:
            return 'Not Found'
        if node.left and node.right:
            sucessor = self._sucessor(node)
            rnode = self._delete(sucessor)
            rnode.right = node.right
            rnode.left = node.left
            self._transplant(node,rnode)
            return node
        if node.right:
            self._transplant(node,node.right)
            return node
        if node.left:
            self._transplant(node,node.left)
            return node
        self._transplant(node,None)

    def _delete(self,node):
        if node is None:
            return 'Not Found'
        if node.left and node.right:
            sucessor = self._sucessor(node)
            rnode = self._delete(sucessor)
            self._transplant(node,rnode)
            return node
        if node.right:
            self._transplant(node,node.right)
            return node
        if node.left:
            self._transplant(node,node.left)
            return node
        self._transplant(node,None)
        return node

    def __str__(self):
        return 'data: ' + str(self.data)

    def rightrotate(self):
        if self.left:
            _temp = self.left
            self.left = _temp.right
            _temp.right = self
            _temp.parent = self.parent
            if self.parent:
                if self == self.parent.right:
                    self.parent.right = _temp
                else:
                    self.parent.left = _temp
            else:
                self._replace(_temp._copy())
        return

    def leftrotate(self):
        if self.right and self.parent:
            _temp = self.right
            self.right = _temp.left
            _temp.left = self
            _temp.parent = self.parent
            if self == self.parent.right:
                self.parent.right = _temp
            else:
                self.parent.left = _temp
        else: 
            _temp = self.right._copy()
            scopy = self._copy()
            _temp.left = scopy
            _temp.parent = self.parent
            self._replace(_temp)

                
        return

    def _replace(self,node):
        self.data = node.data
        self.left = node.left
        self.right = node.right
        self.parent = node.parent

    def _copy(self):
        return Node(self.data,self.parent)
if __name__ == "__main__":
    tree = Node(10)
    arr = [8,13,11,5,9,15]
    for el in arr:
        tree.insert(el)
    print('~~~~~~~InOrder~~~~~~~')
    tree.in_order_print()
    print('\n~~~~~~~PreOrder~~~~~~~')
    tree.pre_order_print()
    print('\n~~~~~~~PostOrder~~~~~~~')
    tree.post_order_print()
    print('\n~~~~~~~Find~~~~~~~')
    print(tree.find(11))
    print(tree.find(15))
    print(tree.find(14))
    print('\n~~~~~~~Min~~~~~~~')
    print(tree.minimum())
    print('\n~~~~~~~Sucessor~~~~~~~')
    print(tree.sucessor(5))
    print(tree.sucessor(8))
    print(tree.sucessor(9))
    print(tree.sucessor(11))
    print(tree.sucessor(15))
    print('\n~~~~~~~Predecessor~~~~~~~')
    print(tree.predecessor(5))
    print(tree.predecessor(8))
    print(tree.predecessor(9))
    print(tree.predecessor(11))
    print(tree.predecessor(15))
    print('\n~~~~~~~Delete~~~~~~~')
    tree.delete(13)
    tree.in_order_print()
