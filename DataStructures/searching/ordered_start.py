# searching for an item in an ordered list
# this technique uses a binary search

items = [6, 8, 19, 20, 23, 42, 53, 87]

def binary_search(item, dataset):
    # start at the two ends of the list
    lower = 0
    upper = len(dataset) - 1

    while lower <= upper:
        # TODO: calculate the middle point
        mid = (lower + upper) // 2

        # TODO: id item is found return the index
        if dataset[mid] == item:
            return mid

        # TODO: otherwise get the next midpoint
        if dataset[mid] < item:
            lower = mid + 1
        else:
            upper = mid - 1

    if lower > upper:
        return None

l=4
r=7
print(binary_search(42, items))
print(binary_search(18, items))
print(binary_search(6, items))
print(l + (7-4) / 2)
