class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

s = Stack()

while True:
    print('Option 1: Push')
    print('Option 2: Pop')
    print('Option 3: Quit')

    do = int(input('What would you like to do? Enter a relevant Option.'))

    if do == 1:
        item = int(input('Enter the value to be pushed: '))
        s.push(item)
    elif do == 2:
        if s.is_empty():
            print("Stack is empty!")
        else:
            print('Popped value: ',s.pop())
    elif do == 3:
        print('Exiting ...')
        break
    else:
        print('Please enter a valid Option')