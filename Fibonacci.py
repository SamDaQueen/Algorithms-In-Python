def get_fib(position):
    if position==0:
        return 0
    if position==1:
        return 1
    else:
        first = 0
        second = 1
        next = first + second
        return get_fib(position-1)

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)
