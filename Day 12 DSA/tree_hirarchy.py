class TreeNode:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None
    def addChild(self,child):
        child.parent = self
        self.children.append(child)
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.name + " (" + self.designation + ")")
        if self.children:
            for child in self.children:
            # print(child.data)
                child.print_tree()
        
def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Vishwa","Infrastructure Head")
    infra_head.addChild(TreeNode("Dhaval","Cloud Manager"))
    infra_head.addChild(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.addChild(infra_head)
    cto.addChild(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels","HR Head")

    hr_head.addChild(TreeNode("Peter","Recruitment Manager"))
    hr_head.addChild(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.addChild(cto)
    ceo.addChild(hr_head)

    return ceo





if __name__ == '__main__':
    root = build_management_tree()
    root.print_tree()
    # root.get_level()




