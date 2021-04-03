# searching for an item in an ordered list
# this technique uses a binary search

items = [6, 8, 19, 20, 23, 42, 53, 87]

def search_item(item, datavalues):
    return binary_search(item, datavalues, 0, len(datavalues) - 1)

def binary_search(element, dataset, lower, upper):
    # start at the two ends of the list

    if upper >= lower:
        # TODO: calculate the middle point
        mid = (lower + upper) // 2

        # TODO: id item is found return the index
        if dataset[mid] == element:
            return mid
        # TODO: otherwise get the next midpoint
        elif dataset[mid] < element:
            return binary_search(element, dataset, mid + 1, upper)
        else:
            return binary_search(element, dataset, lower, mid - 1)
    else:
        return None


print(search_item(42, items))
print(search_item(18, items))
print(search_item(6, items))
