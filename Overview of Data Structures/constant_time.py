import time
import random

def access_element(arr, index):
    return arr[index]

if __name__ == "__main__":
    # Generate a random list for testing
    test_list = random.sample(range(1, 100000), 100)

    # Specify the number of repetitions for the operation
    num_repetitions = 1000

    total_time = 0.0
    for _ in range(num_repetitions):
        # Measure the time taken to access an element in an array
        start_time = time.time()
        result = access_element(test_list, 10)
        end_time = time.time()
        total_time += (end_time - start_time)

    average_time = total_time / num_repetitions
    print(f"Accessing an element in an array: {result}. Average time taken for {num_repetitions} repetitions: {average_time:.6f} seconds")
