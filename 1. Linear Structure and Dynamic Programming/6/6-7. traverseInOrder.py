### traverseInlOrder


def traverseInlOrder(self, node = ''):
    if node == '':
        node =self.root
    ret = []
    if node.getLHS() != '':
        ret = ret + self.traverseInlOrder(node.getLHS())
    ret.append(node.getValue())
    if node.getRHS() != '':
        ret = ret + self.traverseInlOrder(node.getRHS())
    return ret