"""Module for demonstrating generator execution"""


def take(count, iterable):
    """Take items from the front of an iterable.

    Args:
        count: The maximum number of items to retrieve.
        iterable: The source series.

    Yields: At most 'count' items from 'iterable'.
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [9, 14, 0, 4, 6]
    for item in take(3, items):
        print(item)

def distinct(iterable):
    """Return unique items by eliminating duplicates.
    Args:
        iterable: The source series.
    Yields:
        Unique elements in order from 'iterable'.
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    items = [5,6,6,2,9,5]
    for item in distinct(items):
        print(item)


def run_pipeline():
    items = [5, 1, 1, 2, 3, 5]
    for item in take(3,distinct(items)):
        print(item)

if __name__ == '__main__':
    run_pipeline()