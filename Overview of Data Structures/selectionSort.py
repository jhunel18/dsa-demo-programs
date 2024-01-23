def selection_sort(arr):
    n = len(arr)
    print(n)

    for i in range(n - 1):
        min_index = i
        print("The minimum index is", min_index)

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        # Print the comparison and the current state of the list after each swap
        print("Comparing values at indices", i, "and", min_index)
        print("Step", i + 1, ":", arr)

# Input loop to add numbers to the list
originalList = []
while True:
    number = input("Press any number to add to the list or press Enter to terminate and sort: ")
    if number == "":
        # If the user presses Enter, break the input loop and proceed to sort the list
        break
    else:
        originalList.append(int(number))

print("Original list:", originalList)

# Sort the list using Selection Sort
selection_sort(originalList)

print("Sorted list:", originalList)
