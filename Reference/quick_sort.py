def partition(arr, low, high):
    """
    Partitions the array and returns the index of the pivot.
    """
    # Choose the rightmost element as pivot
    pivot = arr[high]
    # Index of smaller element
    i = low - 1

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def iterative_quick_sort(arr):
    """
    Sorts an array using iterative quick sort algorithm.
    """
    # Create a stack for storing start and end indices
    stack = []

    # Push initial values of low and high to stack
    stack.append((0, len(arr) - 1))

    # Keep popping from stack while it is not empty
    while stack:
        # Pop low and high
        low, high = stack.pop()

        # Set pivot element at its correct position
        pivot_index = partition(arr, low, high)

        # If there are elements on left side of pivot,
        # push left side to stack
        if pivot_index - 1 > low:
            stack.append((low, pivot_index - 1))

        # If there are elements on right side of pivot,
        # push right side to stack
        if pivot_index + 1 < high:
            stack.append((pivot_index + 1, high))


# Test the iterative_quick_sort function
if __name__ == "__main__":
    # Test case 1: Random integers
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr1)
    iterative_quick_sort(arr1)
    print("Sorted array:", arr1)

    # Test case 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5]
    print("\nOriginal array:", arr2)
    iterative_quick_sort(arr2)
    print("Sorted array:", arr2)

    # Test case 3: Reverse sorted array
    arr3 = [5, 4, 3, 2, 1]
    print("\nOriginal array:", arr3)
    iterative_quick_sort(arr3)
    print("Sorted array:", arr3)

    # Test case 4: Array with duplicate elements
    arr4 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("\nOriginal array:", arr4)
    iterative_quick_sort(arr4)
    print("Sorted array:", arr4)
