# noYieldAlgorithms.py

def LinearSearchNoYield(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def BubbleSortNoYield(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def MergeSortNoYield(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        MergeSortNoYield(left)
        MergeSortNoYield(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def QuickSortNoYield(arr):
    if len(arr) <= 1:
        return
    pivot = arr[len(arr)//2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    sorted_arr = left + mid + right
    arr[:] = sorted_arr
    QuickSortNoYield(left)
    QuickSortNoYield(right)

def RadixSortNoYield(arr):
    if not arr:
        return
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_no_yield(arr, exp)
        exp *= 10

def counting_sort_no_yield(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index]-1] = arr[i]
        count[index] -= 1
    for i in range(n):
        arr[i] = output[i]
