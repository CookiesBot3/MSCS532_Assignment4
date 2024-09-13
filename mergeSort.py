# The merge sort function is implemented here
def mergeSort(arr):
    # If there is only one or less the array is sorted.
    if len(arr) <= 1:
        return arr

    # Getting the midpoint, left side and right side of the array
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort the first and second halves.
    left = mergeSort(left)
    right = mergeSort(right)
    # Merge the two sides back
    return merge(left, right)

def merge(left, right):
    # Creating temp spaces as this is not in position sort
    result = []
    i, j = 0, 0

    # Looping through both the left and right side to merge in ascending order.
    # N is just there to track the amount of operations.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Merging is done. These two lines Merges the left and right side
    # of the array into one result array if there are any remaining.
    result.extend(left[i:])
    result.extend(right[j:])

    return result