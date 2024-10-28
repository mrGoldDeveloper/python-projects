class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def add(self,data):
            self.root=self._add(data,self.root)
    def _add(self,data,node):
        if not node:
            return Node(data)
        if data<node.data:
            node.left=self._add(data,node.left)
        elif data>node.data:
            node.right=self._add(data,node.right)
        return node
    def removeval(self,data):
        if not self.root:
            print("root of the tree is empty")
            return
        if self.root.data==data:
            self.root=None
            return
        self._remove(data,self.root)
    def _remove(self,data,node):
        if node.left and node.left.data==data:
            node.left=None
            return
        if node.right and node.right.data==data:
            node.right=None
            return
        if data<node.data:
            if node.left:
                self._remove(data,node.left)
        else:
            if node.right:
                self._remove(data,node.right)
    def display(self):
        result=[]
        d={1:'self.inorder(self.root,result)',2:'self.preorder(self.root,result)',3:'self.postorder(self.root,result)'}
        a=d[int(input("1:inorder,2:preorder,3:postorder:-"))]
        eval(a)
        print(result)
    def inorder(self,node,result):#left,current,right
        if not node:
            return None
        self.inorder(node.left,result)
        result.append(node.data)
        self.inorder(node.right,result)
    def preorder(self,node,result): #current,left,right
        if not node:
            return None
        result.append(node.data)
        self.preorder(node.left,result)
        self.preorder(node.right,result)
    def postorder(self,node,result):#left,right,current
        if not node:
            return None
        self.postorder(node.left,result)
        self.postorder(node.right,result)
        result.append(node.data)
    def search(self,data):
        if not self.root:
            print("root of the tree is empty")
            return
        if self.root.data==data:
            print("True")
            return
        print("True") if self._search(data,self.root) else print("False")

    def _search(self,data,node):
        if node and node.data==data:
            return node
        if node.left and data<node.data:
                return self._search(data,node.left)
        elif node.right and data>node.data:
            return self._search(data,node.right)

    def printd(self,d=0,node=None):
        if self.root is None:
            print("root of the tree is empty")
            return
        if node is None:
            node=self.root
        print("  "*d,node.data)
        if node.left:
            self.printd(d+1,node.left)
        if node.right:
            self.printd(d+1,node.right)
bt=BST()
bt.add(10)
bt.add(4)
bt.add(3)
bt.add(5)
bt.add(13)
bt.add(12)
bt.add(14)

bt.search(14)

bt.display()