# use a hashtable to filter out duplicate items

# define a set of items that we want to reduce duplicates

fruits = ["apple", "grape", "orange", "banana", "apple",
          "orange", "mango", "pear", "banana", "date",
          "mango", "date", "grape", "pear", "orange"]

# TODO: create a hashtable to perform a filter
basket = dict()

# TODO: loop over each item and add to the hashtable
for fruit in fruits:
    basket[fruit] = 0

# TODO: create a set from the resulting keys in the hashtable
result = set(basket.keys())
print(result)

