# Main.py

# Standard Library Imports
import sys
import random

# Local Imports
from Algorithms import (
    LinearSearch,
    BubbleSort,
    MergeSort,
    QuickSort,
    RadixSort
)


def RunTests():
    randIntLowBound = 0
    randIntHighBound = 1000
    numOfElems = 25

    # 1. Linear Search Test
    arrSearch = [random.randint(randIntLowBound, randIntHighBound) for _ in range(numOfElems)]
    targetInArr = random.choice(arrSearch)
    targetNotInArr = 10000

    print("=== Linear Search Test ===")
    print(f"Array: {arrSearch}")
    print(f"Searching for: {targetInArr} (in array) and {targetNotInArr} (not in array)")
    print(f"{targetInArr} found at position {LinearSearch(arrSearch, targetInArr)}")
    print(f"{targetNotInArr} found at position {LinearSearch(arrSearch, targetNotInArr)}\n")

    # 2. Bubble Sort Test
    arrBubble = [random.randint(randIntLowBound, randIntHighBound) for _ in range(numOfElems)]
    print("=== Bubble Sort Test ===")
    print("Before:", arrBubble)
    BubbleSort(arrBubble)  # Sort in-place, returns arrBubble too
    print("After: ", arrBubble, "\n")

    # 3. Merge Sort Test
    arrMerge = [random.randint(randIntLowBound, randIntHighBound) for _ in range(numOfElems)]
    print("=== Merge Sort Test ===")
    print("Before:", arrMerge)
    MergeSort(arrMerge)  # Sort in-place, returns arrMerge
    print("After: ", arrMerge, "\n")

    # 4. Quick Sort Test
    arrQuick = [random.randint(randIntLowBound, randIntHighBound) for _ in range(numOfElems)]
    print("=== Quick Sort Test ===")
    print("Before:", arrQuick)
    sortedQuick = QuickSort(arrQuick)  # QuickSort returns a new sorted list
    print("After: ", sortedQuick, "\n")

    # 5. Radix Sort Test
    arrRadix = [random.randint(randIntLowBound, randIntHighBound) for _ in range(numOfElems)]
    print("=== Radix Sort Test ===")
    print("Before:", arrRadix)
    sortedRadix = RadixSort(arrRadix)  # RadixSort returns the sorted list
    print("After: ", sortedRadix, "\n")


if __name__ == "__main__":
    if "--no-gui" in sys.argv:
        RunTests()
    else:
        from GUI import RunGUI
        RunGUI()
