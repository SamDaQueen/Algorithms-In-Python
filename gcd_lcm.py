def gcd(a, b):
    s = min(a, b)
    l = max(a, b)
    while(l % s > 0):
        s = l % s
    print("GCD: ", s)
    lcm(a, b, s)


def lcm(a, b, s):
    print("LCM: ", (a*b)/s)


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if a > 0 and b > 0:
        gcd(a, b)
    else:
        print("\nNumbers should be positive")


if __name__ == "__main__":
    main()
