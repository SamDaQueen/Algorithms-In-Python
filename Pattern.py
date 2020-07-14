def number(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1, end=' ')
        print('')


def number2(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=' ')
        print('')


def number3(n):
    for i in range(n):
        for j in range(i+1, 0, -1):
            print(j, end=' ')
        print('')


def number4(n):
    s = 2
    c = 1
    for i in range(n):
        for j in range(1, s):
            print(c, end=' ')
            c += 1
        print('')
        s += 2


def number5(n):
    for i in range(n):
        j = 2**i
        while j > 1:
            print(j, end=' ')
            j //= 2
        print('1')
    for i in range(n):
        for j in range(i, -1, -1):
            print(2**j, end=' ')
        print(' ')


def number6(n):
    for i in range(n):
        print(2**i, end=' ')
        for j in range(i):
            print(2**(i+1), end=' ')
        print('')


def halfPyramid(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end=' ')
        print('')


def invertedHalfPyramid(n):

    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end=' ')
        print('')


def sideTriangle(n):
    for i in range(n//2):
        for j in range(i+1):
            print('*', end=' ')
        print('')
    for i in range(n-n//2, 0, -1):
        for j in range(i):
            print('*', end=' ')
        print('')


def pyramid(n):
    spaces = n-1
    for i in range(1, n+1):
        for j in range(spaces):
            print(' ', end=' ')
        for j in range(i*2-1):
            print('*', end=' ')
        print('')
        spaces -= 1


def leftFacingTriangle(n):
    spaces = n-1
    for i in range(1, n+1):
        for j in range(spaces):
            print(' ', end=' ')
        for j in range(i):
            print('*', end=' ')
        print('')
        spaces -= 1


def nPyramid(n):
    spaces = n-1
    for i in range(1, n+1):
        for j in range(spaces):
            print(' ', end='')
        for j in range(i):
            print('*', end=' ')
        print('')
        spaces -= 1


def alphabet(n):
    asc = ord('A')
    for i in range(n):
        for j in range(i+1):
            print(chr(asc), end=' ')
            asc += 1
        print('')


def main():
    while True:
        try:
            n = int(input("Enter number: "))
            break
        except ValueError:
            print("Enter an integer!\n")
            continue
    number(n)
    print()
    number2(n)
    print()
    number3(n)
    print()
    number4(n)
    print()
    number5(n)
    print()
    halfPyramid(n)
    print()
    invertedHalfPyramid(n)
    print()
    sideTriangle(n)
    print()
    pyramid(n)
    print()
    leftFacingTriangle(n)
    print()
    nPyramid(n)
    print()
    alphabet(n)


if __name__ == "__main__":
    main()
