import DataStructures.Sorting.mergesort_start as merge

def search(element, dataset, lower, upper):
    if upper >= lower:
        mid = (lower + upper) // 2

        if dataset[mid] == element:
            return True

        elif dataset[mid] > element:
            return search(element, dataset, lower, mid - 1)
        else:
            return search(element, dataset, mid + 1, upper)

    else:
        return False

if __name__ == '__main__':
    datavalues = [1, 3, 71, 4, 20, 12, 18]
    merge.mergesort(datavalues)
    #print(datavalues)

    if search(21, datavalues, 0, len(datavalues) - 1):
        print('Found ..')
    else:
        print('Not Found ..')
