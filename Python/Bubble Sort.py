def bubblesort(array):
    length = len(array)   # will contribute to less time complexity
    for i in range(length):
        for j in range(length - 1):
            nextIndex = j + 1
            if array[j] > array[nextIndex]:
                smallernum = array[nextIndex]
                array[nextIndex] = array[j]
                array[j] = smallernum
    return array

# a test case
print(bubblesort([9, 8, 7, 4, 5, 6, 12, 10, 3]))
