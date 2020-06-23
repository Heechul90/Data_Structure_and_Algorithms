

def perform_selection_sort(list_numbers):
    for itr1 in range(0, len(list_numbers)):
        for itr2 in range(itr1+1,len(list_numbers)):
            if list_numbers[itr1] > list_numbers[itr2]:
                list_numbers[itr1], list_numbers[itr2] = list_numbers[itr2], list_numbers[itr1]
    return list_numbers


def main():

    
    list_numbers = [2,5,8,9,4,8,1,4,5,3,2]
    print(list_numbers)
    print(perform_selection_sort(list_numbers))


if __name__ == "__main__":
    main()