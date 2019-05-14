def bubble_sort(array):
    switched = True
    for i in range(len(array)):
        if not switched: break
        switched = False
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                switched = True
                array[j],array[j+1]=array[j+1],array[j]
                print (array)

test_list = [5,6,76,-1,12,98,-3]
bubble_sort(test_list)
print('Sorted array:' ,test_list)
