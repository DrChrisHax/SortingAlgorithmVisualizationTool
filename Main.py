# Main.py

# Standard Library Imports
import random

# Third Party Imports

# Local Imports
from Algorithms import LinearSearch


def main():
    # Linear Search Test
    arr = [random.randint(1, 9999) for _ in range(10)]
    targetInArr = random.choice(arr)
    targetNotInArr = 10000

    print(f"Array: {arr}")
    print(f"Searching for: {targetInArr} and {targetNotInArr}")
    print(f"{targetInArr} found at position {LinearSearch(arr, targetInArr)}")
    print(f"{targetNotInArr} found at position {LinearSearch(arr, targetNotInArr)}")





# Needed so python calls the right main function
if __name__ == "__main__":
    main()