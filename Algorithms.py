# algorithms.py

def LinearSearch(arr, target):
    for i in range(len(arr)):
        yield arr.copy(), (i,)
        if arr[i] == target:
            yield arr.copy(), (i,)
            return
    yield arr.copy(), None


def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr.copy(), (j, j+1)
    yield arr.copy(), None


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


def QuickSort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                yield arr.copy(), (i, j)
                i += 1
            yield arr.copy(), None
        arr[i], arr[high] = arr[high], arr[i]
        yield arr.copy(), (i, high)
        yield from QuickSort(arr, low, i - 1)
        yield from QuickSort(arr, i + 1, high)
    yield arr.copy(), None


def CountingSort(arr, exp):
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
        yield arr.copy(), (i,)

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
