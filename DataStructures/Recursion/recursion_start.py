# Implement power and factorial function using recursion

# 2^4 = 2*2*2*2

def power(num, pw):
    if pw == 0:
        return 1
    else:
        return num * power(num, pw - 1)



# 5! = 5*4*3*2*1
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def countup(x):
    if x == 128:
        return
    else:
        countup(x + 1)


print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))
print(countup(5))
