class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"{type(self).__name__}({self._items!r})"


class SortedList(SimpleList):
    def __init__(self, items=()):  # items is optional argument
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()


class IntList(SimpleList):
    def __init__(self, items):
        for e in items: self._validate(e)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values')

    def add(self, element):
        self._validate(element)  # super() does not just let us access the base classes, rather it let us access
        super().add(element)  # the complete Method Resolution Order for a class


class SortedIntList(IntList, SortedList):
    """
    This class inherits from two base classes, IntList and SortedList.This is an example
    of multiple inheritance in Python. The order of declaring the base classes inside parenthesis
    is important. Based on this order Python generates the Method Resolution Order aka inheritance graph.
    MRO is dependent on base class declaration order. MRO is calculated by Python using the C3 algorithm.

    C3 algorithm: C3 preserves base-class declaration order. It puts subclasses before base classes.
    In case of inconsistent base class ordering Python will raise a TypeError when the class definition is
    reached.
    """
    pass


if __name__ == '__main__':
    """SortedIntList maintains the constraint set in IntList as well as SortedList.
    When call to add() method on SortedIntList object, it resolves to a call to IntList.add() which itself
    calls super(). The super() call in IntList.add() uses the full MRO for a SortedList. i.e. rather than
    resolving to SimpleList.add() it actually resolves to SortedList.add().
    IntList.__mro__ -> gives types in inheritance graph as tuples
    SortedIntList.__bases__ -> shows tuples of types on SortedIntList
    
    super(): Given a Method Resolution Order and a class C in that MRO, super() gives an object which
    resolves methods using only the part of the MRO which comes after C. super() works with the MRO
    of an object not just its base classes.
    super(class-object, instance-or-class) 
    first argument in super() is the class that will be used to trim the MRO
    and second argument provides the MRO.
    Hence we can change the behaviour a class which extends multiple base classes by explicitly
    passing the arguments to super().
    
    Duck typing: The specific type name of an object does not determine if it can be used
    in a given context rather Python uses Duck typing where an object's fitness for use is only determined
    at the time its actually used, and exceptions are raised when an object does not have the necessary
    attributes to fulfill the request.
    
    In Python inheritance is best used as a way to share implementation, i.e inheritance in Python is a
    convenient way to reuse code, much more than it is a way to construct type hierarchies.    
    """
    s = SortedIntList([4, 21, 1])
    s.add(-189)
    print(s)  # Will print the sorted int list
    s.add('num')  # Will raise TypeError



