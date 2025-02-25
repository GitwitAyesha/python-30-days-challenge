class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self,child):
        child.parent = self
        self.children.append(child)
    def get_level(self):
        # function is telling the children level and code will be able to count parents for a particular child
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
            # print(child.data)
                child.print_tree()
def build_product_tree():
    # root node (means parent node)
    root = TreeNode("Electronics")
    # laptop subtree
    laptop = TreeNode("Laptop")
    laptop.addChild(TreeNode("Mac"))
    laptop.addChild(TreeNode("Surface"))
    laptop.addChild(TreeNode("Thinkpad"))
    
    cellphone = TreeNode("Cell phone")
    cellphone.addChild(TreeNode("iphone"))
    cellphone.addChild(TreeNode("google pixel"))
    cellphone.addChild(TreeNode("samsung"))

    tv = TreeNode("TV")
    tv.addChild(TreeNode("Samsung"))
    tv.addChild(TreeNode("changhong Ruba"))
    tv.addChild(TreeNode("LG"))

    root.addChild(laptop)
    root.addChild(cellphone)
    root.addChild(tv)
    print(tv.get_level())
    return root

if __name__ == '__main__':
    root = build_product_tree()
    # print(root.get_level())
    root.print_tree()
    pass
    