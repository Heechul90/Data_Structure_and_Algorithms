### findMin


def findMin(self, node = ''):
    if node == '':
        node = self.root
    if node.getLHS() == '':
        return node
    return self.findMin(node.getLHS())