### traverseLevelOrder


def traverseLevelOrder(self):
    ret = []
    Q = Queue()
    Q.enqueue(self.root)
    while Q.isEmpth() == False:
        node = Q.dequeue()
        if node == '':
            continue
        ret.append(node.getValue())
        if node.getLHS() != '':
            Q.enqueue(node.getLHS())
        if node.getRHS() != '':
            Q.enqueue(node.getRHS())
    return ret