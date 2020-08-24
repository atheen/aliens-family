class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def get_data(self):
        return self.data

    def get_children(self):
        return self.right,self.left

    def get_parent(self):
        return self.parent

# checks if "key" value is available in the "node" tree
    def check_exist(self,node,key):
        if node == None:
            return None
        if node.data == key:
            return node
        res1 = self.check_exist(node.left,key)
        if res1 != None:
            return res1
        res2 = self.check_exist(node.right,key)
        return res2

    def set_parent(self,root,name):
        family = name.split(" ")
        parent = family[1]
        parent_node = self.check_exist(root,parent)
        if parent_node != None:
            parent_node.add_child(self)
            self.parent = parent_node
        else:
            print("parent does not exist")

    def add_child(self,node):
        if self.left == None:
            self.left = node
            print("added a child to the left of %s"%(self.data))
        elif self.right == None:
            self.right = node
            print("added a child to the right of %s"%(self.data))
        else:
            print("child is an orphan")


root = TreeNode("family")
child = input("enter child full name(done if finished): ")

while child != "done":
    first_name = child.split(" ")
    child_node = TreeNode(first_name[0])
    child_node.set_parent(root,child)
    print("-"*40)
    child = input("enter child full name(done if finished): ")
