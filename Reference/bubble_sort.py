def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Flag to optimize the algorithm
        swapped = False

        # range 代表最后面的"墙"
        # 每次bubble上浮的过程,都会把最大的数放在后边
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping occurred, array is already sorted
        if not swapped:
            break


# Test the function
if __name__ == "__main__":
    # Example array
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original array:", arr)

    bubble_sort(arr)

    print("Sorted array:", arr)
