originalList = []

# Input loop to add numbers to the list
while True:
    number = input("Press any number to add to the list or press Enter to terminate and sort: ")
    if number == "":
        # If the user presses Enter, break the input loop and proceed to sort the list
        break
    else:
        originalList.append(int(number))

print("Original list:", originalList)

# Bubble Sort algorithm to sort the list
n = len(originalList) #get the int equivalent of list(3,2,1) = 3

for i in range(n): #n = number of elements in the container
    
    swapped = False
    for j in range(0, n - i - 1):
        print("The value decreases each bubble up", n-i-1)
        print("The list becomes:", originalList)
        print("Compare " + str(originalList[j]) + " and " + str(originalList[j + 1]))
        if originalList[j] > originalList[j + 1]:
            # Swap the elements
            print("Numbers were swapped")
            originalList[j], originalList[j + 1] = originalList[j + 1], originalList[j]
            swapped = True

        input("Press Enter to continue to the next comparison...")

    # Print whether any numbers were swapped during this pass
    if swapped:
        print(f"Pass {i + 1}")
        print(f"Pass {i + 1}")
    else:
        print(f"Pass {i + 1}: Numbers were not swapped. The list is sorted.")
        break  # Optimization: If no swaps, the list is already sorted, so exit early.

print("Sorted list:", originalList)