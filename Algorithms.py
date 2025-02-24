# Algorithms.py

# Linear Search
# Takes an array and a target element
# Returns the index of the target element or -1 if the target is not found
# O(n) time complexity
# O(1) space complexity
def LinearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target found
    return -1  # Target not found

# Bubble Sort
# Takes an array
# Returns an array sorted with Bubble Sort
# O(n^2) time complexity
# O(1) space complexity
def BubbleSort(arr):
    n = len(arr)
    # Loop over the array
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Yield the array and highlight the swapped indices
                yield arr.copy(), (j, j+1)
    # Final state (no swap highlighted)
    yield arr.copy(), None

# Merge Sort
# Takes an array
# Returns an array sorted with Merge Sort (in-place)
# O(n log n) time complexity
# O(n) space complexity
def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        MergeSort(leftHalf)
        MergeSort(rightHalf)

        i = j = k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1

    return arr

# Quick Sort
# Takes an array
# Returns an array sorted with Quick Sort
# O(n log n) average time complexity, O(n^2) worst case
# O(log n) space complexity (due to recursion)
def QuickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return QuickSort(left) + middle + QuickSort(right)

# Counting Sort (Helper for Radix Sort)
def CountingSort(arr, exp):
    numOfElem = len(arr)
    output = [0] * numOfElem
    count = [0] * 10

    # 1. Count occurrences of each digit in the current place
    for i in range(numOfElem):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # 2. Convert counts to cumulative counts
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 3. Build the output array (right to left for stability)
    for i in range(numOfElem - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # 4. Copy sorted output back to the original array
    for i in range(numOfElem):
        arr[i] = output[i]

# Radix Sort
# Takes an array of non-negative integers
# Returns the array sorted with Radix Sort
# O(nk) time complexity where k is the number of digits 
# O(n) space complexity
def RadixSort(arr):
    if not arr: return arr  # Edge case if the list is empty

    # Least significant digit approach (LSD)
    # Find the maximum number to determine the number of digits 
    maxNum = max(arr)
    exp = 1

    # Continue sorting for each digit place value
    while maxNum // exp > 0:
        CountingSort(arr, exp)
        exp *= 10
    return arr



