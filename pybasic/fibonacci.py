
def fibo1(n):
        series_length = int(input("Enter the no of items to be generated: "))
        first = 0
        second = 1
        print(first, second, end=" ")
        for i in range(0, series_length - 2):
            third = first + second
            first = second
            second = third
            print(second, end=" ")

#Function for nth Fibonacci number

def fibo2(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b

        # Driver Program

print(fibo2(8))
