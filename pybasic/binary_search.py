import DataStructures.Sorting.mergesort_start as merge

def binary_search(element, dataset, lower, upper):
    if upper >= lower:
        mid = (lower + upper) // 2

        if dataset[mid] == element:
            return mid

        elif dataset[mid] > element:
            return binary_search(element, dataset, lower, mid - 1)
        else:
            return binary_search(element, dataset, mid + 1, upper)

    else:
        return -1

def search(elem, elements):
    return binary_search(elem, elements, 0, len(elements)-1)

if __name__ == '__main__':
    datavalues = [1, 3, 20, 71, 4,1, 20, 3, 12, 18]
    ranked = [100, 90, 90, 80, 75, 60]
    merge.mergesort(datavalues)
    ranked.reverse()

    print(search(100, ranked))
    #if search(100, datavalues):
     #   print('Found ..')
    #else:
     #   print('Not Found ..')
