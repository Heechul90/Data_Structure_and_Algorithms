### Search


def search(self, value, node = ''):
    if node == '':
        node = self.root
    if value == node.getValue():
        return True
    if value > node.getValue():
        if node.getRHS() == '':
            return False
        else:
            return self.search(value, node.getRHS())
    if value < node.getValue():
        if node.getLHS() == '':
            return False
        else:
            return self.serach(value, node.getLHS())