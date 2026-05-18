def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [1001,1005,1010,1015,1020,1025]
target = 1015
result = binary_search(arr, target)

if result != -1:
    print(f"Employee found at index {result}")
else:
    print("Employee not found")
