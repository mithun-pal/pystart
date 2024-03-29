# Implement a merge sort with recursion

items = [20, 6, 8, 53, 23, 87, 42, 19]

def mergesort(dataset):
    #print("I am called..")
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        #TODO: recursively break down the array
        mergesort(leftarr)
        mergesort(rightarr)

        # TODO: now perform the merging
        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # TODO: while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1
        # TODO: if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1
        # TODO: if the right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1

    #return dataset


# test the merge sort with data
if __name__ == '__main__':
    mergesort(items)
    print(items)
    #print(7 / 2)