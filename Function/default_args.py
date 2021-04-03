# Any default argument should be preceded by non-default arguments i.e
# Default argument should be after non-default arguments

def main():
    kitten(4)


def kitten(a, b=1, c=29):
    print('Meow.')
    print(a, b, c)


if __name__ == '__main__':
    main()