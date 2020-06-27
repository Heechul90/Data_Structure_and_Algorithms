import random

N = 10
IstNumbers = range(N)
random.shuffle(IstNumbers)

print(IstNumbers)

def performSelectionSort(IstNumbers):
    for itr1 in range(0, N):
        for itr2 in range(itr1 + 1, N):
            if IstNumbers[itr1] < IstNumbers[itr2]:
                IstNumbers[itr1], IstNumbers[itr2] = \
                IstNumbers[itr2], IstNumbers[itr1]
        return IstNumbers

print(performSelectionSort(IstNumbers))