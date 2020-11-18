def bubble_sort(p):
    n = len(p)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


array = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]
bubble_sort(array)
print(array)