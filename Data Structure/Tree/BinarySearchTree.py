# %%

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node: Node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        if data > node.data:
            node.right = self.insert(node.right, data)
        return node
    # in-order traversal
    def traverse(self,root:Node,mode="in-order"): 
        if root is not None:
            if mode=='in-order':
                self.traverse(root.left)
                print(root.data)
                self.traverse(root.right)
            if mode=='pre-order':
                print(root.data)
                self.traverse(root.left)
                self.traverse(root.right)
            if mode=='post-order':
                self.traverse(root.left)
                self.traverse(root.right)
                print(root.data)
    def height(self,root:Node):
        if root is None:
            return -1
        return max(self.height(root.right),self.height(root.left))+1

# %%
if __name__ == "__main__":
    tree = Tree()
    root = tree.createNode(5)
    # insert
    for val in [2,10,7,15,12,20,30,6,8]:
        tree.insert(root,val)
    print("In-order traversal------------------->")
    tree.traverse(root)
# %%
