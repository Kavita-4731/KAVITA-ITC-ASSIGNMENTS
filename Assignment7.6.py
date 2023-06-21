def remove_duplicates(numbers):
    return list(set(numbers))

def selection_sort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

numbers = input("Enter a list of integer numbers (space-separated): ").split()
numbers = [int(num) for num in numbers]

numbers = remove_duplicates(numbers)

sorted_numbers_selection = selection_sort(numbers[:])

sorted_numbers_bubble = bubble_sort(numbers[:])

print("List without duplicates:")
print(numbers)

print("Sorted list using selection sort:")
print(sorted_numbers_selection)

print("Sorted list using bubble sort:")
print(sorted_numbers_bubble)
