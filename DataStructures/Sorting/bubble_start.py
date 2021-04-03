# Bubble sort algorithm

def bubblesort(dataset):
    # TODO: start with the array length and decrement each time
    for i in range(0, len(dataset), 1):
        for j in range(len(dataset)-i-1):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j+1]
                dataset[j+1] = dataset[j]
                dataset[j] = temp
        print('Current state:', dataset)

def main():
    list1=[20,6,28,8,23,41,19]
    bubblesort(list1)
    print('result:',list1)


if __name__ == '__main__':
    main()