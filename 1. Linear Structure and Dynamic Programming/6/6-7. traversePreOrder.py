### traversePreOrder


def traversePreOrder(self, node = ''):
    if node == '':
        node = self.root
    ret = []
    ret.append(node.getValue())
    if node.getLHS() != '':
        ret = ret + self.traversePreOrder(node.getLHS())
    if node.getRHS() != '':
        ret = ret + self.traversePreOrder(node.getRHS())
    return ret