from math import pow

def decimal(binary):
    """Function to convert binary number to decimal number
    args:
         binary: binary string to be converted to decimal number
    """
    num = 0
    for i in range(0, len(binary)):
        num = num + (int(binary[i]) * pow(2, len(binary) - 1 - i))

    return num


if __name__ == '__main__':
    print(decimal('11001'))

