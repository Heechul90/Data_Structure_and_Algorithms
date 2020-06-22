### Insert


def insert(self, value, node = ''):
    if node == '':
        node = self.root
    if self.root == '':
        self.root = TreeNode(value, '')
        return
    if value == node.getValue():
        return
    if value > node.getValue():
        if node.getRHS() == '':
            node.setRHS(TreeNode(value, node))
        else:
            sefl.insert(value, node.getRHS())
    if value < node.getValue():
        if node.getLHS() == '':
            node.setLHS(TreeNode(value, node))
        else:
            self.insert(value, node.getLHS())
    return