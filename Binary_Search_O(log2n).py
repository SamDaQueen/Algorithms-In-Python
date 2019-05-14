def binary_search(input_array, value):
    up = len(input_array)
    down = 0
    mid = up//2
    c=up
    while (value is not input_array[mid]) and (c>=0):
        if value<input_array[mid]:
            up=mid
            mid=mid-(up-down)//2
        else:
            down=mid
            mid=mid+(up-down)//2
        c=c-1
    if c<0:
        return -1
    else:
        return mid

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
