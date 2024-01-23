import time
import random

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    # Generate a sorted list for testing
    test_list = sorted(random.sample(range(1, 1000), 100))

    # Measure the time taken for binary search
    start_time = time.time()
    result = binary_search([1,2,3,4,5,6,7,8,9,10], 42)
    end_time = time.time()

    print(f"Binary search: {result}. Time taken: {end_time - start_time:.6f} seconds")
