from array import array

arr = array('i',[1,2,3,4,5])

while True:
    print('Option 1: Print the Array')
    print('Option 2: Add Elements')
    print('Option 3: Delete Elements')
    print('Option 4: Exit')

    opt = int(input('Enter your choice: '))
    if opt == 1:
        print('Array elements are: ', end='')
        print('[', end='')
        for i in range(0, len(arr)):
            if i != len(arr) - 1:
                print(arr[i], end=',')
            else:
                print(arr[i], end=']')
        print()
    elif opt == 2:
        try:
            num = int(input('Enter the number to be added: '))
            if isinstance(num, int):
                arr.append(num)
        except ValueError as error:
            print('Your should provide an Integer number to be added, try again...')
            print(error)
        #print('your input is: ', num)
    elif opt == 3:
        popped = arr.pop()
        print('The value {} is deleted'.format(popped))
    elif opt == 4:
        break
    else:
        print('Please enter a valid choice')


