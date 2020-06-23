### traversePostlOrder


def traversePostlOrder(self, node = ''):
    if node == '':
        node = self.root
    ret = []
    if node.getLHS() != '':
        ret = ret + self.traversePostlOrder(node.getLHS())
    if node.getRHS() != '':
        ret = ret + self.traversePostlOrder(node.getRHS())
    ret.append(node.getValue())
    return ret