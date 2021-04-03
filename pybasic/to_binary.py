def binary(num):
    """Function to convert to Binary number of a Decimal number

    args:
         num: number in Decimal format to be converted in Binary format

    """
    binary_str=""

    while num != 0:
        remainder = num % 2
        num = num // 2
        binary_str = str(remainder) + binary_str

    return binary_str

if __name__ == '__main__':
    #print("".join(reversed('hello')))
    #lang = 'python'
    #print(lang[len(lang)::-1])
    print(binary(25))
    print(1 % 2)
