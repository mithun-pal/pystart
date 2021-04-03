# Implement a quicksort

items = [20, 5, 8, 26, 10, 41, 87]

def quicksort(dataset, first, last):
    if first < last:
        # calculate the pivot index
        pivot_indx = partition(dataset, first, last)

        # now sort the two partitions
        quicksort(dataset, first, pivot_indx-1)
        quicksort(dataset, pivot_indx+1, last)


def partition(datavalues, first, last):
    # choose the first item as the pivot value
    pivot_val = datavalues[first]

    lower = first + 1
    upper = last

    #
    done = False
    while not done:
        #TODO: advance the lower index
        while datavalues[lower] <= pivot_val and lower <= upper:
            lower += 1

        # TODO: lower the upper index
        while datavalues[upper] >= pivot_val and upper >= lower:
            upper -= 1

        # TODO: if the two indexes crosses we have found the split point
        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    # when the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return the split point index
    return upper

quicksort(items, 0, len(items) - 1)
print(items)