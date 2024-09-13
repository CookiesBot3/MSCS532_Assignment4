def partition(arr, low, high):

    #Chose the pivot
    pivot = arr[high]
    i = low - 1

    # Traverse the arr low to high and
    # move all smaller elements to the left side,
    # each iteration the elements from low to i gets smaller
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Move the pivot point after smaller elements and return the position.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# The quickSort recursive function
def quickSort(arr, low = 0, high = None):
    #set the high index for the first round
    if high is None:
        high = len(arr) - 1

    if low < high:
        # The pivot index is partition and retrieve
        pivot_i = partition(arr, low, high)

        # Recursively calls for small elements for the left side
        # then the bigger elements for the right side.
        quickSort(arr, low, pivot_i-1)
        quickSort(arr, pivot_i+1, high)