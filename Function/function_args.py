# In the event that you pass arguments like whole numbers, strings or tuples to a function, the passing is like
# CALL BY VALUE because you can not change the value of the immutable objects being passed to the function.
# Whereas passing mutable objects can be considered as CALL BY REFERENCE because when their values are changed
# inside the function, then it will also be reflected outside the function

def main():
    #x = [2, 4, 7]
    x=6
    y = x
    #y[1] = 15
    y = 11
    #kitten(y)
    #print(f'in main: x is {x}')
    print(f'value of x {x}')
    print(f'value of y {y}')
    print('value of location of x ', id(x))
    print('value of location of y ', id(y))


def kitten(n):
    n[0] = 10
    print(n, 'Meow.')
    print('value of location of n ', id(n))


if __name__ == '__main__':
    main()
