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

arr = [35,42,50,61,78,85,90]
target = 78
result = binary_search(arr, target)

if result != -1:
    print(f"Marks found at index {result}")
else:
    print("Marks not found")
