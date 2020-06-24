### Implementation of binary heap using array


class BinaryHeap:
    
    arrPriority = {}
    arrValue = {}
    size = 0

    def __init__(self):
        self.arrPriority = {}
        self.arrValue = {}
        self.size = 0
    
    def enqueueWithPriority(self, value, priority):
        self.arrPriority[self.size] = priority
        self.arrValue[self.size] = value
        self.percorlateUp(self.size-1)
    
    def percorlateUp(self, idxPercolate):
        if idxPercolate == 0:
            return
        parent = int((idxPercolate-1) / 2)
        if self.arrPriority[parent] < self.arrPriority[idxPercolate]:
            self.arrPriority[parent], self.arrPriority[idxPercolate] = self.arrPriority[idxPercolate], self.arrPriority[parent]
            self.arrValue[parent], self.arrValue[idxPercolate] = self.arrValue[idxPercolate], self.arrValue[parent]
            self.percorlateUp(parent)
        
    def dequeueWithPriority(self):
        if self.size == 0:
            return ''
        retPriority = self.arrPriority[0]
        retValue = self.arrValue[0]
        self.arrPriority[0] = self.arrPriority[self.size -1]
        self.arrValue[0] = self.arrValue[self.size -1]
        self.size = self.size - 1
        self.percorlateDown(0)
        return retValue
    
    def percolateDown(self, idxPercolate):
        if 2*idxPercolate + 1 >= self.size:
            return
        
        else:
            leftChild = 2 * idxPercolate + 1
            LeftPriority = self.arrPriority[leftChild]
        if 2*idxPercolate + 2 >= self.size:
            rightPriority = -9999
        else:
            rightChild = 2 * idxPercolate + 2
            rightPriority = self.arrPriority[rightChild]
        if leftPriority > rightPriority:
            biggerChild = leftChild
        else:
            biggerChild = rightChild
        if self.arrPriority[idxPercolate] < self.arrPriority[biggerChild]:
            self.arrPriority[idxPercolate], self.arrPriority[biggerChild] = self.arrPriority[biggerChild], self.arrPriority[idxPercolate]
            self.arrValue[idxPercolate], self.arrValue[biggerChild] = self.arrValue[biggerChild], self.arrValue[idxPercolate]
            self.percolateDown(biggerChild)

    def build(self, arrInputPriority, arrInputValue):
        for itr in range(len(arrInputPriority)):
            self.arrPriority[itr] = arrInputPriority[itr]
            self.arrValue[itr] = arrInputPriority[itr]
        self.size = len(arrInputPriority)
        for itr in range(self.size-1, -1, -1):
            self.percolateDown(itr)

pq = BinaryHeap()
pq.enqueueWithPriority('A', 1)
pq.enqueueWithPriority('B', 2)
pq.enqueueWithPriority('C', 3)
pq.enqueueWithPriority('D', 99)

print(pq.dequeueWithPriority())
print(pq.dequeueWithPriority())
print(pq.dequeueWithPriority())
print(pq.dequeueWithPriority())


