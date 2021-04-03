# searching for an item in an unordered list
# sometimes called a linear search

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_item(item, dataset):
    for i in range(len(dataset)):
        if dataset[i] == item:
            return i

    return None


print(find_item(19, items))
print(find_item(90, items))
