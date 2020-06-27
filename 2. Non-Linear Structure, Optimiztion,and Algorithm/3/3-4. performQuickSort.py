import random

N = 10
IstNumbers = range(N)
random.shuffle(IstNumbers)

print(IstNumbers)

def performQuickSort(seq, pivot = 0):
    if len(seq) <= 1:
        return seq
    pivotValue = seq[pivot]
    less = []
    greater = []
    for itr in range(len(seq)):
        if itr == pivot:
            continue
        elif seq[itr] > pivotValue:
            greater.append(seq[itr])
        elif seq[itr] <= pivotValue:
            less.append(seq[itr])
    return performQuickSort(less) + [pivotValue] + performQuickSort(greater)

print(performQuickSort(IstNumbers))