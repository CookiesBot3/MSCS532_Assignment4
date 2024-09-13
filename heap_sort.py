def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child
    right = 2 * i + 2  # right child

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def build_max_heap(arr):
    n = len(arr)
    # Build a max heap starting from the last non-leaf node and heapifying upward
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# def extract_max(arr):
#     n = len(arr)
#     if n == 0:
#         return None  # If the heap is empty, there's no max to extract
#
#     # Swap the root (maximum element) with the last element
#     arr[0], arr[n - 1] = arr[n - 1], arr[0]
#     max_element = arr.pop()  # Remove the last element (the maximum one)
#     heapify(arr, len(arr), 0)  # Re-heapify to restore the heap property
#     return max_element

def heapsort(arr):
    n = len(arr)
    build_max_heap(arr)  # Build the initial max-heap

    # One by one extract the maximum element from the heap and reduce the heap size
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap the root (max) with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

    return arr

# arr = [12, 11, 13, 5, 6, 7]
# print("Original array:", arr)
#
# build_max_heap(arr)
# print("Max-heap:", arr)
#
# heapsort(arr)
# print("Sorted array using heapsort:", arr)
