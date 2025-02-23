# Algorithms.py

# Linear Search
# Takes an array and a target element
# Returns the index of the target element or -1 if the target is not found
def LinearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 # Target not found


