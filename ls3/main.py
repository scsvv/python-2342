def binary_search(array, target, low, high):
    while low <= high: 
        
        mid = low + (high - low) // 2

        if array[mid] == target:
            return mid
        
        elif array[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1
    
    return -1


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    target = 4

    result = binary_search(array, target, 0, len(array)-1)

    if result != -1: 
        print(f"Element has index {result}")
    else: 
        print("No element in array")