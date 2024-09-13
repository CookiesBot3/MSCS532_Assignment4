from mergeSort import mergeSort
from quickSort import quickSort
from heap_sort import heapsort
import time
import random

def generate_data(size, random_flag=False, ascending=False, descending=False):
    # Generates Random numbers in the array according to the size
    if random_flag:
        return random.sample(range(1, size + 1), size)
    # Generates ascending numbers in the array according to the size
    if ascending:
        temp = []
        for i in range(size):
            temp.append(i+1)
        return list(temp) # list() is used to decouple the array for a deepcopy
    # Generates descending numbers in the array according to the size
    if descending:
        temp = []
        for i in range(size, 0, -1):
            temp.append(i)
        return list(temp) # list() is used to decouple the array for a deepcopy
    # Generate a list of random array with repeated elements.
    else:
        array_with_repeats = [random.choice(range(1, size+1)) for _ in range(size)]
        return array_with_repeats

def sort_runner(arr, sort_flag = 0 ,arrayType = 0):
    sort_type = ""
    array_data_type = ""
    temp = []

    #flags to determine which data type it is sorting.
    if arrayType == 1:
        array_data_type = "random"
    elif arrayType == 2 :
        array_data_type = "ascending"
    elif arrayType == 3:
        array_data_type = "descending"
    else:
        array_data_type = "random with repeated elements"

    print(array_data_type + " before: ", arr)
    start_time = time.process_time() #start the timer
    if sort_flag == 1:
        quickSort(arr)
    elif sort_flag == 2:
        temp = mergeSort(arr)
    else:
        heapsort(arr)
    end_time = time.process_time()
    #Print out the proper result
    if sort_flag == 1:
        sort_type = "quick sort"
    elif sort_flag == 2:
        sort_type = "merge sort"
    else:
        sort_type = "Heap sort"

    print(sort_type + " time: ", end_time - start_time)
    if sort_flag == 2:
        print(array_data_type + " after sorted: ", temp)
    else:
        print(array_data_type + " after sorted: ", arr)
    print('')

def simulate_run(arr_size, sort_type):
    # Generate all the array dataset according to the flag ie. Random, ascending, descending
    array_random = generate_data(arr_size, random_flag=True)
    array_ascending = generate_data(arr_size, ascending=True)
    array_descending = generate_data(arr_size, descending=True)
    array_repeated = generate_data(arr_size)

    # Run the Sorter for each type of the array for merge and quick sort
    sort_runner(array_random, sort_type, arrayType=1)
    sort_runner(array_ascending, sort_type, arrayType=2)
    sort_runner(array_descending, sort_type, arrayType=3)
    sort_runner(array_repeated, sort_type)

if __name__ == '__main__':
    arr_size = 450 # Size of the array and values from 1 to size
    simulate_run(arr_size, 1)
    simulate_run(arr_size, 2)
    simulate_run(arr_size, 3)

