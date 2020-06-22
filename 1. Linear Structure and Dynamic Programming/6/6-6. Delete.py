



def delete(self, value, node = ''):
    if node == '':
        node = self.root
    if node.getValue() < value:
        return self.delete(value, node.getRHS())
    if node.getValue() > value:
        return self.delete(value, node.getLHS())
    if node.getValue() == value:
        if node.getLHS() != '' and node.getRHS() != '':
            nodeMin = self.findMin(node.getRHS())
            node.setValue(nodeMin.getValue())
            self.delete(nodeMin.getValue(), node.getRHS())
            return
        parent = node.getParent()
        if node.getLHS() != '':
            if node == self.root:
                self.root = node.getLHS()
            elif parent.getLHS() == node:
                parent.getLHS(node.getLHS())
                node.getLHS().setParent(parent)
            else:
                parent.setRHS(node.getLHS())
                node.getLHS().setParent(parent)
            return
        if node.getRHS() != '':
            if node == self.root:
                self.root = node.getRHS()
            elif parent.getLHS() ==node:
                parent.setLHS(node.getRHS())
                node.getRHS().setParent(parent)
            else:
                parent.setRHS(node.getRHS())
                node.getRHS().setParent(parent)
            return
        if node == self.root:
            self.root = ''
        elif parent.getLHS() == node:
            parent.setLHS('')
        else:
            parent.setLHS('')
        return