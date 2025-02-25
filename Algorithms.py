# Algorithms.py

# Linear Search Generator
# Yields the array state at each iteration, highlighting the index being checked.
def LinearSearch(arr, target):
    for i in range(len(arr)):
        # Yield the current state, highlighting index i.
        yield arr.copy(), (i,)
        if arr[i] == target:
            # Optionally yield a final state showing the found index.
            yield arr.copy(), (i,)
            return
    yield arr.copy(), None


# Bubble Sort Generator (already done)
def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Yield a copy of the array and highlight the swapped indices.
                yield arr.copy(), (j, j+1)
    yield arr.copy(), None


# Merge Sort Generator
# This version uses a helper merge() function that yields after each merge operation.
def MergeSort(arr, left=0, right=None):
    if right is None:
        right = len(arr)
    if right - left > 1:
        mid = (left + right) // 2
        yield from MergeSort(arr, left, mid)
        yield from MergeSort(arr, mid, right)
        yield from merge(arr, left, mid, right)
    yield arr.copy(), None

def merge(arr, left, mid, right):
    left_part = arr[left:mid]
    right_part = arr[mid:right]
    i = j = 0
    k = left
    # Merge the two halves back into arr.
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        yield arr.copy(), (k,)
        k += 1
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        yield arr.copy(), (k,)
        k += 1
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        yield arr.copy(), (k,)
        k += 1


# Quick Sort Generator (in-place)
def QuickSort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot = arr[high]
        i = low
        # Partitioning: move elements smaller than pivot to the left.
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                yield arr.copy(), (i, j)
                i += 1
            yield arr.copy(), None
        # Place the pivot in its correct position.
        arr[i], arr[high] = arr[high], arr[i]
        yield arr.copy(), (i, high)
        # Recursively sort the left and right partitions.
        yield from QuickSort(arr, low, i - 1)
        yield from QuickSort(arr, i + 1, high)
    yield arr.copy(), None


# Counting Sort Generator (Helper for Radix Sort)
def CountingSort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # 1. Count occurrences of each digit at the current exponent.
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # 2. Convert count to cumulative count.
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 3. Build the output array (iterate from right for stability).
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # 4. Copy output back to arr, yielding after each assignment.
    for i in range(n):
        arr[i] = output[i]
        yield arr.copy(), (i,)

# Radix Sort Generator
def RadixSort(arr):
    if not arr:
        yield arr.copy(), None
        return
    maxNum = max(arr)
    exp = 1
    while maxNum // exp > 0:
        yield from CountingSort(arr, exp)
        exp *= 10
    yield arr.copy(), None