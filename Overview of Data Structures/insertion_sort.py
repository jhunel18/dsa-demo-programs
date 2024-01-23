def insertion_sort(arr):
    n = len(arr)
    print(n)

    for i in range(1, n):
        key = arr[i]
        print('The value of key is at index : ',key)
        j = i - 1
        print('The value of js: ', j)

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            print()
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

        # Print the comparison and the current state of the list after each insertion
        print("Comparing value at index", i, "with previous elements")
        print("Step", i, ":", arr)

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

# Sort the list using Insertion Sort
insertion_sort(originalList)

print("Sorted list:", originalList)
