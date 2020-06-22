### findMax


def findMax(self, node = ''):
    if node == '':
        node = self.root
    if node.getRHS() == '':
        return node
    return self.findMax(node.getRHS())