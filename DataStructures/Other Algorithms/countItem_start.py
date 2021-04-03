# using a hashtable to count individual items

# define a set of items that we want to count

fruits = ["apple", "grape", "orange", "mango", "apple",
          "orange", "mango", "pear", "banana", "grape",
          "mango", "date", "banana", "pear", "orange"]

# TODO: create a hashtable object to hold the items and count
basket = dict()

# TODO: iterate over each item and increament the count for each one
for fruit in fruits:
    if fruit in basket.keys():
        basket[fruit] += 1
    else:
        basket[fruit] = 1

# print the results
print(basket)