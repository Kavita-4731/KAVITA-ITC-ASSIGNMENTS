def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def count_occurrences(arr, target):
    count = 0

    for num in arr:
        if num == target:
            count += 1

    return count

arr = list(map(int, input("Enter the elements of the array (separated by space): ").split()))

arr.sort()

element = int(input("Enter the element to search: "))

index = binary_search(arr, element)

if index != -1:
    print("Element found at index:", index)
    occurrences = count_occurrences(arr, element)
    print("Number of occurrences:", occurrences)
else:
    print("Element not found in the array.")
