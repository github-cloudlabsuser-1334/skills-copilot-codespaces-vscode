#         
# The function should take a list of numbers as input and return the sorted list.
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr  

# Example usage 
if __name__ == "__main__":
    test_list = [64, 34, 25, 12, 22, 11, 90, 11, 28, 55, 45,99]
    sorted_list = bubble_sort(test_list)
    print("Sorted array is:", sorted_list)  